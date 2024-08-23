import ttkbootstrap as ttk
from data import data

class RegisterPage(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(5, weight=1)

        label = ttk.Label(self, text="Register Dorm", font=("Helvetica", 18), justify="center")
        label.grid(row=1, column=1, pady=10, sticky='we')

        # LSU ID Entry
        lsuid_label = ttk.Label(self, text="LSU ID:", justify="left")
        lsuid_label.grid(row=2, column=0, pady=5, sticky='w')

        self.lsu_id_entry = ttk.Entry(self, justify="right")
        self.lsu_id_entry.grid(row=2, column=1, pady=5, sticky='e')
        self.lsu_id_entry.insert(0, "")

        # Dorm Number Entry
        dormNumberLbl = ttk.Label(self, text="Dorm Number:", justify="left")
        dormNumberLbl.grid(row=3, column=0, pady=5, sticky='w')

        self.dorm_number_entry = ttk.Entry(self)
        self.dorm_number_entry.grid(row=3, column=1, pady=5, sticky='e')
        self.dorm_number_entry.insert(0, "")

        # PIN Entry
        pin_label = ttk.Label(self, text="PIN:", justify="left")
        pin_label.grid(row=4, column=0, pady=5, sticky='w')

        self.pin_entry = ttk.Entry(self, show="*")
        self.pin_entry.grid(row=4, column=1, pady=5, sticky='e')
        self.pin_entry.insert(0, "")

        register_button = ttk.Button(self, text="Register", command=self.register_dorm)
        register_button.grid(row=5, column=1, pady=20)

    def register_dorm(self):
        lsu_id = self.lsu_id_entry.get()
        dorm_number = self.dorm_number_entry.get()
        pin = self.pin_entry.get()

        for user in data:
            if user["lsuId"] == lsu_id:
                self.show_message("LSU ID already registered.")
                return
            if user["dorm"]["roomNumber"] == dorm_number:
                self.show_message("Dorm number already registered.")
                return

        for user in data:
            if user["lsuId"] == lsu_id:
                user["dorm"]["roomNumber"] = dorm_number
                user["pin"] = pin
                self.show_message("Dorm registered successfully.")
                return

        self.show_message("LSU ID or Dorm number not found.")

    def show_message(self, message):
        message_label = ttk.Label(self, text=message, font=("Helvetica", 12))
        message_label.grid(row=6, column=1, pady=10)