from urllib.parse import urlparse
import os
from tqdm import tqdm
import asyncio
from args import parse_args
from constant import base_headers, output_dir
from cdn import load_cdn_info, update_cdn_info
from custom_transport import request
from utils import generate_file_name, save_file


async def rescue_requests(url, ips, headers, pbar):
    tasks = [request(url, headers, ip) for ip in ips]
    results = []
    for task in asyncio.as_completed(tasks):
        res = await task
        results.append(res)
        pbar.update(1)
    return results


async def rescue(urls, ips, dir, filename=None):
    total_tasks = len(urls) * len(ips)
    with tqdm(total=total_tasks) as pbar:
        for url in urls:
            u = urlparse(url)
            tqdm.write(f"Started rescue for {url}")
            results = await rescue_requests(url, ips, base_headers, pbar)
            result = None
            for res in results:
                if res.err or res.status != 200:
                    continue
                result = res
                break
            
            if not result or result.status != 200:
                tqdm.write(f"[FAILED] Unfortunately, {url} all {len(ips)} resolves failed.")
                continue
            
            tqdm.write(f"[SUCCESS] {url} | {result.ip} | {len(result.body)}")
            
            filename = generate_file_name(u.path, url, result.headers.get("content-type"), filename)
            path = os.path.join(dir, filename)
            if not os.path.exists(dir):
                os.makedirs(dir)
            save_file(path, result.body)
            tqdm.write(f"Saved {url} to {path}")


def main(args=None):
    if args is None:
        args = parse_args(None)
    else:
        args = parse_args(args)

    if args.u:
        update_cdn_info()
        return

    if args.f:
        update_cdn_info()
        image_url = args.f
    else:
        image_url = args.image_url

    if not image_url:
        print("Image URL is required.")
        return

    ips = load_cdn_info()

    if not ips:
        print("No cached resolves found, please run the -u command first")
        return

    print(f"Using {len(ips)} cached resolves.")
    asyncio.run(rescue([image_url], ips, f"./{output_dir}/"))


if __name__ == "__main__":
    main()
