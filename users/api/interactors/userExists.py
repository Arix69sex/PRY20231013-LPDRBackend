from users.api.models import User

def userExists(email):
    return User.objects.filter(email=email).exists()