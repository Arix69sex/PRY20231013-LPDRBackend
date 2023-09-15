def updateUserDataInteractor(userDataToUpdate, identification, names, lastNames, address, phoneNumber):
    try:
        if identification: userDataToUpdate.identification = identification;
        if names: userDataToUpdate.names = names;
        if lastNames: userDataToUpdate.lastNames = lastNames;
        if address: userDataToUpdate.address = address;
        if phoneNumber: userDataToUpdate.phoneNumber = phoneNumber;

        userDataToUpdate.save()
        return True
    except Exception as e:
        print("error: ", e)
        return False