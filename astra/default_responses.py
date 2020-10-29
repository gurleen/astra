"""
astra web framework
author: Gurleen Singh<gs585@drexel.edu>
"""
from astra.response import Response


def error_404():
	return Response("Not Found", 404)