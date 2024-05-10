import tkinter as tk
from tkinter import messagebox

import valid 

def login () :
    
    def verification () : 
        try_username = id_entry.get()
        try_password = pw_entry.get()
        if (try_username == "admin") and (try_password == "1234") : print("Login!")
        else : tk.messagebox.showinfo("Login", "Check your ID and Password!")


    root = tk.Tk()
    root.title("Login")
    root.geometry("300x140")
    root.resizable(0, 0)

    bg_color = "SkyBlue1"
    fg_color = "Black"
    font = 14 
    
    root.configure(bg = bg_color)
    
    id_label = tk.Label(root, text = "Username :: ", bg = bg_color, fg = fg_color, font = font)
    id_label.grid(row = 0, column = 0, padx = 10, pady = 10)

    id_entry = tk.Entry(root)
    id_entry.grid(row = 0, column = 1, padx = 10, pady = 10, columnspan = 2)

    pw_label = tk.Label(root, text = "Password :: ", bg = bg_color, fg = fg_color, font = font)
    pw_label.grid(row = 1, column = 0, padx = 10, pady = 10)
    
    pw_entry = tk.Entry(root, show="*")
    pw_entry.grid(row = 1, column = 1, padx = 10, pady = 10, columnspan = 2)
    
    login_button = tk.Button(root, text = "Login", command = verification)
    login_button.grid(row = 2, column = 1, padx = 10, pady = 10)

    join_button = tk.Button(root, text = "Create", command = create)
    join_button.grid(row = 2, column = 2, padx = 10, pady = 10)
    
    root.mainloop()

def create () :

    def create_account () :
        try_username = id_entry.get()
        try_password = pw_entry.get()
        check_password = pw_again_entry.get()

        Success = "Create Successfully"
        Failed = "Create Failed"

        if (try_password != check_password) :
            tk.messagebox.showinfo(Failed, "Password and Again are not same.")
            return ;

        username = valid.check_username(try_username)
        password = valid.check_password(try_password)
        if (username) : tk.messagebox.showinfo(Failed, username); return ;
        if (password) : tk.messagebox.showinfo(Failed, password); return ;

        tk.messagebox.showinfo(Success, "Create Successfully!"); 
        return new.destroy()
        
    new = tk.Tk()
    new.title("Create new Account")
    new.geometry("300x180")
    new.resizable(0, 0)

    bg_color = "SkyBlue1"
    fg_color = "Black"
    font = 14 
    
    new.configure(bg = bg_color)
    
    id_label = tk.Label(new, text = "Username :: ", bg = bg_color, fg = fg_color, font = font)
    id_label.grid(row = 0, column = 0, padx = 10, pady = 10)

    id_entry = tk.Entry(new)
    id_entry.grid(row = 0, column = 1, padx = 10, pady = 10)

    pw_label = tk.Label(new, text = "Password :: ", bg = bg_color, fg = fg_color, font = font)
    pw_label.grid(row = 1, column = 0, padx = 10, pady = 10)
    
    pw_entry = tk.Entry(new, show="*")
    pw_entry.grid(row = 1, column = 1, padx = 10, pady = 10)
    
    blank_label = tk.Label(new, text = "Enter again ", bg = bg_color, fg = fg_color, font = font)
    blank_label.grid(row = 2, column = 0, padx = 10, pady = 10)
    
    pw_again_entry = tk.Entry(new, show="*")
    pw_again_entry.grid(row = 2, column = 1, padx = 10, pady = 10)

    create_button = tk.Button(new, text = "Create", command = create_account)
    create_button.grid(row = 3, column = 1, padx = 10, pady = 10)
    
    new.mainloop()

login()
