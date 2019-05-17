from flask import Blueprint, request

from HttpResource import HttpResource
from api.DeviceService import DeviceService


class Controller:

    routes = Blueprint('routes', __name__)
    device_service = DeviceService()

    @staticmethod
    @routes.route('/_health', methods=['GET'])
    def get_health():
        return HttpResource.success()

    @staticmethod
    @routes.route('/pub_key', methods=['GET'])
    def get_pub_key():
        pub_key = Controller.device_service.get_pub_key()
        return HttpResource.success(pub_key)

    @staticmethod
    @routes.route('/decrypt', methods=['POST'])
    def decrypt():
        decrypted = Controller.device_service.decrypt(request.json)
        return HttpResource.success(decrypted)

    @staticmethod
    @routes.route('/encrypt', methods=['POST'])
    def encrypt():
        encrypted = Controller.device_service.encrypt(request.json)
        return HttpResource.success(encrypted)
