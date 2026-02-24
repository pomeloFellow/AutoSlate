from tkinter import ttk
import tkinter as tk

class ToolTip():
    def __init__(self, widget, text, delay=500):
        self.widget = widget
        self.text = text
        self.delay = delay  # Time in milliseconds (500ms = 0.5 seconds)
        self.tip_window = None
        self.after_id = None  # To track the scheduled "show" event
        
        widget.bind("<Enter>", self.schedule_show)
        widget.bind("<Leave>", self.hide)

    def schedule_show(self, event=None):
        """Schedules the tooltip to appear after the delay."""
        self.after_id = self.widget.after(self.delay, self.show)

    def show(self, event=None):
        if self.tip_window or not self.text:
            return

        # Position the tooltip slightly away from the cursor to avoid flickering
        x = self.widget.winfo_rootx() + 25
        y = self.widget.winfo_rooty() + 25

        self.tip_window = tw = tk.Toplevel(self.widget)
        tw.wm_overrideredirect(True)
        tw.wm_geometry(f"+{x}+{y}")

        label = ttk.Label(
            tw,
            text=self.text,
            background="#ffffe0",
            relief="solid",
            borderwidth=1,
            padding=5
        )
        label.pack()

    def hide(self, event=None):
        # Cancel any scheduled show event if the mouse leaves early
        if self.after_id:
            self.widget.after_cancel(self.after_id)
            self.after_id = None
            
        # Destroy the window if it's currently visible
        if self.tip_window:
            self.tip_window.destroy()
            self.tip_window = None