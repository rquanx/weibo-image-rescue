import httpx
import socket
from model import Result

class CustomHTTPTransport(httpx.AsyncHTTPTransport):
    def __init__(self, ip, *args, **kwargs):
        self.ip = ip
        super().__init__(*args, **kwargs)

    async def handle_async_request(self, request: httpx.Request) -> httpx.Response:
        # Override DNS resolution
        original_getaddrinfo = socket.getaddrinfo
        def getaddrinfo_override(*args, **kwargs):
            return [(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP, '', (self.ip, 0))]
        
        socket.getaddrinfo = getaddrinfo_override
        try:
            return await super().handle_async_request(request)
        finally:
            socket.getaddrinfo = original_getaddrinfo


async def request(url, headers, ip):
    transport = CustomHTTPTransport(ip)
    async with httpx.AsyncClient(http2=True, headers=headers, timeout=15.0, transport=transport) as client:
        try:
            response = await client.get(url)
            if response.headers.get('Content-Encoding') == 'br':
                body = brotli.decompress(response.content)
            else:
                body = response.content
            return Result(status=response.status_code, headers=response.headers, ip=ip, body=body)
        except Exception as e:
            return Result(err=e, ip=ip)