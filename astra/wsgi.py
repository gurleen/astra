"""
astra web framework
author: Gurleen Singh<gs585@drexel.edu>
"""
from collections import namedtuple
from typing import Callable, Mapping, List, NamedTuple

from astra.router import Router


class Astra(object):

    router: Router

    def __init__(self):
        self.routes = []
        self.router = Router()

    def __call__(self, environ: Mapping, start_response: Callable) -> iter:
        print(environ["REQUEST_METHOD"], environ["RAW_URI"])
        handler: Callable = self.router.get_route(environ["RAW_URI"])
        response = handler()
        start_response(response.code, response.headers)
        return iter([response.content])

    def register_route(self, path: str) -> None:
        def inner(func):
            self.router.register_route(path, func)
            func()
        return inner