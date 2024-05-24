import tkinter as tk

class calender (month = 12, year = 2024) :
    
    def left () :
        calender(month - 1, year)
        
    def right () :
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
    
    root.mainloop()

    

calender()
