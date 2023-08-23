def updateInfractionInteractor(infractionToUpdate, name, level, fine):
    try:
        if name: infractionToUpdate.name = name;
        if level: infractionToUpdate.level = level;
        if fine: infractionToUpdate.fine = fine;

        infractionToUpdate.save()
        return True
    except Exception as e:
        print("error: ", e)
        return False