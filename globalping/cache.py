import threading
import queue
import sys

from .client import Client

def unique(items):
    return list(set(items))

def unique_ips(ip_list):
    seen = set()
    unique_list = []
    for item in ip_list:
        if item not in seen:
            unique_list.append(item)
            seen.add(item)
    return unique_list

def cache(hostnames, force=False):
    provider = Client()
    
    try:
        locations = provider.locations()
    except Exception as e:
        raise Exception(f"failed to get locations: {str(e)}")

    locations = unique(locations)
    print(f"Using {len(locations)} locations.")

    wg = threading.Event()
    ch = queue.Queue(len(hostnames))

    def resolve_hostname(hostname):
        try:
            ips = provider.resolve(hostname, locations)
            ch.put(ips)
        except Exception as e:
            print(f'Failed to resolve "{hostname}": {str(e)}', file=sys.stderr)
            ch.put(None)
        finally:
            wg.set()

    for h in hostnames:
        threading.Thread(target=resolve_hostname, args=(h,)).start()

    wg.wait()

    resolves = []
    if not force:
        resolves = resolves

    for _ in range(len(hostnames)):
        result = ch.get()
        if result is not None:
            resolves.extend(result)
    ip_list = unique_ips(resolves)
    return ip_list
