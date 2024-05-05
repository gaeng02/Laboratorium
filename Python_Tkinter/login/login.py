import tkinter as tk
from tkinter import messagebox

def login () :
    
    def verification () : 
        login_id = id_entry.get()
        login_pw = pw_entry.get()
        if (login_id == "admin") and (login_pw == "admin") : print("Login!")
        else : login_wrong()

    #def join () :

    def login_wrong () :
        tk.messagebox.showinfo("Login", "Login Failed!")
            
    root = tk.Tk()
    root.title("Login")
    root.geometry("300x150")
    root.resizable(0, 0)

    bg_color = "RoyalBlue1"
    fg_color = "Black"
    font = 14 
    
    root.configure(bg = bg_color)
    
    id_label = tk.Label(root, text = "User id", bg = bg_color, fg = fg_color, font = font)
    id_label.pack()

    id_entry = tk.Entry(root)
    id_entry.pack()

    pw_label = tk.Label(root, text = "Password", bg = bg_color, fg = fg_color, font = font)
    pw_label.pack()
    
    pw_entry = tk.Entry(root, show="*")
    pw_entry.pack()

    blank_label = tk.Label(root, bg = bg_color)
    blank_label.pack()

    login_button = tk.Button(root, text = "Login", command = verification)
    login_button.pack()

    root.mainloop()


login()
