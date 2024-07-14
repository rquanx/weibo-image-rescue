import json
import dns.resolver
import os
import concurrent.futures
from tqdm import tqdm

from constant import cdn_file, public_dns_servers, domains


def get_cdn_ips(domain, dns_server):
    resolver = dns.resolver.Resolver()
    resolver.nameservers = [dns_server]
    try:
        answers = resolver.resolve(domain, "A")
        return [rdata.address for rdata in answers]
    except Exception:
        return []


def update_cdn_info():
    cdn_ips = set()
    total_tasks = len(domains) * len(public_dns_servers) * 3  # 多次查询以增加IP数

    def resolve_domain_with_dns(domain, dns_server):
        ips = get_cdn_ips(domain, dns_server)
        return ips

    with tqdm(total=total_tasks) as pbar:
        with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
            future_to_domain = {
                executor.submit(resolve_domain_with_dns, domain, dns_server): (domain, dns_server)
                for domain in domains
                for dns_server in public_dns_servers
                for _ in range(3)
            }
            for future in concurrent.futures.as_completed(future_to_domain):
                try:
                    ips = future.result()
                    cdn_ips.update(ips)
                except Exception:
                    pass
                pbar.update(1)

    cdn_ips = list(cdn_ips)  # 去重
    with open(cdn_file, "w") as f:
        json.dump(cdn_ips, f)
    print(f"\nCDN information updated. Total CDN IPs: {len(cdn_ips)}")


def load_cdn_info():
    if not os.path.exists(cdn_file) or os.path.getsize(cdn_file) == 0:
        update_cdn_info()
    with open(cdn_file, "r") as f:
        cdn_ips = json.load(f)
    return cdn_ips
