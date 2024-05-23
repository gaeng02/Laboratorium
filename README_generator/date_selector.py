import tkinter as tk

def calender (month = 12, year = 2024) :

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

    def left () :
        print("left")
    def right () :
        print("right")

calender()
