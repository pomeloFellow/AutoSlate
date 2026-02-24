from tkinter import ttk
import tkinter as tk
from src.gui.components.tooltip import ToolTip

class SettingBar(ttk.Frame):
    def __init__(self, parent, setting, description, **kwargs):
        super().__init__(parent, **kwargs)

        self.columnconfigure(0, weight=0)  # Label stays small
        self.columnconfigure(1, weight=1)  # Container takes ALL remaining horizontal space

        label = ttk.Label(self, text=setting)
        label.grid(row=0, column=0, sticky="w", padx=5, pady=5)

        self.container = ttk.Frame(self)
        # Change sticky to "nsew" so the container fills the entire right side
        self.container.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)
        
        # Configure the container's own internal column to push items to the right
        self.container.columnconfigure(0, weight=1)

        ToolTip(label, description)