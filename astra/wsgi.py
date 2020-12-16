"""
astra web framework
author: Gurleen Singh<gs585@drexel.edu>
"""
from collections import namedtuple
from typing import Callable, Mapping, List, NamedTuple

from astra.router import Router
from astra.request import Request
from astra.default_responses import error_405

class Astra(object):

    router: Router

    def __init__(self):
        self.router = Router()

    def __call__(self, environ: Mapping, start_response: Callable) -> iter:
        uri = environ["RAW_URI"]
        method = environ["REQUEST_METHOD"]
        route, params, method_allowed = self.router.get_route(uri, method)
        request = Request(uri, params, environ)

        if not method_allowed:
            response = error_405(request)
        else:
            response = route.handler(request)
        
        start_response(response.code, response.headers)
        return iter([response.content])

    def route(self, path: str, methods: List[str] = ["GET"]) -> None:
        def inner(func):
            self.router.register_route(path, func, methods)
        return inner
