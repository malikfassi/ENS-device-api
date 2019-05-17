from flask import Blueprint, request

from HttpResource import HttpResource
from api.DeviceService import DeviceService
from flask_cors import cross_origin

class Controller:

    routes = Blueprint('routes', __name__)
    device_service = DeviceService()

    @cross_origin()
    @staticmethod
    @routes.route('/_health', methods=['GET'])
    def get_health():
        return HttpResource.success()

    @cross_origin()
    @staticmethod
    @routes.route('/pub_key', methods=['GET'])
    def get_pub_key():
        pub_key = Controller.device_service.get_pub_key()
        return HttpResource.success(pub_key)

    @cross_origin()
    @staticmethod
    @routes.route('/decrypt', methods=['POST'])
    def decrypt():
        decrypted = Controller.device_service.decrypt(request.json['encryptedAddress'])
        return HttpResource.success(decrypted)

    @cross_origin()
    @staticmethod
    @routes.route('/verify', methods=['POST'])
    def verify():
        print(request.json)
        decrypted = Controller.device_service.verify(request.json['encryptedAddress'], request.json['name'])
        return HttpResource.success(decrypted)

    @cross_origin()
    @staticmethod
    @routes.route('/encrypt', methods=['POST'])
    def encrypt():
        encrypted = Controller.device_service.encrypt(request.json)
        return HttpResource.success(encrypted)
