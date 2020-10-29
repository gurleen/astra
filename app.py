"""
astra web framework
author: Gurleen Singh<gs585@drexel.edu>
"""
from astra.wsgi import Astra
from astra.response import Response


app = Astra()


@app.register_route("/")
def hello():
    return Response("Hello, world!")


@app.register_route("/test")
def test():
	return Response("This is a test")