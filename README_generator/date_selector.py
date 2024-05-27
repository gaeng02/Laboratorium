import tkinter as tk

class Calender () :

    def __init__ (self, root) :
        
        self.root = root
        self.root.title("Calender")
        self.root.geometry("300x140")
        self.root.resizable(0, 0)
        
        self.current = datetime.now()
        self.selected_date = "None"

        # Header
        self.header_frame = ttk.Frame(root)
        self.header_frame.pack()

        self.left_button = ttk.Button(self.header_frame, text = "◀", command = left)
        self.left_button.grid(row = 0, column = 0)
        
        self.right_button = ttk.Button(self.header_frame, text = "▶", command = right)
        self.right_button.grid(row = 0, column = 6)

        # Calendar          
        self.calendar_frame = ttk.Frame(root)
        self.calendar_frame.pack()

        self.create()
        self.update()

        # Selection 
        self.selection_frame = ttk.Frame(root)
        self.selection_frame.pack()

        self.selection_label = ttk. Label(self.selection_frame, text = "", anchor = "center")
        self.selection_label.pack()

        self.year_label = ttk.Label(self.header_frame, text = self.y)
        year_label.grid(row = 0, column = 1, columnspan = 2)
        self.month_label = ttk.Label(self.header_frame, text = self.m)
        month_label.grid(row = 0, column = 4, columnspan = 2)


    def create (self) :

    def update (self) :
        
        
if (__name__ == "__main__") :
    root = tk.Tk()
    app = Calendar(root)
    root.mainloop()
