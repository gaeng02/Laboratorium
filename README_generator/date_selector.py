import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import calendar
from datetime import datetime, timedelta


class Calender () :

    def __init__ (self, root) :
        
        self.current = datetime.now()
        self.year = self.current.year
        self.month_list = ["", "January", "February", "March", "April", "May", "June", "July",
                           "August", "September", "October", "November", "December"]
        self.month = self.current.month

        self.selected_date = "None"
        
        self.root = root
        self.root.title("Calender")
        self.root.geometry("600x250")
        self.root.resizable(0, 0)
        

        # Header
        self.header_frame = ttk.Frame(root)
        self.header_frame.pack(pady=5)

        self.previous_button = ttk.Button(self.header_frame, text = "◀", width = 4, command = self.previous_month)
        self.previous_button.pack(padx = 20, side = "left")

        self.year_label = ttk.Label(self.header_frame, text = self.year, width = 4, anchor = "center")
        self.year_label.pack(side = "left")
        
        self.month_label = ttk.Label(self.header_frame, text = self.month_list[self.month], width = 10, anchor = "center")
        self.month_label.pack(side = "left")
        
        self.next_button = ttk.Button(self.header_frame, text = "▶", width = 4, command = self.next_month)
        self.next_button.pack(padx = 20, side = "left")

        # Calendar          
        self.calendar_frame = ttk.Frame(root)
        self.calendar_frame.pack(pady=5)

        self.create()
        self.update()

        # Selection 
        self.selection_frame = ttk.Frame(root)
        self.selection_frame.pack()

        self.selection_label = ttk.Label(self.selection_frame, text = "Not Selected", width = 25, anchor = "center")
        self.selection_label.pack(side = "left")

        self.selection_button = ttk.Button(self.selection_frame, text = "Select", width = 8, command = self.confirm_date)
        self.selection_button.pack(padx = 5, side = "left")


    def create (self) :

        self.days_buttons = []
        day_of_week = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]

        for i in range (7) :
            # Day of week == 7
            day_label = ttk.Label(self.calendar_frame, text = day_of_week[i], width = 10, anchor = "center")
            day_label.grid(row = 0, column = i)

        for row in range (1, 7) :
            # Max of row on the Calendar == 6
            
            row_buttons = []
            
            for col in range (7) :
                # Day of week == 7
                button = ttk.Button(self.calendar_frame, text = "", width = 10, command = lambda r = row-1, c = col : self.select_date(r, c))
                button.grid(row = row, column = col)
                row_buttons.append(button)
            self.days_buttons.append(row_buttons)
        

    def update (self) :
        for row_buttons in self.days_buttons :
            for button in row_buttons :
                button.config(text="", state = "disabled")

        self.year_label.config(text = self.year)
        self.month_label.config(text = self.month_list[self.month])

        first_day, num_days = calendar.monthrange(self.year, self.month)
        first_day = (first_day + 1) % 7 # Set start_day as "Sun" (default = "Mon")
        
        current_day = 1
        
        for week in range (6) :
            for day in range (7) :
                if (week == 0 and day < first_day) or (current_day > num_days) : continue

                self.days_buttons[week][day].config(text = str(current_day), state = "normal")
                current_day += 1  


    def previous_month (self) :
        self.current = self.current.replace(day=1) - timedelta(days = 1)
        self.year = self.current.year
        self.month = self.current.month
        self.update()

        
    def next_month (self) :
        num_days = calendar.monthrange(self.current.year, self.current.month)[1]
        self.current = self.current.replace(day=1) + timedelta(days = num_days)
        self.year = self.current.year
        self.month = self.current.month
        self.update()

        
    def select_date (self, row, col) :
        self.day = self.days_buttons[row][col].cget("text")
        self.selection_label.config(text = f"Selected Date : {self.year}-{str(self.month).zfill(2)}-{str(self.day).zfill(2)}")


    def confirm_date (self) :
        if (self.select_date) :
            if (self.ask()) :
                print(f"Selected Date : {self.year}-{str(self.month).zfill(2)}-{str(self.day).zfill(2)}")
                self.root.quit()
                self.root.destroy()


    def ask (self) :
        return messagebox.askyesno("Confirm", f"Selected Date : \n{self.year}-{str(self.month).zfill(2)}-{str(self.day).zfill(2)}")
        
        
'''        
if (__name__ == "__main__") :
    root = tk.Tk()
    app = Calender(root)
    root.mainloop()
'''
