class Result:
    def __init__(self, err=None, headers=None, ip=None, url = None,body=None, status=None):
        self.err = err
        self.headers = headers
        self.ip = ip
        self.body = body
        self.status = status
        self.url = url
