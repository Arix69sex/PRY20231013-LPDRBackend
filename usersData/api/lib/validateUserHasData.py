from usersData.api.interactors.getUserDataByUserInteractor import getUserDataByUserInteractor


def validateUserHasData(user):
    hasUserData = getUserDataByUserInteractor(user)
    if hasUserData.exists():
        raise Exception("User already has User Data")