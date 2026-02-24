from tkinter import ttk
import src.gui.logic.logic as logic
from src.gui.components.settingsbar import SettingBar

class EndTimeSetting(ttk.Frame):
    def __init__(self, settings_frame, state):
        super().__init__(settings_frame)
        self.state = state

        vcmd = (self.register(logic.validate_float), "%P")

        end_desc = "Time (seconds) where AutoSlate stops audio detection."
        end_bar = SettingBar(settings_frame, "End Time", end_desc)
        end_bar.grid(row=1, column=0, sticky="ew", pady=10)

        # Use end_bar.container as the parent
        end_frame = ttk.Frame(end_bar.container)
        end_frame.grid(row=0, column=0, sticky="e")

        end_combo = ttk.Combobox(
            end_frame,
            values=["Slate Clap", "Other", "End of Clip"],
            state="readonly",
            textvariable=state.min_time_mode,
            width=16
        )
        end_combo.grid(row=0, column=0)

        end_entry = ttk.Entry(
            end_frame,
            textvariable=state.min_time,
            validate="key",
            validatecommand=vcmd,
            width=8
        )

        def toggle_end(event=None):
            mode = state.min_time_mode.get()
            
            if mode == "Other":
                end_entry.grid(row=0, column=1, padx=5)
            elif mode == "Slate Clap":
                end_entry.grid_forget()
                state.min_time.set(-1)
            elif mode == "End of Clip":
                end_entry.grid_forget()
                state.min_time.set(-2)

        end_combo.bind("<<ComboboxSelected>>", toggle_end)
        toggle_end()