import json
import os
from constant import cdn_file, domains
from globalping.cache import cache


def update_cdn_info():
    cdn_ips = cache(domains, force=True)
    with open(cdn_file, "w") as f:
        json.dump(cdn_ips, f)
    print(f"\nCDN information updated. Total CDN IPs: {len(cdn_ips)}")


def load_cdn_info():
    if not os.path.exists(cdn_file) or os.path.getsize(cdn_file) == 0:
        update_cdn_info()
    with open(cdn_file, "r") as f:
        cdn_ips = json.load(f)
    return cdn_ips
