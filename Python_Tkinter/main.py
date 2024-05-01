import tkinter as tk
import webbrowser 

def login () :
    a = id_entry.get()
    b = pw_entry.get()
    if a == 'admin' and b == '1234' : print("Login!")
    else : print("Error")
    
root = tk.Tk()
root.title("Login")
root.geometry("400x600")
root.resizable(0, 0)

id_label = tk.Label(root, text = "User id")
id_label.pack() # pady=100, side = tk.TOP
id_entry = tk.Entry(root)
id_entry.pack()

pw_label = tk.Label(root, text = "Password")
pw_label.pack()
pw_entry = tk.Entry(root, show="*")
pw_entry.pack()

login_button = tk.Button(root, text = "Login", command = login)
login_button.pack()

root.mainloop()
