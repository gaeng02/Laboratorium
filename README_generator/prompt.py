import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime

import date_selector


class Readme () :

    def __init__ (self, root) :


    def Create (self) :
        
        with open("README.md", "w") as file : 
            file.writelines(self.text)

    def Reset (self) :

        with open ("README.md", "w") as file :
            file.write()


class Prompt (README) :

    def __init__ (self, root) :
        
        self.text = []
        
        self.root = root
        self.root.title("README prompt")
        self.root.geometry("800x600")
        self.root.resizable(0, 0)

class Object (PROMPT) :



class Drag_Label (tk.Label) :
    def __init__ (self, master) :

    def on_click (self) :

    def on_drag (self):
    
