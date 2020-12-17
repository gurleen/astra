"""
astra web framework
"""


class Request:
    def __init__(self, route, params, env):
        self.route = route
        self.params = params
        self.env = env
        self.body = None
