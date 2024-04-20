import tkinter as tk
import webbrowser 

def instagram () :
    webbrowser.open("https://www.instagram.com/gaeng._.02/")

def github () :
    webbrowser.open("https://github.com/gaeng02")

def baekjoon () :
    webbrowser.open("https://www.acmicpc.net/user/gaeng_02")
    

root = tk.Tk()
root.title("Login")
root.geometry("400x600")
root.resizable(0, 0)

text_id = tk.Text(root, height = 2, width = 20, font=("Arial", 20))
text_id.pack(pady=100, side = tk.TOP)

text_pw = tk.Text(root, height = 2, width = 20)
text_pw.pack()

button_login = tk.Button(root, text = "Login")
button_login.pack()

button_instagram = tk.Button(root, command = instagram)
button_github = tk.Button(root, command = github)
button_baekjoon = tk.Button(root, command = baekjoon)

button_instagram.pack()
button_github.pack()
button_baekjoon.pack()

root.mainloop()
