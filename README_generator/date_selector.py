import tkinter as tk

class calender () :

    def __init__ (self, month = 12, year = 2024) :
        self.m = month
        self.y = year
        self.display()
        
    def check (self) :
        if (self.m < 1) :
            self.m += 12
            self.y -= 1
        elif (self.m > 12) :
            self.m -= 12
            self.y += 1

    def display(self) :

        def left () :
            self.m -= 1
            self.check()
        
        def right () :
            self.m += 1
            self.check()
        
        root = tk.Tk()
        root.title("Calender")
        root.geometry("300x140")
        root.resizable(0, 0)

        left_button = tk.Button(root, text = "◀", command = left)
        right_button = tk.Button(root, text = "▶", command = right)

        left_button.grid(row = 0, column = 0)
        right_button.grid(row = 0, column = 6)

        year_label = tk.Label(root, text = self.y)
        month_label = tk.Label(root, text = self.m)

        year_label.grid(row = 0, column = 1, columnspan = 2)
        month_label.grid(row = 0, column = 4, columnspan = 2)

        print(self.m, self.y)
        
        root.mainloop()

calender()
