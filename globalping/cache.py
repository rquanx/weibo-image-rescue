from concurrent.futures import ThreadPoolExecutor, as_completed
import queue
from tqdm import tqdm
from .client import Client


def cache(hostnames, force=False):
    provider = Client()
    
    try:
        locations = provider.locations()
    except Exception as e:
        raise Exception(f"failed to get locations: {str(e)}")

    locations = unique(locations)
    print(f"Using {len(locations)} locations.")

    ch = queue.Queue(len(hostnames))
    progress_bar = tqdm(total=len(hostnames), desc="Resolving hostnames")

    def resolve_hostname(hostname):
        try:
            ips = provider.resolve(hostname, locations)
            ch.put(ips)
        except Exception as e:
            # print(f'Failed to resolve "{hostname}": {str(e)}', file=sys.stderr)
            ch.put(None)
        finally:
            progress_bar.update(1)

    with ThreadPoolExecutor(max_workers=len(hostnames)) as executor:
        futures = [executor.submit(resolve_hostname, h) for h in hostnames]
        for future in as_completed(futures):
            pass

    progress_bar.close()

    resolves = []
    if not force:
        resolves = resolves

    while not ch.empty():
        result = ch.get()
        if result is not None:
            resolves.extend(result)
    ip_list = unique_ips(resolves)
    return ip_list

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
