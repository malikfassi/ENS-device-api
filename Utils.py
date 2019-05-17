from cryptography.hazmat.primitives import serialization
import simplejson as json


class Utils:

    @staticmethod
    def serialize_key(public_key):
        pem = public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )
        return json.dumps(pem)