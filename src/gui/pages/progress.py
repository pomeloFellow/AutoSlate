from tkinter import ttk
import src.gui.logic.logic as logic

class ProgressPage(ttk.Frame):
    def __init__(self, parent, state, to_results):
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
        inner_frame.grid(row=1, column=1, sticky="ew", pady=20)
        inner_frame.grid_columnconfigure(0, weight=1)

        # progress text
        progress_text_label = ttk.Label(inner_frame, textvariable=state.progress_text) 
        progress_text_label.grid(row=0, column=0, sticky="ew", pady=(0, 10))

        # progress bar
        progress_bar = ttk.Progressbar(inner_frame, variable=state.progress_bar_value, orient="horizontal", 
                                       length=100, mode='determinate')
        
        progress_bar.grid(row=1, column=0, sticky="ew", pady=(0, 10))

        # results frame
        results_frame = ttk.Frame(inner_frame)
        results_frame.grid(row=2, column=0, sticky="ew", pady=(0, 10))

        # results button holder
        results_button_holder = ttk.Frame(results_frame)
        results_button_holder.grid(row=0, column=2, sticky="se", pady=(0, 10))

        # results button
        results_button = ttk.Button(results_button_holder, text="Results", command=to_results)
        results_button.pack()
        logic.bind_visibility(state.show_results_button,
                results_button,
                method="pack")

    def on_show(self):
        logic.progress_page_shown(self.state)
        
        