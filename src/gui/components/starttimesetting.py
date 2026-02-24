from tkinter import ttk
import src.gui.logic.logic as logic
from src.gui.components.settingsbar import SettingBar

class StartTimeSetting(ttk.Frame):
    def __init__(self, settings_frame, state):
        super().__init__(settings_frame)
        self.state = state

        vcmd = (self.register(logic.validate_float), "%P")
    
        # --- START TIME ---
        start_desc = "Time (seconds) where AutoSlate begins audio detection."
        start_bar = SettingBar(settings_frame, "Start Time", start_desc)
        start_bar.grid(row=0, column=0, sticky="ew", pady=10)

        # Use start_bar.container as the parent
        start_frame = ttk.Frame(start_bar.container)
        start_frame.grid(row=0, column=0, sticky="e")

        start_combo = ttk.Combobox(
            start_frame,
            values=["Start of Clip", "Other"],
            state="readonly",
            textvariable=state.start_time_mode,
            width=16
        )
        start_combo.grid(row=0, column=0)

        start_entry = ttk.Entry(
            start_frame,
            textvariable=state.start_time,
            validate="key",
            validatecommand=vcmd,
            width=8
        )

        def toggle_start(event=None):
            if state.start_time_mode.get() == "Other":
                start_entry.grid(row=0, column=1, padx=5)
            else:
                start_entry.grid_forget()

        start_combo.bind("<<ComboboxSelected>>", toggle_start)
        toggle_start()