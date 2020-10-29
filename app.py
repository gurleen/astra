"""
astra web framework
author: Gurleen Singh<gs585@drexel.edu>
"""
from astra.wsgi import Astra, Response

app = Astra()


def hello():
    return Response(b"Hello, world!", "200 OK", [
                ("Content-type", "text/plain"),
                ("Content-length", str(len("Hello, world!")))
            ])


app.register_route("", hello)