import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime

import date_selector

class Prompt () :

    def __init__ (self, root) :
        
        self.text = []
        
        self.window = root
        self.window.title("README prompt")
        self.window.geometry("800x600")
        self.window.resizable(0, 1)

        self.main_canvas = tk.Canvas(self.window)
        self.main_canvas.pack(side = "left", fill = "both", expand = True)

        self.main_scrollbar = ttk.Scrollbar(self.window, orient = "vertical", command = self.main_canvas.yview)
        self.main_scrollbar.pack(side = "right", fill = "y")

        self.main_canvas.configure(yscrollcommand = self.main_scrollbar.set)
        self.main_canvas.bind('<Configure>', lambda e: self.main_canvas.configure(scrollregion=self.main_canvas.bbox("all")))

        self.root = ttk.Frame(self.main_canvas)
        self.root.bind("<Configure>", lambda e: self.main_canvas.configure(scrollregion=self.main_canvas.bbox("all")))
        
        self.main_canvas.create_window((0, 0), window=self.root, anchor="nw")


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
        
        self.start_date_var = tk.IntVar()
        self.start_date_checkbox = tk.Checkbutton(self.root, text = "Start Date", variable = self.start_date_var)
        self.start_date_checkbox.grid(row = self.grid_row, column = 0)

        self.start_date = datetime.now().strftime("%Y - %m - %d")
        self.start_date_button = tk.Button(self.root, text = self.start_date, command = self.Get_start_date) 
        self.start_date_button.grid(row = self.grid_row, column = 1) 


        #
        self.grid_row += 1

        self.last_update_var = tk.IntVar()
        self.last_update_checkbox = tk.Checkbutton(self.root, text = "Last Update", variable = self.last_update_var)
        self.last_update_checkbox.grid(row = self.grid_row, column = 0)

        self.last_update_date = datetime.now().strftime("%Y - %m - %d")
        self.last_update_button = tk.Button(self.root, text = self.last_update_date, command = self.Get_last_update_date) 
        self.last_update_button.grid(row = self.grid_row, column = 1)

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
        self.member_checkbox.grid(row = self.grid_row, column = 0, sticky = "n")

        self.member_frame = tk.Frame(self.root)
        self.member_frame.grid(row = self.grid_row, column = 1)

        self.member_name_label = tk.Label(self.member_frame, text = "User Name")
        self.member_name_label.grid(row = 0, column = 1)
        self.member_url_label = tk.Label(self.member_frame, text = "Github URL")
        self.member_url_label.grid(row = 0, column = 2)
        self.member_add_button = tk.Button(self.member_frame, text = "+", command = self.Add_member)
        self.member_add_button.grid(row = 0, column = 3)

        self.member_num = 1
        self.member_default_name_entry = tk.Entry(self.member_frame)
        self.member_default_name_entry.grid(row = self.member_num, column = 1)
        self.member_default_url_entry = tk.Entry(self.member_frame)
        self.member_default_url_entry.grid(row = self.member_num, column = 2)


        #
        self.grid_row += 1
        self.library_var = tk.IntVar()
        self.library_checkbox = tk.Checkbutton(self.root, text = "Library", variable = self.library_var)
        self.library_checkbox.grid(row = self.grid_row, column = 0, sticky = "n")

        self.library_frame = tk.Frame(self.root)
        self.library_frame.grid(row = self.grid_row, column = 1)

        self.library_name_label = tk.Label(self.library_frame, text = "Library Name")
        self.library_name_label.grid(row = 0, column = 1)
        self.library_license_label = tk.Label(self.library_frame, text = "License")
        self.library_license_label.grid(row = 0, column = 2)
        self.library_add_button = tk.Button(self.library_frame, text = "+", command = self.Add_library)
        self.library_add_button.grid(row = 0, column = 3)

        self.library_num = 1
        self.library_default_name_entry = tk.Entry(self.library_frame)
        self.library_default_name_entry.grid(row = self.library_num, column = 1)
        self.library_default_license_entry = tk.Entry(self.library_frame)
        self.library_default_license_entry.grid(row = self.library_num, column = 2)

        #
        self.grid_row += 1
        self.instruction_var = tk.IntVar()
        self.instruction_checkbox = tk.Checkbutton(self.root, text = "Instruction", variable = self.instruction_var)
        self.instruction_checkbox.grid(row = self.grid_row, column = 0, sticky = "n")

        self.instruction_frame = tk.Frame(self.root)
        self.instruction_frame.grid(row = self.grid_row, column = 1)

        self.instruction_name_label = tk.Label(self.instruction_frame, text = "Instruction")
        self.instruction_name_label.grid(row = 0, column = 1)
        self.instruction_explanation_label = tk.Label(self.instruction_frame, text = "Explanation")
        self.instruction_explanation_label.grid(row = 0, column = 2)
        self.instruction_add_button = tk.Button(self.instruction_frame, text = "+", command = self.Add_instruction)
        self.instruction_add_button.grid(row = 0, column = 3)

        self.instruction_num = 1
        self.instruction_default_name_entry = tk.Entry(self.instruction_frame)
        self.instruction_default_name_entry.grid(row = self.instruction_num, column = 1)
        self.instruction_default_explanation_entry = tk.Entry(self.instruction_frame)
        self.instruction_default_explanation_entry.grid(row = self.instruction_num, column = 2)


    '''
        self.fixed_frame = ttk.Frame(self.window)
        self.fixed_frame.pack(side="bottom", fill="y")

        self.fixed_label = ttk.Label(self.fixed_frame, text = "Fixed")
        self.fixed_label.pack()

    '''
    
    def Get_start_date (self) :
        self.start_date = date_selector.update_date()
        self.start_date_button.config(text = self.start_date)

    def Get_last_update_date (self) :
        self.last_update_date = date_selector.update_date()
        self.last_update_button.config(text = self.last_update_date)

        
    def Add_member (self) :
        self.member_num += 1
        
        delete_button = tk.Button(self.member_frame, text = "-", command = lambda r = self.member_num : self.Delete_member(r))
        delete_button.grid(row = self.member_num, column = 0)
        
        new_name_entry = tk.Entry(self.member_frame)
        new_name_entry.grid(row = self.member_num, column = 1)
        
        new_url_entry = tk.Entry(self.member_frame)
        new_url_entry.grid(row = self.member_num, column = 2)


    def Delete_member (self, row) :
        self.member_num -= 1

        for widget in self.member_frame.grid_slaves(row = row) :
            widget.grid_forget()

        for r in range (row + 1, self.member_num) :
            for widget in self.member_frame.grid_slaves(row = r) :
                widget.grid(row = r-1, column = widget.grid_info()["column"])
                if isinstance(widget, tk.Button) and widget.cget("text") == "-":
                    widget.config(command = lambda r = r-1 : self.Delete_member(r))


    def Add_library (self) :
        self.library_num += 1
        
        delete_button = tk.Button(self.library_frame, text = "-", command = lambda r = self.library_num : self.Delete_library(r))
        delete_button.grid(row = self.library_num, column = 0)
        
        new_name_entry = tk.Entry(self.library_frame)
        new_name_entry.grid(row = self.library_num, column = 1)
        
        new_license_entry = tk.Entry(self.library_frame)
        new_license_entry.grid(row = self.library_num, column = 2)


    def Delete_library (self, row) :
        self.library_num -= 1

        for widget in self.library_frame.grid_slaves(row = row) :
            widget.grid_forget()

        for r in range (row + 1, self.member_num) :
            for widget in self.library_frame.grid_slaves(row = r) :
                widget.grid(row = r-1, column = widget.grid_info()["column"])
                if isinstance(widget, tk.Button) and widget.cget("text") == "-":
                    widget.config(command = lambda r = r-1 : self.Delete_library(r))
                    

    def Add_instruction (self) :
        self.instruction_num += 1
        
        delete_button = tk.Button(self.instruction_frame, text = "-", command = lambda r = self.instruction_num : self.Delete_instruction(r))
        delete_button.grid(row = self.instruction_num, column = 0)
        
        new_name_entry = tk.Entry(self.instruction_frame)
        new_name_entry.grid(row = self.instruction_num, column = 1)
        
        new_explanation_entry = tk.Entry(self.instruction_frame)
        new_explanation_entry.grid(row = self.instruction_num, column = 2)


    def Delete_instruction (self, row) :
        self.instruction_num -= 1

        for widget in self.instruction_frame.grid_slaves(row = row) :
            widget.grid_forget()

        for r in range (row + 1, self.instruction_num) :
            for widget in self.instruction_frame.grid_slaves(row = r) :
                widget.grid(row = r-1, column = widget.grid_info()["column"])
                if isinstance(widget, tk.Button) and widget.cget("text") == "-":
                    widget.config(command = lambda r = r-1 : self.Delete_instruction(r))
                    

if (__name__ == "__main__") :
    app = tk.Tk()
    prompt = Prompt(app)
    app.mainloop()
