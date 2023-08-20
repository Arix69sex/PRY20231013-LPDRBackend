from usersData.api.models import UserData

def createUserDataByIdInteractor(user, identification, names, lastNames, address, phoneNumber):
    try:
        UserData.objects.create(user=user, identification= identification, names=names, lastNames=lastNames, address=address, phoneNumber=phoneNumber)
        return True
    except Exception as e:
        print("error: ", e)
        return False