from urllib.parse import urlparse
import os
from tqdm import tqdm
import asyncio
from args import parse_args
from constant import base_headers, output_dir
from cdn import load_cdn_info, update_cdn_info
from custom_transport import request
from utils import generate_file_name, generate_urls_of_all_qualities, save_file
import concurrent.futures


def save(result, dir, filename):
    u = urlparse(result.url)
    filename = generate_file_name(
        u.path, result.url, result.headers.get("content-type"), filename
    )
    path = os.path.join(dir, filename)
    if not os.path.exists(dir):
        os.makedirs(dir)
    save_file(path, result.body)
    print(f"Saved {result.url} to {path}")


def create_tasks(urls, ips) -> list[tuple]:
    tasks = []
    for url in urls:
        for ip in ips:
            tasks.append((url, ip))
    return tasks


def request_task(url, ip):
    return asyncio.run(request(url, base_headers, ip))


def rescue(urls, ips, dir, filename=None):
    total_tasks = len(urls) * len(ips)
    tasks = create_tasks(urls, ips)
    result = None

    with tqdm(
        total=total_tasks, desc="Rescuing"
    ) as pbar, concurrent.futures.ThreadPoolExecutor() as executor:
        future_to_task = {
            executor.submit(request_task, url, ip): (url, ip) for url, ip in tasks
        }

        for future in concurrent.futures.as_completed(future_to_task):
            task_result = future.result()
            pbar.update(1)
            if task_result and task_result.status == 200:
                result = task_result
                for f in future_to_task:
                    f.cancel()
                break
        pbar.n = pbar.total
        pbar.refresh()

    if not result:
        print(f"[FAILED] Unfortunately, all {total_tasks} resolves failed.")
        return
    print(f"[SUCCESS] {result.url} | {result.ip} | {len(result.body)}")
    save(result, dir, filename)


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
    qualities = args.q.split(',')
    urls = generate_urls_of_all_qualities(image_url, qualities)
    rescue(urls, ips, f"./{output_dir}/")


if __name__ == "__main__":
    main()
