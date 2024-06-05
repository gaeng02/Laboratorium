import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime

# import date_selector

class Prompt () :

    def __init__ (self, root) :
        
        self.text = []
        
        self.root = root
        self.root.title("README prompt")
        self.root.geometry("800x600")
        self.root.resizable(0, 0)

        # 
        self.grid_row = 0
        
        self.project_name_label = tk.Label(self.root, text = "Project Name")
        self.project_name_label.grid(row = self.grid_row, column = 0)

        self.project_name_entry = tk.Entry(self.root)
        self.project_name_entry.grid(row = self.grid_row, column = 1)

        # 
        self.grid_row += 1

        self.project_purpose_label = tk.Label(self.root, text = "Project Purpose")
        self.project_purpose_label.grid(row = self.grid_row, column = 0)

        self.project_purpose_text = tk.Text(self.root)
        self.project_purpose_text.grid(row = self.grid_row, column = 1)

        #
        self.grid_row += 1

        self.start_date_label = tk.Label(self.root, text = "Start Date")
        self.start_date_label.grid(row = self.grid_row, column = 0)

        self.start_date_label = tk.Label(self.root, text = "")
        self.start_date_label.grid(row = self.grid_row, column = 1)

        #
        self.grid_row += 1

        self.last_update_var = tk.IntVar()
        self.last_update_checkbox = tk.Checkbutton(self.root, text = "Last Update", variable = self.last_update_var)
        self.last_update_checkbox.grid(row = self.grid_row, column = 0)

        self.last_update_label = tk.Label(self.root, text = "")
        self.last_update_label.grid(row = self.grid_row, column = 1)

        #
        self.grid_row += 1

        self.contents_var = tk.IntVar()
        self.contents_checkbox = tk.Checkbutton(self.root, text = "Contents", variable = self.contents_var)
        self.contents_checkbox.grid(row = self.grid_row, column = 0)

        self.contents_label = tk.Label(self.root, text = "Auto Creating")
        self.contents_label.grid(row = self.grid_row, column = 1)

        # 
        self.grid_row += 1

        self.environment_var = tk.IntVar()
        self.environment_checkbox = tk.Checkbutton(self.root, text = "Develop Environment", variable = self.environment_var)
        self.environment_checkbox.grid(row = self.grid_row, column = 0)

        self.environment_frame = tk.Frame(self.root)
        self.environment_frame.grid(row = self.grid_row, column = 1)

        #
        self.grid_row += 1

        self.member_var = tk.IntVar()
        self.member_checkbox = tk.Checkbutton(self.root, text = "Member", variable = self.member_var)
        self.member_checkbox.grid(row = self.grid_row, column = 0)

        #self.member_label = tk.La
        

if __name__ == "__main__" :
    app = tk.Tk()
    prompt = Prompt(app)
    app.mainloop()
