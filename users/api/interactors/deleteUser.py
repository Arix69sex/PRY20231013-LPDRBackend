from users.api.models import User

def deleteUserInteractor(id):
    try:
        userToDelete = User.objects.get(id)
        #TODO: add code to encrypt password
        #TODO: add code to validate email is actual email with RegEx
        userToDelete.delete()

        return True
    except Exception:
        return False