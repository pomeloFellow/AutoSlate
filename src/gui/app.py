import tkinter as tk
from tkinter import ttk
import ttkthemes

from src.gui.state import AppState
from src.gui.pages.start import StartPage

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("AutoSlate")
        self.geometry("500x300")
        self.minsize(400, 250)

        style = ttkthemes.ThemedStyle(self)
        style.theme_use("equilux")

        self.state = AppState()

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.content_frame = ttk.Frame(self)
        self.content_frame.grid(sticky="nsew")

        self.content_frame.grid_rowconfigure(0, weight=1)
        self.content_frame.grid_columnconfigure(0, weight=1)

        self.pages = {}

        self.pages["main"] = StartPage(
            self.content_frame,
            self.state,
            # show_settings=lambda: self.show_page("settings")
        )

        for page in self.pages.values():
            page.grid(row=0, column=0, sticky="nsew")

        self.show_page("main")

    def show_page(self, name):
        self.pages[name].tkraise()
