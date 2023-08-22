from users.api.models import User

def createUserInteractor(email, password):
    try:
        new_user = User(email=email, password=password)
        new_user.save()

        return new_user
    except Exception:
        return False