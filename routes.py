from astra.blueprints import Blueprint
from astra.response import Response

blueprint = Blueprint("/path")

@blueprint.route("/")
def blueprint_test(request):
    return Response("Hello from a blueprint!")