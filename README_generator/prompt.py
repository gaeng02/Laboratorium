import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime

# import date_selector

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


class Prompt () :

    def __init__ (self, root) :
        
        self.text = []
        
        self.root = root
        self.root.title("README prompt")
        self.root.geometry("800x600")
        self.root.resizable(0, 0)

        self.block_frame = tk.Frame(self.root, width = 300, height = 600, bg = "light grey")
        self.block_frame.grid(row = 0, column = 0)
        
        self.label = Drag_Label(self.block_frame, width = 10, bg = "black")
        self.label.pack()

        self.draw_frame = tk.Frame(self.root, width = 500, height = 600, background = "white")
        self.draw_frame.grid(row = 0, column = 1)
        

        #self.root.mainloop()
        

#class Object (PROMPT) :

if __name__ == "__main__" :
    app = tk.Tk()
    prompt = Prompt(app)
    app.mainloop()
    
