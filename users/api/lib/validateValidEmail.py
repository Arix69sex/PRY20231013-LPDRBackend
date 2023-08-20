import re

def isValidEmail(email):
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    print("re.match(email_pattern, email)", re.match(email_pattern, email))
    if re.match(email_pattern, email):
        return True
    else:
        return False
