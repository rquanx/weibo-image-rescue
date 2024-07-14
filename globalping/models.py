class MeasurementRequest:
    def __init__(self, type, target, locations, ping_options=None, http_options=None):
        self.type = type
        self.target = target
        self.locations = locations
        self.ping_options = ping_options
        self.http_options = http_options

    def to_dict(self):
        if not self.target:
            raise ValueError(".target is empty")
        if not self.locations:
            raise ValueError(".locations is empty")

        data = {
            "type": self.type,
            "target": self.target,
            "locations": [loc.to_dict() for loc in self.locations],
        }

        if self.type == "ping":
            if self.ping_options is None:
                self.ping_options = PingOptions()
            if self.ping_options.packets_count == 0:
                self.ping_options.packets_count = 1
            data["measurementOptions"] = self.ping_options.to_dict()
        elif self.type == "http":
            if self.http_options is None:
                self.http_options = HttpOptions()
            data["measurementOptions"] = self.http_options.to_dict()
        else:
            raise ValueError(f"Unknown .type: {self.type}")

        return data


class MeasurementType:
    PING = "ping"
    HTTP = "http"


class PingOptions:
    def __init__(self, packets_count=1):
        self.packets_count = packets_count

    def to_dict(self):
        return {"packets": self.packets_count}


class HttpOptions:
    def __init__(
        self,
        protocol="HTTP",
        method="HEAD",
        headers=None,
        host="",
        path="",
        query="",
        port=80,
    ):
        self.protocol = protocol
        self.method = method
        self.headers = headers or {}
        self.host = host
        self.path = path
        self.query = query
        self.port = port

    def to_dict(self):
        return {
            "protocol": self.protocol,
            "request": {
                "method": self.method,
                "headers": self.headers,
                "host": self.host,
                "path": self.path,
                "query": self.query,
            },
            "port": self.port,
        }


class Location:
    def __init__(self, region, country="", city="", limit=5):
        self.region = region
        self.country = country
        self.city = city
        self.limit = limit

    def to_dict(self):
        data = {"region": self.region, "limit": self.limit}
        if self.country:
            data["country"] = self.country
        if self.city:
            data["city"] = self.city
        return data


class ResponseOnSuccess:
    def __init__(self, id, status, results, probes_count):
        self.id = id
        self.status = status
        self.results = results
        self.probes_count = probes_count


class ResponseOnError:
    def __init__(self, error):
        self.error = error


class MeasurementResult:
    def __init__(self, result, probe):
        self.result = result
        self.probe = probe


class Probe:
    def __init__(self, location):
        self.location = location
