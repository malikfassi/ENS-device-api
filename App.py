from flask import Flask

from flask_cors import CORS
from RoutesRegistrar import RoutesRegistrar
import logging


class App(Flask):
    def __init__(self):

        super().__init__(__name__)
        RoutesRegistrar(self).register()
        cors = CORS(self)
        self.config['CORS_HEADERS'] = 'Content-Type'

        log = logging.getLogger('werkzeug')
        log.disabled = True