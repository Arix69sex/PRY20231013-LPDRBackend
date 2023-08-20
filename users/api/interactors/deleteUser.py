
def deleteUserInteractor(userToDelete):
    try:
        userToDelete.delete()

        return True
    except Exception:
        return False