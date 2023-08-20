from usersData.api.interactors.getUserDataByUserInteractor import getUserDataByUserInteractor


def validateUserHasData(user):
    hasUserData = getUserDataByUserInteractor(user)
    if hasUserData.exists():
        raise Exception("User doesn't have User Data")