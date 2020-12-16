# Astra 🚀

Astra is a tiny Flask-esque web framework. It provides you with a basic `Request` and `Response` objects, as well as more advanced routing through the `Blueprint` object. URL parameters are supported. It requires no outside dependencies (not even [Werkzeug](https://github.com/pallets/werkzeug) or [WebOb](https://github.com/Pylons/webob), two awesome projects).

As someone who writes a lot of backend code, I wrote this in order to learn how web frameworks work. As such, I make no guarantees about the performance/security of this code, and I highly reccomend that you do not use it in production. You may find it useful in a small personal project, though 😄 .

## Installing

```bash
git clone https://github.com/gurleens2000/astra-web
cd astra-web
pip install .
```

## Example

```python
from astra.wsgi import Astra
from astra.response import Response
from astra.blueprints import Blueprint

app = Astra()

@app.route("/", methods=["GET"])
def hello(request):
    return Response("Hello, world!")

@app.route("/user/:name")
def username(request):
    name = request.params.get("name")
    # Response supports text as well as dicts/lists (serialized as JSON)
    return Response({"msg": f"Hello, {name}!"})

blueprint = Blueprint("/blueprint")

@blueprint.path("/")
def blueprint_test(request):
    return Response("Hello from a blueprint!")
```

Run it using any WSGI-compliant server. I use [Gunicorn](https://github.com/benoitc/gunicorn) and have provided a run script for it:

`./run.sh`

You can also use [wsgiref](https://docs.python.org/3/library/wsgiref.html) which is a part of the Python standard library. I will make this functionality built-in at some point.
