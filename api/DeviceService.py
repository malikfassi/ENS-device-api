import base64

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from singleton_decorator import singleton
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes

from Utils import Utils


@singleton
class DeviceService:

    def __init__(self):

        self.private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048,
            backend=default_backend()
        )
        self.public_key = self.private_key.public_key()

    def get_pub_key(self):
        return {'pub_key': Utils.serialize_key(self.public_key)}

    def decrypt(self, json_data):
        encrypted_message = json_data['message']
        encrypted_message = base64.b64decode(encrypted_message)
        original_message = self.private_key.decrypt(
            encrypted_message,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        return original_message

    def encrypt(self, json_data):
        message = json_data['message'].encode()
        encrypted_message = self.public_key.encrypt(
            message,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        return str(base64.b64encode(encrypted_message), 'utf-8')