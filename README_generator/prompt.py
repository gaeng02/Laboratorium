import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime

# import date_selector

class Prompt () :

    def __init__ (self, root) :
        
        self.text = []
        
        self.window = root
        self.window.title("README prompt")
        self.window.geometry("800x600")
        self.window.resizable(0, 0)

        self.main_canvas = tk.Canvas(self.window)
        self.main_canvas.pack(side = "left", fill = "both", expand = True)

        self.main_scrollbar = ttk.Scrollbar(self.window, orient = "vertical", command = self.main_canvas.yview)
        self.main_scrollbar.pack(side = "right", fill = "y")

        self.main_canvas.configure(yscrollcommand = self.main_scrollbar.set)
        self.main_canvas.bind('<Configure>', lambda e: self.main_canvas.configure(scrollregion=self.main_canvas.bbox("all")))

        self.root = ttk.Frame(self.main_canvas)
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
        self.member_checkbox.grid(row = self.grid_row, column = 0, sticky = "n")

        self.member_frame = tk.Frame(self.root)
        self.member_frame.grid(row = self.grid_row, column = 1)

        self.name_label = tk.Label(self.member_frame, text = "User Name")
        self.name_label.grid(row = 0, column = 1)
        self.url_label = tk.Label(self.member_frame, text = "Github URL")
        self.url_label.grid(row = 0, column = 2)
        self.add_button = tk.Button(self.member_frame, text = "+", command = self.Add_member)
        self.add_button.grid(row = 0, column = 3)

        self.member_num = 1
        self.default_name_entry = tk.Entry(self.member_frame)
        self.default_name_entry.grid(row = self.member_num, column = 1)
        self.default_url_entry = tk.Entry(self.member_frame)
        self.default_url_entry.grid(row = self.member_num, column = 2)


        #
        self.grid_row += 1


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

if (__name__ == "__main__") :
    app = tk.Tk()
    prompt = Prompt(app)
    app.mainloop()
