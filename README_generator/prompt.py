import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime

import date_selector


class README () :

    def __init__ (self, root) :

        self.text = []
        
        self.root = root
        self.root.title("README prompt")
        self.root.geometry("800x600")
        self.root.resizable(0, 0)


    def Create (self) :
        
        with open("README.md", "w") as file : 
            file.writelines(self.text)
