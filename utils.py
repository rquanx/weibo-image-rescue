import mimetypes
import os
import time
from constant import quality_map

def all_qualities():
    return [k for k in quality_map.keys()]

def all_qualities_str():
    return ",".join(all_qualities())


def generate_urls_of_all_qualities(url, qualities=None):
    # 如果没有提供qualities，则默认使用 "l"
    if qualities is None:
        qualities = all_qualities()
    # 映射质量值，如果不存在于quality_map中则直接使用输入值
    mapped_qualities = [quality_map.get(q, q) for q in qualities]
    # 获取原始质量部分
    parts = url.split('/')

    # 构建基础URL
    base_url = "/".join(parts[:-2]) + "/{q}/" + parts[-1]
    
    # 生成包含所有质量的URL
    urls = [base_url.replace("{q}", quality) for quality in mapped_qualities]
    
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
