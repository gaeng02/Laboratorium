import re

def check_username (try_username) :
    n = len(try_username)
    check = re.compile('[a-zA-Z_0-9]*')
    
    result = check.match(try_username)
    return "Username is not valid."
        
    return True

def check_password (try_password) : 
    n = len(try_password)

    if not (include_alphabet(try_password, n)) :
        return "Password must contain alphabet"
