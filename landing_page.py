import ttkbootstrap as ttk

class LandingPage(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(2, weight=1)

        label = ttk.Label(self, text="Dorm Security App", font=("Helvetica", 18))
        label.grid(row=1, column=1, pady=10)

        register_button = ttk.Button(self, text="Register Dorm",
                                     command=lambda: controller.show_frame("RegisterPage"))
        register_button.grid(row=2, column=1, pady=20)

        login_button = ttk.Button(self, text="Get Into Dorm",
                                  command=lambda: controller.show_frame("LoginPage"))
        login_button.grid(row=3, column=1, pady=20)