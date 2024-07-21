base_headers = {
    "Accept": "image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Referer": "https://weibo.com/",
    "Sec-Ch-Ua": 'Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24',
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": "Windows",
    "Sec-Fetch-Dest": "image",
    "Sec-Fetch-Mode": "no-cors",
    "Sec-Fetch-Site": "cross-site",
    # "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
}

output_dir = "images"


cdn_file = "cdn.json"


# public_dns_servers = [
#     "8.8.8.8",        # Google Public DNS (USA)
#     "8.8.4.4",        # Google Public DNS (USA)
#     "1.1.1.1",        # Cloudflare DNS (Global)
#     "1.0.0.1",        # Cloudflare DNS (Global)
#     "9.9.9.9",        # Quad9 DNS (Global)
#     "149.112.112.112",# Quad9 Secondary DNS (Global)
#     "208.67.222.222", # OpenDNS (Global)
#     "208.67.220.220", # OpenDNS Secondary (Global)
#     "180.76.76.76",   # Baidu Public DNS (China)
#     "114.114.114.114",# 114 DNS (China)
#     "168.95.1.1",     # HiNet DNS (Taiwan)
#     "77.88.8.8",      # Yandex DNS (Russia)
#     "77.88.8.1",      # Yandex DNS (Russia)
#     "74.82.42.42",    # Hurricane Electric DNS (USA)
#     "129.250.35.250", # NTT DNS (Japan)
#     "4.2.2.1",        # Level3 DNS (USA)
#     "4.2.2.2",        # Level3 DNS (USA)
#     "8.26.56.26",     # Comodo Secure DNS (Global)
#     "8.20.247.20",    # Comodo Secure DNS (Global)
#     "64.6.64.6",      # Verisign DNS (Global)
#     "64.6.65.6",      # Verisign DNS (Global)
#     "1.2.4.8",        # DNSPod Public DNS+ (China)
# ]


domains = ["wx1.sinaimg.cn", "wx2.sinaimg.cn", "wx3.sinaimg.cn", "wx4.sinaimg.cn"]


quality_map = {
    "l": "large",
    "m": "mw690",
    "t": "thumb150",
    "ml": "mw2000",
    "o": "orj360",
}


VALID_IMAGE_URL = "https://wx4.sinaimg.cn/mw690/41d692acgy1hrnmhkowr6j20be0be3yq.jpg"
INVALID_IMAGE_URL = "https://wx3.sinaimg.cn/mw690/41d692acgy1hrnmhkdmqfj20be0beaag.jpg"
ABSOLUTE_INVALID_IMAGE_URL = (
    "https://wx3.sinaimg.cn/mw2000/ede975b2gy1hrosk73sx0j20ib0i4q9c.jpg"
)
