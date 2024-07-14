import requests
import json
import time
from threading import Lock
from .models import (
    MeasurementRequest,
    Location,
    ResponseOnSuccess,
    MeasurementResult,
    Probe,
)
import socket
import sys
from .config import (
    BASE_URL,
    REQUEST_TIMEOUT,
    GET_MEASUREMENT_INTERVAL,
    GET_MEASUREMENT_OVERALL_TIMEOUT,
    BASE_REQ_HEADERS,
    DEFAULT_REGIONS,
)


class Client:
    def __init__(self):
        self.session = requests.Session()
        self.etags = {}
        self.lock = Lock()

    def create_measurement(self, hostname, regions):
        if not hostname:
            raise ValueError("No hostname specified")
        if not regions:
            raise ValueError("No regions specified")

        locations = [Location(region=r, limit=5) for r in regions]
        req_body = MeasurementRequest(
            type="ping", target=hostname, locations=locations
        ).to_dict()
        url = f"{BASE_URL}/measurements"
        response = self.request("POST", url, json=req_body)
        if not response:
            raise Exception("No response from server")

        r = response.json()
        if r.get("probes_count") == 0:
            raise Exception("No probes available")
        if not r.get("id"):
            raise Exception(f"Invalid response: {response.text}")

        return r["id"]

    def get_measurement(self, measurement_id):
        if not measurement_id:
            raise ValueError("No measurement ID specified")

        url = f"{BASE_URL}/measurements/{measurement_id}"

        with self.lock:
            self.etags.pop(url, None)

        start_time = time.time()

        while time.time() - start_time < GET_MEASUREMENT_OVERALL_TIMEOUT:
            time.sleep(GET_MEASUREMENT_INTERVAL)
            response = self.request("GET", url)

            if not response:
                print(f"Measurement {measurement_id} in progress...", file=sys.stderr)
                continue

            r = response.json()
            if not r.get("id"):
                raise Exception(f"Invalid response: {response.text}")

            if r.get("status") == "in-progress":
                print(f"Measurement {r['id']} in progress...", file=sys.stderr)
                continue
            elif r.get("status") == "finished":
                return r.get("results", [])

        raise TimeoutError(f"Measurement {measurement_id} timed out")

    def request(self, method, url, **kwargs):
        headers = kwargs.pop("headers", BASE_REQ_HEADERS)
        response = self.session.request(
            method, url, headers=headers, timeout=REQUEST_TIMEOUT, **kwargs
        )

        if response.status_code == 304:
            return None
        response.raise_for_status()
        return response

    def resolve(self, hostname, locations=None):
        if locations is None:
            locations = DEFAULT_REGIONS

        mID = self.create_measurement(hostname, locations)
        mResults = self.get_measurement(mID)

        IPs = [
            socket.gethostbyname(result["result"]["resolvedAddress"])
            for result in mResults
            if result["result"]["resolvedAddress"]
        ]
        return IPs

    def probes(self):
        probes = self.get_probes()

        locations = [
            probe["location"]["region"]
            for probe in probes
            if probe["location"]["region"]
        ]
        return locations

    def locations(self):
        return DEFAULT_REGIONS

    def get_probes(self):
        url = f"{BASE_URL}/probes"
        response = self.request("GET", url)
        probes = response.json()
        return [Probe(**probe) for probe in probes]

