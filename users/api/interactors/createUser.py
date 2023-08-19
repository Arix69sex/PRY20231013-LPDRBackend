from users.api.models import User

def createUserInteractor(email, password):
    try:
        #TODO: add code to encrypt password
        #TODO: add code to validate email is actual email with RegEx
        new_user = User(email=email, password=password)
        new_user.save()

        return True
    except Exception:
        return False