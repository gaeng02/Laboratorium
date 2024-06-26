# write user_data

import tkinter as tk
from tkinter import messagebox
import os

def setup () :
    file = "_user_info_.txt"
    
    def Load () :
        
        if not os.path.exists(file) :
            tk.messagebox.showinfo("Load Failed", "There is no file. Check again.")
            return ;

        with open(file, 'r') as f :
            data = f.read()
            # data = ["api_token_test", "database_id_test"]
            
            api_token_entry.delete(0, tk.END)
            api_token_entry.insert(0, data[0])
            database_id_entry.delete(0, tk.END)
            database_id_entry.insert(0, data[1])


    def Save () :
        
        api_token = api_token_entry.get()
        database_id = database_id_entry.get()

        messagebox.askokcancel("Save", "Are you sure you're going to save it?")
        with open(file, 'w') as f :
            f.write(api_token + '\n' + database_id)           

            
    window = tk.Tk()

    window.title("User Info Setup")
    window.geometry("400x140")
    window.resizable(0, 0)

    bg_color = "SkyBlue1"
    fg_color = "Black"
    font = 14 
    
    window.configure(bg = bg_color)
    
    api_token_label = tk.Label(window, text = "Private API token ", bg = bg_color, fg = fg_color, font = font)
    api_token_label.grid(row = 0, column = 0, padx = 10, pady = 10)

    api_token_entry = tk.Entry(window, width = 30)
    api_token_entry.grid(row = 0, column = 1, padx = 10, pady = 10, columnspan = 2)

    database_id_label = tk.Label(window, text = "Database ID ", bg = bg_color, fg = fg_color, font = font)
    database_id_label.grid(row = 1, column = 0, padx = 10, pady = 10)
    
    database_id_entry = tk.Entry(window, width = 30)
    database_id_entry.grid(row = 1, column = 1, padx = 10, pady = 10, columnspan = 2)
    
    load_button = tk.Button(window, text = "Load", command = Load) # command = load
    load_button.grid(row = 2, column = 1, padx = 10, pady = 10)

    save_button = tk.Button(window, text = "Save", command = Save) # command = save
    save_button.grid(row = 2, column = 2, padx = 10, pady = 10)
    
    window.mainloop()


setup()
