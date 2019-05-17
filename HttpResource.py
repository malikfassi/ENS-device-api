from flask import make_response
from flask.json import jsonify


class HttpResource:
    @staticmethod
    def success(obj=None):
        if obj is None:
            obj = {'success': True}
        http_response = make_response(jsonify(obj))
        return http_response