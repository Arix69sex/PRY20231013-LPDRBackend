import jwt
from decouple import config

class JWT:
    def encode(self, payload):
        secret = config('SECRET_KEY')
        token = jwt.encode(payload, secret, algorithm="HS256");
        return token
    def decode(self, token):
        secret = config('SECRET_KEY')
        print("toekn", token)
        payload = jwt.decode(token, secret, algorithms=["HS256"])
        return payload