from tkinter import ttk
import tkinter as tk
from src.gui.components.settingsbar import SettingBar

class ConfidenceSetting(ttk.Frame):
    def __init__(self, settings_frame, state):
        super().__init__(settings_frame)
        self.state = state

        conf_desc = (
            "Minimum model confidence required to accept detected words.\n"
            "Recommended average working range: 0.30 – 0.40."
        )
        
        conf_bar = SettingBar(settings_frame, "Minimum Confidence", conf_desc)
        conf_bar.grid(row=2, column=0, sticky="ew", pady=10)

        conf_frame = ttk.Frame(conf_bar.container)
        conf_frame.grid(row=0, column=0, sticky="ew")
        conf_frame.columnconfigure(1, weight=1)

        slider_value = tk.DoubleVar(value=0.35)
        enable_var = tk.IntVar(value=0)

        enable_check = ttk.Checkbutton(conf_frame, text="Enable", variable=enable_var)
        enable_check.grid(row=0, column=0, padx=(0, 10))

        slider = ttk.Scale(conf_frame, from_=0.0, to=1.0, variable=slider_value)
        slider.grid(row=0, column=1, sticky="ew")

        value_label = ttk.Label(conf_frame, width=5)
        value_label.grid(row=0, column=2, padx=5)

        def update_label(*args):
            value_label.config(text=f"{slider_value.get():.2f}")

        slider_value.trace_add("write", update_label)
        update_label()

        def toggle_confidence(*args):
            if enable_var.get():
                slider.state(["!disabled"])
                value_label.state(["!disabled"])
                state.min_confidence.set(slider_value.get())
            else:
                slider.state(["disabled"])
                value_label.state(["disabled"])
                state.min_confidence.set(-1)

        enable_var.trace_add("write", toggle_confidence)

        def slider_changed(*args):
            if enable_var.get():
                state.min_confidence.set(slider_value.get())

        slider_value.trace_add("write", slider_changed)
        toggle_confidence()