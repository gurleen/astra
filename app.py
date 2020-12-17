"""
astra web framework
author: Gurleen Singh<gs585@drexel.edu>
"""
from routes import blueprint

from astra.wsgi import Astra
from astra.response import Response
from astra.blueprints import Blueprint

app = Astra()

@app.route("/")
def hello(request):
    return Response("Hello, world!")


@app.route("/test")
def test(request):
    return Response("This is a test")


@app.route("/user/:name")
def testwitharg(request):
    name = request.params.get("name", "name")
    message = {"message": f"Hello, {name}!"}
    return Response(message)

app.register_blueprint(blueprint)

if __name__ == "__main__":
    app.run(8000)