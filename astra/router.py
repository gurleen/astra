"""
astra web framework
author: Gurleen Singh<gs585@drexel.edu>
"""
from typing import List, Callable, Mapping
from dataclasses import dataclass

from astra.default_responses import error_404
from astra.response import Response


@dataclass
class Route:
    path: str
    handler: Callable
    methods: List[str]

    def __init__(self, path, handler, methods=[]):
        self.path = path
        self.handler = handler
        self.methods = methods


class Router:

    routes: List[Route]

    def __init__(self):
        self.routes = []

    def get_route(self, path, method):
        for route in self.routes:
            params = self.match(path.rstrip("/"), route.path)
            if params == None:
                continue
            else:
                method_allowed = (method in route.methods)
                return route, params, method_allowed
        return Route("/", error_404), {}, True

    def match(self, path, route):
        params = dict()
        path_split, route_split = path.split("/"), route.split("/")
        if route_split == ["", ""]:
            route_split.pop()
        if len(path_split) != len(route_split):
            return None
        for path_comp, route_comp in zip(path_split, route_split):
            is_var = route_comp.startswith(":")
            if is_var:
                key = route_comp[1:]
                params[key] = path_comp
            else:
                if path_comp != route_comp:
                    return None
        return params

    def register_route(self, path, handler, methods):
        self.routes.append(Route(path, handler, methods))
