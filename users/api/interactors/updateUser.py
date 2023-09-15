
def updateUserInteractor(userToUpdate, email=None, password=None):
    try:
        #TODO: add code to encrypt password
        #TODO: add code to validate email is actual email with RegEx
        if email: userToUpdate.email = email;
        if password: userToUpdate.password = password;
        userToUpdate.save()

        return True
    except Exception as e:
        print("error", e)
        return False