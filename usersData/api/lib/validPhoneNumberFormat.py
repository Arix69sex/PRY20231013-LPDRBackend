import re

def validPhoneNumberFormat(phoneNumber):
    pattern = r'^\+\d+$'
    print("phoneNumber", phoneNumber)
    return re.match(pattern, phoneNumber)