import tkinter as tk

root = tk.Tk()
root.title("Login")

text_id = tk.Text(root, height = 2, width = 20)
text_id.pack()

text_pw = tk.Text(root, height = 2, width = 20)
text_pw.pack()

root.mainloop()
