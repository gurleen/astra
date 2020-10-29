"""
astra web framework
author: Gurleen Singh<gs585@drexel.edu>
"""
from typing import List, Callable
from dataclasses import dataclass

from astra.default_responses import error_404

@dataclass
class Route:
	path: str
	handler: Callable


class Router:

	routes: List[Route]

	def __init__(self):
		self.routes = []

	def get_route(self, path) -> Callable:
		for route in self.routes:
			if route.path == path:
				return route.handler
		return error_404

	def register_route(self, path, handler):
		self.routes.append(Route(path, handler))