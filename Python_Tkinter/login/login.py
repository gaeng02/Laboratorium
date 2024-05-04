import tkinter as tk
import webbrowser 

def login () :
    
    def verification () : 
        a = id_entry.get()
        b = pw_entry.get()
        if a == 'admin' and b == '1234' : print("Login!")
        else : print("Error")
        
    root = tk.Tk()
    root.title("Login")
    root.geometry("400x600")
    root.resizable(0, 0)

    bg_color = "RoyalBlue1"
    fg_color = "Black"
    font = 14 
    
    root.configure(bg = bg_color)
    blank_1 = tk.Label(root, bg=bg_color)
    blank_1.grid(row = 1, column = 1) 
    
    id_label = tk.Label(root, text = "User id", bg = bg_color, fg = fg_color, font = font)
    id_label.grid(row = 1, column = 2)

    id_entry = tk.Entry(root)
    id_entry.grid(row = 2, column = 2)

    pw_label = tk.Label(root, text = "Password", bg = bg_color, fg = fg_color, font = font)
    pw_label.grid(row = 3, column = 2)
    
    pw_entry = tk.Entry(root, show="*")
    pw_entry.grid(row = 4, column = 2)

    login_button = tk.Button(root, text = "Login", command = verification)
    login_button.grid(row = 5, column = 2)

    root.mainloop()

login()
