import mimetypes
import os
import time


def generate_urls_of_all_qualities(url):
    qualities = ["large", "mw690", "thumb150"]
    urls = [url.replace("large", quality) for quality in qualities]
    return urls


def save_file(path, content):
    with open(path, "wb") as f:
        f.write(content)


def generate_file_name(path, url, content_type, filename):
    if not filename or filename in [".", "/"]:
        filename = os.path.basename(path) or str(int(time.time()))
        mime_type = (
            content_type or mimetypes.guess_type(url)[0] or "application/octet-stream"
        )
        ext = mimetypes.guess_extension(mime_type)
        filename += ext or ".bin"
    return filename
