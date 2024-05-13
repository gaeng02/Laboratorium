# write user_data

import tkinter as tk
import os

def read_file () :
    file = "_user_info.txt"
    
    if not os.path.exists(file) :
        
        with open(file, 'w') as f :
            f.write("token_api \ndatabase_id")
            
        return False

    with open(file, 'r') as f :
        data = f.read()

    return True


def setup () : 
    window = tk.Tk()

    window.title = ("User Info Setup")
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
    
    load_button = tk.Button(window, text = "Load") # command = load
    load_button.grid(row = 2, column = 1, padx = 10, pady = 10)

    save_button = tk.Button(window, text = "Save") # command = save
    save_button.grid(row = 2, column = 2, padx = 10, pady = 10)
    
    window.mainloop()


setup()
