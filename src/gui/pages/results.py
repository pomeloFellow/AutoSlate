from tkinter import ttk
import src.gui.logic.logic as logic
import src.gui.logic.ProgressReport as pr
from src.gui.components.scrollableframe import ScrollableFrame

class ResultsPage(ttk.Frame):
    def __init__(self, parent, state, to_start):
        super().__init__(parent)
        self.state = state

        self.grid(row=0, column=0, sticky="nsew")

        # Outer 3x3 grid (center weighted)
        for i in range(3):
            weight = 10 if i == 1 else 1
            self.grid_rowconfigure(i, weight=weight)
            self.grid_columnconfigure(i, weight=weight)

        # Centered Inner Frame
        inner_frame = ttk.Frame(self)
        inner_frame.grid(row=1, column=1, sticky="nsew")  # CENTER CELL

        # Configure inner frame layout
        inner_frame.grid_rowconfigure(1, weight=1)   # Middle expands
        inner_frame.grid_columnconfigure(0, weight=1)

        # Title (Top Right)
        title_label = ttk.Label(inner_frame, text="Files Renamed:")
        title_label.grid(row=0, column=0, sticky="nw", padx=10, pady=10)

        # Results Frame (Middle Fill)
        self.results_container = ScrollableFrame(inner_frame)
        self.results_container.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)
        state.results_frame = self.results_container.scrollable_frame

        # Done Button (Bottom Left)
        done_button = ttk.Button(inner_frame, text="Done", command=to_start)
        done_button.grid(row=2, column=0, sticky="se", padx=10, pady=10)

    def on_show(self):
        logic.update_results_ui(self.state)