"""
astra web framework
author: Gurleen Singh<gs585@drexel.edu>
"""
import json
from collections import namedtuple
from typing import Callable, Mapping, List, NamedTuple
from wsgiref.simple_server import make_server

from astra.router import Router
from astra.request import Request
from astra.response import DEFAULT_HEADERS
from astra.blueprints import Blueprint
from astra.exceptions import AstraException

class Astra(object):

    router: Router
    middleware: List[Callable]

    def __init__(self):
        self.router = Router()
        self.middleware = []

    def __call__(self, environ: Mapping, start_response: Callable) -> iter:
        try:
            uri = environ["PATH_INFO"]
            method = environ["REQUEST_METHOD"]
            print(self.router.routes)
            route, params = self.router.get_route(uri, method)
            request = Request(uri, params, environ)
            if method == "POST" and "wsgi.input" in environ:
                body = environ.get("wsgi.input").read()
                if environ.get("CONTENT_TYPE", "") == "application/json":
                    body = json.loads(body)
                request.body = body

            for handler in self.middleware:
                request = handler(request)

            response = route.handler(request)
        except AstraException as e:
            start_response(str(e.status_code), DEFAULT_HEADERS)
            return iter([e.message.encode("ascii")])
        
        start_response(response.code, response.headers)
        return iter([response.content])

    def route(self, path: str, methods: List[str] = ["GET"]) -> None:
        def inner(func):
            self.router.register_route(path, func, methods)
        return inner

    def register_blueprint(self, blueprint: Blueprint) -> None:
        for route in blueprint.get_routes():
            self.router.register_route_instance(route)

    def register_middleware(self, handler: Callable) -> None:
        self.middleware.append(handler)

    def run(self, port=8000):
        with make_server('', port, self) as httpd:
            print(f"Serving on port {port}...")
            httpd.serve_forever()