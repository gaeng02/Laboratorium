import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime

import date_selector
import create_markdown

class Prompt () :

    def __init__ (self, root) :

        window = root
        window.title("README prompt")
        window.geometry("600x600")
        window.resizable(0, 1)

        self.top_frame = ttk.Frame(window)
        self.top_frame.pack(side="top", fill="both", expand=True)

        self.bottom_frame = ttk.Frame(window)
        self.bottom_frame.pack(side="bottom", fill="x")

        self.main_canvas = tk.Canvas(self.top_frame)
        self.main_scrollbar = ttk.Scrollbar(self.top_frame, orient = "vertical", command = self.main_canvas.yview)

        root = ttk.Frame(self.main_canvas)
        root.bind("<Configure>", lambda e: self.main_canvas.configure(scrollregion=self.main_canvas.bbox("all")))
        
        self.main_canvas.create_window((0, 0), window = root, anchor="nw")
        self.main_canvas.configure(yscrollcommand = self.main_scrollbar.set)
        
        self.main_canvas.pack(side = "left", fill = "both", expand = True)
        self.main_scrollbar.pack(side = "right", fill = "y")
        
        self.main_canvas.bind_all("<MouseWheel>", self._on_mouse_wheel) # for Windows / Linux
        self.main_canvas.bind_all("<Button-4>", self._on_mouse_wheel) # for macOS 
        self.main_canvas.bind_all("<Button-5>", self._on_mouse_wheel)
        

        # Project Name
        grid_row = 0
        
        project_name_label = tk.Label(root, text = "Project Name")
        project_name_label.grid(row = grid_row, column = 0, sticky = "nw", padx = 10, pady = 5)

        self.project_name_entry = tk.Entry(root, width = 50)
        self.project_name_entry.grid(row = grid_row, column = 1, sticky = "w", ipady = 5, pady = 5)


        # Project Purpose
        grid_row += 1

        project_purpose_label = tk.Label(root, text = "Project Purpose")
        project_purpose_label.grid(row = grid_row, column = 0, sticky = "nw", padx = 10, pady = 5)

        self.project_purpose_text = tk.Text(root, width = 50, height = 10)
        self.project_purpose_text.grid(row = grid_row, column = 1, sticky = "w", ipady = 5, pady = 5)


        # Start Date (YY-MM-DD)
        grid_row += 1
        
        self.start_date_var = tk.IntVar()
        start_date_checkbox = tk.Checkbutton(root, text = "Start Date", variable = self.start_date_var)
        start_date_checkbox.grid(row = grid_row, column = 0, sticky = "nw", padx = 10, pady = 5)

        self.start_date = datetime.now().strftime("%Y - %m - %d")
        self.start_date_button = tk.Button(root, text = self.start_date, command = self.Get_start_date, width = 12, height = 1) 
        self.start_date_button.grid(row = grid_row, column = 1, sticky = "n", pady = 5) 


        # Last Update Date (YY-MM-DD)
        grid_row += 1

        self.last_update_var = tk.IntVar()
        last_update_checkbox = tk.Checkbutton(root, text = "Last Update", variable = self.last_update_var)
        last_update_checkbox.grid(row = grid_row, column = 0, sticky = "nw", padx = 10, pady = 5)

        self.last_update_date = datetime.now().strftime("%Y - %m - %d")
        self.last_update_button = tk.Button(root, text = self.last_update_date, command = self.Get_last_update_date, width = 12, height = 1) 
        self.last_update_button.grid(row = grid_row, column = 1, sticky = "n", pady = 5)


        # Contents 
        grid_row += 1

        self.contents_var = tk.IntVar()
        contents_checkbox = tk.Checkbutton(root, text = "Contents", variable = self.contents_var)
        contents_checkbox.grid(row = grid_row, column = 0, sticky = "nw", padx = 10, pady = 5)

        self.contents_label = tk.Label(root, text = "Auto Creating")
        self.contents_label.grid(row = grid_row, column = 1)


        # Environment 
        grid_row += 1

        self.environment_var = tk.IntVar()
        environment_checkbox = tk.Checkbutton(root, text = "Develop Environment", variable = self.environment_var)
        environment_checkbox.grid(row = grid_row, column = 0, sticky = "nw", padx = 10, pady = 5)

        self.environment_frame = tk.Frame(root)
        self.environment_frame.grid(row = grid_row, column = 1, sticky = "n", pady = 5)


        # Member
        grid_row += 1

        self.member_var = tk.IntVar()
        member_checkbox = tk.Checkbutton(root, text = "Member", variable = self.member_var)
        member_checkbox.grid(row = grid_row, column = 0, sticky = "nw", padx = 10, pady = 5)

        self.member_frame = tk.Frame(root)
        self.member_frame.grid(row = grid_row, column = 1, sticky = "n", pady = 5)

        member_name_label = tk.Label(self.member_frame, text = "User Name")
        member_name_label.grid(row = 0, column = 0, padx = 5, pady = 1)
        member_url_label = tk.Label(self.member_frame, text = "Github URL")
        member_url_label.grid(row = 0, column = 1, padx = 5, pady = 1)
        member_add_button = tk.Button(self.member_frame, text = "+", command = self.Add_member, width = 2, height = 1)
        member_add_button.grid(row = 0, column = 2, padx = 5, pady = 1)

        self.member_num = 1
        self.member_default_name_entry = tk.Entry(self.member_frame)
        self.member_default_name_entry.grid(row = self.member_num, column = 0, padx = 5, pady = 1)
        self.member_default_url_entry = tk.Entry(self.member_frame)
        self.member_default_url_entry.grid(row = self.member_num, column = 1, padx = 5, pady = 1)


        # Library
        grid_row += 1
        self.library_var = tk.IntVar()
        library_checkbox = tk.Checkbutton(root, text = "Library", variable = self.library_var)
        library_checkbox.grid(row = grid_row, column = 0, sticky = "nw", padx = 10, pady = 5)

        self.library_frame = tk.Frame(root)
        self.library_frame.grid(row = grid_row, column = 1, sticky = "n", pady = 5)

        library_name_label = tk.Label(self.library_frame, text = "Library Name")
        library_name_label.grid(row = 0, column = 0, padx = 5, pady = 1)
        library_license_label = tk.Label(self.library_frame, text = "License")
        library_license_label.grid(row = 0, column = 1, padx = 5, pady = 1)
        library_add_button = tk.Button(self.library_frame, text = "+", command = self.Add_library, width = 2, height = 1)
        library_add_button.grid(row = 0, column = 2, padx = 5, pady = 1)

        self.library_num = 1
        self.library_default_name_entry = tk.Entry(self.library_frame)
        self.library_default_name_entry.grid(row = self.library_num, column = 0, padx = 5, pady = 1)
        self.library_default_license_entry = tk.Entry(self.library_frame)
        self.library_default_license_entry.grid(row = self.library_num, column = 1, padx = 5, pady = 1)


        # Function 
        grid_row += 1
        self.instruction_var = tk.IntVar()
        instruction_checkbox = tk.Checkbutton(root, text = "Instruction", variable = self.instruction_var)
        instruction_checkbox.grid(row = grid_row, column = 0, sticky = "nw", padx = 10, pady = 5)

        self.instruction_frame = tk.Frame(root)
        self.instruction_frame.grid(row = grid_row, column = 1, sticky = "n", pady = 5)

        instruction_name_label = tk.Label(self.instruction_frame, text = "Instruction")
        instruction_name_label.grid(row = 0, column = 0, padx = 5, pady = 1)
        instruction_explanation_label = tk.Label(self.instruction_frame, text = "Explanation")
        instruction_explanation_label.grid(row = 0, column = 1, padx = 5, pady = 1)
        instruction_add_button = tk.Button(self.instruction_frame, text = "+", command = self.Add_instruction, width = 2, height = 1)
        instruction_add_button.grid(row = 0, column = 2, padx = 5, pady = 1)

        self.instruction_num = 1
        self.instruction_default_name_entry = tk.Entry(self.instruction_frame)
        self.instruction_default_name_entry.grid(row = self.instruction_num, column = 0, padx = 5, pady = 1)
        self.instruction_default_explanation_entry = tk.Entry(self.instruction_frame)
        self.instruction_default_explanation_entry.grid(row = self.instruction_num, column = 1, padx = 5, pady = 1)


        # Bottom Frame
        create_button = tk.Button(self.bottom_frame, text = "Create", command = self.Create, width = 20, height = 2)
        create_button.pack(pady = 10)

    def _on_mouse_wheel (self, event) :
        if (event.num == 4) : self.main_canvas.yview_scroll(-1, "units")
        elif (event.num) == 5 : self.main_canvas.yview_scroll(1, "units")
        else : self.main_canvas.yview_scroll(int(-1*(event.delta/120)), "units")
            
    def Get_start_date (self) :
        self.start_date = date_selector.update_date()
        self.start_date_button.config(text = self.start_date)

    def Get_last_update_date (self) :
        self.last_update_date = date_selector.update_date()
        self.last_update_button.config(text = self.last_update_date)

        
    def Add_member (self) :
        self.member_num += 1
        
        new_name_entry = tk.Entry(self.member_frame)
        new_name_entry.grid(row = self.member_num, column = 0, padx = 5, pady = 1)
        
        new_url_entry = tk.Entry(self.member_frame)
        new_url_entry.grid(row = self.member_num, column = 1, padx = 5, pady = 1)

        delete_button = tk.Button(self.member_frame, text = "-", command = lambda r = self.member_num : self.Delete_member(r), width = 2, height = 1)
        delete_button.grid(row = self.member_num, column = 2, padx = 5, pady = 1)


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

        new_name_entry = tk.Entry(self.library_frame)
        new_name_entry.grid(row = self.library_num, column = 0, padx = 5, pady = 1)
        
        new_license_entry = tk.Entry(self.library_frame)
        new_license_entry.grid(row = self.library_num, column = 1, padx = 5, pady = 1)

        delete_button = tk.Button(self.library_frame, text = "-", command = lambda r = self.library_num : self.Delete_library(r), width = 2, height = 1)
        delete_button.grid(row = self.library_num, column = 2, padx = 5, pady = 1)


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
        
        new_name_entry = tk.Entry(self.instruction_frame)
        new_name_entry.grid(row = self.instruction_num, column = 0, padx = 5, pady = 1)
        
        new_explanation_entry = tk.Entry(self.instruction_frame)
        new_explanation_entry.grid(row = self.instruction_num, column = 1, padx = 5, pady = 1)

        delete_button = tk.Button(self.instruction_frame, text = "-", command = lambda r = self.instruction_num : self.Delete_instruction(r), width = 2, height = 1)
        delete_button.grid(row = self.instruction_num, column = 2, padx = 5, pady = 1)
        

    def Delete_instruction (self, row) :
        self.instruction_num -= 1

        for widget in self.instruction_frame.grid_slaves(row = row) :
            widget.grid_forget()

        for r in range (row + 1, self.instruction_num) :
            for widget in self.instruction_frame.grid_slaves(row = r) :
                widget.grid(row = r-1, column = widget.grid_info()["column"])
                if isinstance(widget, tk.Button) and widget.cget("text") == "-":
                    widget.config(command = lambda r = r-1 : self.Delete_instruction(r))

    def Create (self) :
        text = []
        text.append(self.project_name_entry.get())
        text.append(self.project_purpose_text.get("1.0", "end"))

        text.append(self.start_date_button.cget("text") if self.start_date_var.get() else False)
        text.append(self.last_update_button.cget("text") if self.last_update_var.get() else False)
        text.append(True if self.contents_var.get() else False)

        '''
        self.environment_var.get() 
        self.member_var.get()
        self.library_var.get()
        self.instruction_var.get()
        '''
        print(text)
        create_markdown.Readme(text)
        print("Success")


if (__name__ == "__main__") :
    app = tk.Tk()
    prompt = Prompt(app)
    app.mainloop()
