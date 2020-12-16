"""
astra web framework
author: Gurleen Singh<gs585@drexel.edu>
"""
from typing import List

from astra.router import Route

class Blueprint:
    routes = []

    def __init__(self, base_route: str):
        self.base_route = base_route

    def route(self, path: str, methods: List[str] = ["GET"]) -> None:
        path = self.base_route + path
        def inner(func):
            self.routes.append(Route(path, func, methods))
        return inner

    def get_routes(self) -> List[Route]:
        return self.routes