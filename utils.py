import mimetypes
import os
import time
from constant import quality_map


def generate_urls_of_all_qualities(url, qualities=None):
    # 如果没有提供qualities，则默认使用 "l"
    if qualities is None:
        qualities = ["l"]
    
    # 映射质量值，如果不存在于quality_map中则直接使用输入值
    mapped_qualities = [quality_map.get(q, q) for q in qualities]
    
    # 获取原始质量部分
    parts = url.split('/')
    original_quality = parts[-2]
    
    # 如果原始质量不在映射中，追加进去
    predefined_qualities = list(quality_map.values())
    if original_quality not in predefined_qualities:
        predefined_qualities.append(original_quality)
    
    # 构建基础URL
    base_url = "/".join(parts[:-2]) + "/{q}/" + parts[-1]
    
    # 生成包含所有质量的URL
    urls = [base_url.replace("{q}", quality) for quality in set(mapped_qualities)]
    
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
