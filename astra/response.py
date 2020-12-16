"""
astra web framework
author: Gurleen Singh<gs585@drexel.edu>
"""
import json
import typing

DEFAULT_HEADERS = [
    ("Content-type", "text/plain"),
]

STATUS_CODES = {
    200: "200 OK",
    301: "301 Moved Permanently",
    404: "404 Not Found",
    405: "405 Method Not Allowed"
}


class Response:
    def __init__(self, content, code=200, headers=DEFAULT_HEADERS):
        if type(content) in [dict, list]:
            content = json.dumps(content)

        self.content = content.encode("ascii")
        self.code = STATUS_CODES.get(code, "200 OK")
        self.headers = headers
