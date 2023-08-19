from users.api.models import User

def updateUserInteractor(id, email=None, password=None):
    try:
        userToUpdate = User.objects.get(id)
        #TODO: add code to encrypt password
        #TODO: add code to validate email is actual email with RegEx
        if email: userToUpdate.email = email;
        if password: userToUpdate.password = password;
        userToUpdate.save()

        return True
    except Exception:
        return False