from tkinter import ttk

class ResultBar(ttk.Frame):
    def __init__(self, parent, og_name, new_name, **kwargs):
        super().__init__(parent, **kwargs)

        self.grid_columnconfigure(1, weight=1)

        og_name_label = ttk.Label(self, text=og_name)
        og_name_label.grid(row=0, column=0, sticky="nsw")

        new_name_label = ttk.Label(self, text=new_name)
        new_name_label.grid(row=0, column=2, sticky="nse")