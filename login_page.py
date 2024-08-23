import ttkbootstrap as ttk
from data import data

class LoginPage(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.attempts = 0

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(2, weight=100)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(4, weight=1)

        label = ttk.Label(self, text="Login to Dorm", font=("Helvetica", 18))
        label.grid(row=1, column=1, pady=10)

        # Entry Labels

        # LSU ID Entry
        lsuid_label = ttk.Label(self, text="LSU ID")
        lsuid_label.grid(row=2, column=0, columnspan=1, pady=5)

        self.lsu_id_entry = ttk.Entry(self)
        self.lsu_id_entry.grid(row=2, column=1, pady=5)
        self.lsu_id_entry.insert(0, "")

        # PIN Entry

        pin_label = ttk.Label(self, text="PIN")
        pin_label.grid(row=3, column=0, pady=5)

        self.pin_entry = ttk.Entry(self, show="*")
        self.pin_entry.grid(row=3, column=1, pady=5)
        self.pin_entry.insert(0, "")

        login_button = ttk.Button(self, text="Login", command=self.login)
        login_button.grid(row=4, column=1, pady=20)

    def login(self):
        # Gets the information from the insert fields
        lsu_id = self.lsu_id_entry.get()
        pin = self.pin_entry.get()

        for user in data:
            if user["lsuId"] == lsu_id and user["pin"] == pin:
                self.controller.show_frame("VerificationPage")
                return

        self.attempts += 1
        if self.attempts >= 3:
            self.show_message("Too many attempts. Locked out.")
        else:
            self.show_message("Invalid LSU ID or PIN.")

    def show_message(self, message):
        message_label = ttk.Label(self, text=message, font=("Helvetica", 12))
        message_label.grid(row=5, column=1, pady=10)