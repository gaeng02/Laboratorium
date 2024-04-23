def instagram () :
    webbrowser.open("https://www.instagram.com/")

def github () :
    webbrowser.open("https://github.com/")

def baekjoon () :
    webbrowser.open("https://www.acmicpc.net/user/")
    
def login () :
    a = id_entry.get()
    b = pw_entry.get()
    if a == 'admin' and b == '1234' : print("Login!")
    else : print("Error")
