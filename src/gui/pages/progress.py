from tkinter import ttk
import src.gui.logic.logic as logic

class ProgressPage(ttk.Frame):
    def __init__(self, parent, state):
        super().__init__(parent)
        self.state = state

        self.grid(row=0, column=0, sticky="nsew")

        # Outer 3x3 grid with weighted center
        for i in range(3):
            weight = 10 if i == 1 else 1
            self.grid_rowconfigure(i, weight=weight)
            self.grid_columnconfigure(i, weight=weight)

        # Inner centered frame
        inner_frame = ttk.Frame(self)
        inner_frame.pack(expand=True, fill="both")

        # progress bar
        progress_bar = ttk.Progressbar(inner_frame, variable=state.progress_bar_value orient="horizontal", 
                                       length=100, mode='determinate')
        
        progress_bar.pack(pady=10)
    
    def on_show(self):
        logic.progress_page_shown(self.state)
        
        