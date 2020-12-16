"""
astra web framework
author: Gurleen Singh<gs585@drexel.edu>
"""
from astra.response import Response


def error_404(request):
    return Response("Not Found", 404)

def error_405(request):
    return Response("Method Not Allowed", 405)