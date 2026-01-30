from tkinter import ttk
import src.gui.logic as logic

class StartPage(ttk.Frame):
    def __init__(self, parent, state):
        super().__init__(parent)
        self.state = state

        self.grid(row=0, column=0, sticky="nsew")

        # Outer 3x3 grid with weighted center (~75%)
        for i in range(3):
            weight = 6 if i == 1 else 1
            self.grid_rowconfigure(i, weight=weight)
            self.grid_columnconfigure(i, weight=weight)

        # Inner centered frame
        inner_frame = ttk.Frame(self)
        inner_frame.grid(row=1, column=1, sticky="nsew")

        inner_frame.grid_columnconfigure(0, weight=1)
        inner_frame.grid_rowconfigure(0, weight=1)  # logo
        inner_frame.grid_rowconfigure(1, weight=1)  # buttons

        # Logo placeholder
        ttk.Label(inner_frame, text="LOGO").grid(
            row=0, column=0, sticky="nsew"
        )

        # Buttons frame
        buttons_frame = ttk.Frame(inner_frame)
        buttons_frame.grid(row=1, column=0, sticky="ew", pady=20)
        buttons_frame.grid_columnconfigure(0, weight=1)

        ttk.Button(
            buttons_frame,
            textvariable=state.folder_button_text,
            command=lambda: logic.browse_folder(state)
        ).grid(row=0, column=0, sticky="ew", pady=(0, 10))

        ttk.Button(
            buttons_frame,
            text="Relabel Videos",
            command=lambda: logic.relabel_videos(state)
        ).grid(row=1, column=0, sticky="ew", pady=(0, 10))

        ttk.Button(
            buttons_frame,
            text="Advanced Settings"
        ).grid(row=2, column=0, sticky="ew")
