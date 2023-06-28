from flask.views import View


class ExampleView(View):
    def dispatch_request(self):
        return "Example"
