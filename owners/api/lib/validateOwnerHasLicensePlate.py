from owners.api.interactors.getOwnerByLicensePlateInteractor import getOwnerByLicensePlateInteractor


def validateOwnerHasLicensePlate(licensePlate):
    hasOwner = getOwnerByLicensePlateInteractor(licensePlate)
    if hasOwner.exists():
        raise Exception("License plate already has owner")