import tkinter as tk
import webbrowser 

import login
    
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

'''
button_instagram = tk.Button(root, command = instagram)
button_github = tk.Button(root, command = github)
button_baekjoon = tk.Button(root, command = baekjoon)

button_instagram.pack()
button_github.pack()
button_baekjoon.pack()
'''

root.mainloop()
