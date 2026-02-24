import tkinter as tk
from tkinter import ttk
import ttkthemes

from src.gui.state import AppState
from src.gui.pages.start import StartPage
from src.gui.pages.progress import ProgressPage
from src.gui.pages.results import ResultsPage
from src.gui.pages.advsettings import AdvSettingsPage

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("AutoSlate")
        self.geometry("500x300")
        self.minsize(400, 250)

        style = ttkthemes.ThemedStyle(self)
        style.theme_use("equilux")

        self.state = AppState(self)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.content_frame = ttk.Frame(self)
        self.content_frame.grid(sticky="nsew")

        self.content_frame.grid_rowconfigure(0, weight=1)
        self.content_frame.grid_columnconfigure(0, weight=1)

        self.pages = {}

        # defining pages
        self.pages["main"] = StartPage(
            self.content_frame,
            self.state,
            to_progress_bar=lambda: self.show_page("progress"),
            to_adv_settings = lambda: self.show_page("advsettings")
        )

        self.pages["progress"] = ProgressPage(
            self.content_frame,
            self.state,
            to_results = lambda: self.show_page("results")
        )

        self.pages["results"] = ResultsPage(
            self.content_frame,
            self.state,
            to_start = lambda: self.show_page("main")
        )

        self.pages["advsettings"] = AdvSettingsPage(
            self.content_frame,
            self.state,
            to_progress_bar=lambda: self.show_page("progress")
        )

        # placing pages
        for page in self.pages.values():
            page.grid(row=0, column=0, sticky="nsew")

        self.show_page("main")

    def show_page(self, name):
        page = self.pages[name]
        page.tkraise()
        
        if hasattr(page, "on_show"):
            page.on_show()
