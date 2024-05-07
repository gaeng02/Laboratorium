def check_username (try_username) :
    n = len(try_username)
    check = [a-z, A-Z, _]+
    for i in range (n) :
        if (try_username[n] not in check) : return False
    return True
'''
def check_password (try_password) : 
    n = len(try_password)

    b = True
    for i in range (n) :
        
'''
