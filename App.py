from flask import Flask

from RoutesRegistrar import RoutesRegistrar


class App(Flask):
    def __init__(self):

        super().__init__(__name__)
        RoutesRegistrar(self).register()
