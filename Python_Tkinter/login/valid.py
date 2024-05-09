import re

def check_username (try_username) :
    n = len(try_username)
    check = re.compile(r'^[a-zA-Z_0-9]+$')
    
    if (check.match(try_username)) : return False
    
    return "Username is not valid."
        
    
def check_password (try_password) : 

    if not (has_uppercase (try_password)) :
        return "Password must contain upper case."

    if not (has_lowercase (try_password)) :
        return "Password must contain lower case."

    if not (has_digit (try_password)) :
        return "Password must contain digit number."

    if not (has_special (try_password)) :
        return "Password must contain special character."

    return False

def has_uppercase (password) :
    return re.search(r'[A-Z]', password)

def has_lowercase (password) :
    return re.search(r'[a-z]', password)

def has_digit (password) :
    return re.search(r'[0-9]', password)

def has_special (password) :
    return re.search(r'[~!@#$%^&*/?]', password)
