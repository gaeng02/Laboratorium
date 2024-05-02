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

bg_color = "RoyalBlue1"
fg_color = "Black"
font = 14 

root.configure(bg = bg_color)

root.grid_rowconfigure(3, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)

id_label = tk.Label(root, text = "User id", bg = bg_color, fg = fg_color, font = font)
id_label.grid(row = 0, column = 0, sticky="nsew")


id_entry = tk.Entry(root)
id_entry.pack(expand = True)

pw_label = tk.Label(root, text = "Password", bg = bg_color, fg = fg_color, font = font)
pw_label.pack()
pw_entry = tk.Entry(root, show="*")
pw_entry.pack()

login_button = tk.Button(root, text = "Login", command = login)
login_button.pack()


root.mainloop()
