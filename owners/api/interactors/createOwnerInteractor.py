from owners.api.models import Owner

def createOwnerInteractor(licensePlate, identification, names, lastNames, address, phoneNumber):
    try:
        Owner.objects.create(licensePlate=licensePlate, identification= identification, names=names, lastNames=lastNames, address=address, phoneNumber=phoneNumber)
        return True
    except Exception as e:
        print("error: ", e)
        return False