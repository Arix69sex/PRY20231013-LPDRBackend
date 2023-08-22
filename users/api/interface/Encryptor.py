from django.contrib.auth.hashers import check_password
from django.contrib.auth.hashers import make_password

class Encryptor:

    def encrypt(self, data):
        return make_password(data)

    def verify(self, data, storedData):
        return check_password(data, storedData)
