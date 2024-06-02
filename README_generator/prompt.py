import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime

import date_selector


class Readme () :

    def __init__ (self, root) :
        self.n = root

    def Create (self) :
        
        with open("README.md", "w") as file : 
            file.writelines(self.text)

    def Reset (self) :

        with open ("README.md", "w") as file :
            file.write()


class Prompt (Readme) :

    def __init__ (self, root) :
        
        self.text = []
        
        self.root = root
        self.root.title("README prompt")
        self.root.geometry("800x600")
        self.root.resizable(0, 0)

#class Object (PROMPT) :



class Drag_Label (tk.Label) :
    def __init__ (self, master, **kwargs) :
        super().__init__(master, **kwargs)
        self.bind("<Button-1>", self.on_click)
        self.bind("<B1-Motion>", self.on_drag)

    def on_click (self, event) :
        self._drag_start_x = event.x
        self._drag_start_y = event.y

    def on_drag (self, event) :
        x = self.winfo_x() + event.x - self._drag_start_x
        y = self.winfo_y() + event.y - self._drag_start_y
        self.place(x = x, y = y)

app = tk.Tk()
app.geometry("800x600")

label = Drag_Label(app, width = 10, bg = "black")
label.place(x=100, y=100)

app.mainloop()
    
