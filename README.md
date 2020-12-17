# Astra 🚀

Astra is a tiny Flask-esque web framework. It provides you with basic `Request` and `Response` objects, as well as more advanced routing through the `Blueprint` object. URL parameters are supported. It requires no outside dependencies (not even [Werkzeug](https://github.com/pallets/werkzeug) or [WebOb](https://github.com/Pylons/webob), two awesome projects).

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

app.register_blueprint(blueprint)

if __name__ == "__main__":
    app.run(8000)
```

This will serve the app on [http://localhost:8000/](http://localhost:8000/) using wsgiref, Python's built-in WSGI server. You can use any WSGI-compliant server, such as [Gunicorn](https://gunicorn.org/). The supplied `run.sh` script runs the example app via Gunicorn.
