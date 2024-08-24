import ttkbootstrap as ttk

class AuthenticatedPage(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(5, weight=1)

        label = ttk.Label(self, text="You're inside your dorm.", font=("Helvetica", 18))
        label.grid(row=1, column=1, pady=10)

        label2 = ttk.Label(self, text="Check out professor index!")
        label2.grid(row=2, column=1, pady=10)

