from cryptography.hazmat.primitives import serialization
import simplejson as json

class Utils:
    BLACK = lambda x: '\033[30m' + str(x) + Utils.RESET("")
    RED = lambda x: '\033[31m' + str(x) + Utils.RESET("")
    GREEN = lambda x: '\033[32m' + str(x) + Utils.RESET("")
    YELLOW = lambda x: '\033[33m' + str(x) + Utils.RESET("")
    BLUE = lambda x: '\033[34m' + str(x) + Utils.RESET("")
    MAGENTA = lambda x: '\033[35m' + str(x) + Utils.RESET("")
    CYAN = lambda x: '\033[36m' + str(x) + Utils.RESET("")
    WHITE = lambda x: '\033[37m' + str(x) + Utils.RESET("")
    UNDERLINE = lambda x: '\033[4m' + str(x) + Utils.RESET("")
    RESET = lambda x: '\033[0m' + str(x)

    @staticmethod
    def serialize_key(public_key):
        pem = public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )
        return str(pem.decode())



