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


window = tk.Tk()

window.title = ("User Info Setup")
window.geometry("800x200")
window.resizable(0, 0)
