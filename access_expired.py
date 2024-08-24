import ttkbootstrap as ttk

class AccessExpiredPage(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        label = ttk.Label(self, text="Access Expired", font=("Helvetica", 18))
        label.pack(pady=20)

        message = ttk.Label(self, text="You have exceeded the maximum number of login attempts.", font=("Helvetica", 12))
        message.pack(pady=10)