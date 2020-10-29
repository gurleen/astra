"""
astra web framework
author: Gurleen Singh<gs585@drexel.edu>
"""
from collections import namedtuple
from typing import Callable, Mapping, List, NamedTuple

Route = namedtuple("Route", ["path", "handler"])
Response = namedtuple("Response", ["content", "status", "headers"])

class Astra(object):

    routes: List[Route]

    def __init__(self):
        self.routes = []

    def __call__(self, environ: Mapping, start_response: Callable) -> iter:
        print(environ["REQUEST_METHOD"], environ["QUERY_STRING"])
        handler = self.get_route(environ["QUERY_STRING"])
        response: Response = handler()
        start_response(response.status, response.headers)
        return iter([response.content])

    def register_route(self, path: str, handler: Callable) -> None:
        self.routes.append(Route(path, handler))

    def get_route(self, query) -> Callable:
        for route in self.routes:
            if route.path == query:
                return route.handler
        return self.error_404

    def error_404(self):
        return Response(b"Not Found", "404 Not Found", [
                ("Content-type", "text/plain"),
                ("Content-length", str(len("Not Found")))
            ])