def updateOwnerInteractor(OwnerToUpdate, identification, names, lastNames, address, phoneNumber):
    try:
        if identification: OwnerToUpdate.identification = identification;
        if names: OwnerToUpdate.names = names;
        if lastNames: OwnerToUpdate.lastNames = lastNames;
        if address: OwnerToUpdate.address = address;
        if phoneNumber: OwnerToUpdate.phoneNumber = phoneNumber;

        OwnerToUpdate.save()
        return True
    except Exception as e:
        print("error: ", e)
        return False