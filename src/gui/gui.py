# based on Clear Code tutorial
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk

#commands
def browse_folder():
    folder = filedialog.askdirectory()
    if folder:
        input_var.set(folder)

def start():
    input_path = input_var.get()
    if not input_path:
        messagebox.showerror("Error", "Please select an input folder")
        return
    
    try:
        messagebox.showinfo("Done", "Processing complete!")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# window
window = tk.Tk()
window.title = ('AutoSlate')
window.geometry('300x150')

#input
input_var = tk.StringVar()

tk.Label(window, text="Input Folder:").pack(pady=(10, 0))
tk.Entry(window, textvariable=input_var, width=60).pack(pady=5)

tk.Button(window, text="Browse", command=browse_folder).pack()
tk.Button(window, text="Run", command=start).pack(pady=10)
