import tkinter as tk

def check (month, year) :
    if (month < 1) :
        month = 12
        year -= 1
    elif (month > 12) :
        month %= 12
        year += 1
    return month, year

class calender (month = 12, year = 2024) :

    def left () :
        month, year = check(month, year)
        calender(month - 1, year)
        
    def right () :
        month, year = check(month, year) 
        calender(month + 1, year)
        
    m, y = int(month), int(year)
    
    root = tk.Tk()
    root.title("Calender")
    root.geometry("300x140")
    root.resizable(0, 0)

    left_button = tk.Button(root, text = "◀", command = left)
    right_button = tk.Button(root, text = "▶", command = right)

    left_button.grid(row = 0, column = 0)
    right_button.grid(row = 0, column = 6)

    year_label = tk.Label(root, text = year)
    month_label = tk.Label(root, text = month)

    year_label.grid(row = 0, column = 1, columnspan = 2)
    month_label.grid(row = 0, column = 4, columnspan = 2)
    
    root.mainloop()

    

calender()
