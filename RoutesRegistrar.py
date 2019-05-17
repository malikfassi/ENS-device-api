from api.Controller import Controller


class RoutesRegistrar:

    BLUEPRINTS = [
        Controller.routes,
    ]

    def __init__(self, app):
        self.app = app

    def register(self):
        for blueprint in self.BLUEPRINTS:
            self.app.register_blueprint(blueprint)