import ttkbootstrap as ttk

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
        lsuid_label.grid(row=2, column=0, pady=5, padx=30, sticky='w')

        self.lsu_id_entry = ttk.Entry(self, justify="left")
        self.lsu_id_entry.grid(row=2, column=1, pady=5, padx=30,  sticky='e')
        self.lsu_id_entry.insert(0, "")

        # Dorm Number Entry
        dormNumberLbl = ttk.Label(self, text="Dorm Number:", justify="left")
        dormNumberLbl.grid(row=3, column=0, pady=5, padx=30, sticky='w')

        self.dorm_number_entry = ttk.Entry(self)
        self.dorm_number_entry.grid(row=3, column=1, pady=5, padx=30, sticky='e')
        self.dorm_number_entry.insert(0, "")

        # PIN Entry
        pin_label = ttk.Label(self, text="PIN:", justify="left")
        pin_label.grid(row=4, column=0, pady=5, padx=30, sticky='w')

        self.pin_entry = ttk.Entry(self, show="*")
        self.pin_entry.grid(row=4, column=1, pady=5, padx=30, sticky='e')
        self.pin_entry.insert(0, "")

        register_button = ttk.Button(self, text="Register", command=self.register_dorm)
        register_button.grid(row=5, column=1, pady=20)

        # Back button
        back_button = ttk.Button(self, text="Back", command=lambda: controller.show_frame("LandingPage"))
        back_button.grid(row=5, column=0, pady=20)

    def register_dorm(self):
        lsu_id = self.lsu_id_entry.get()
        dorm_number = self.dorm_number_entry.get()
        pin = self.pin_entry.get()

        if not lsu_id.startswith("89"):
            self.show_message("Invalid LSU ID. Should start with 89*******")
            return

        # Check to see if the LSU ID exists in the User table
        query = self.controller.cursor.execute('''
        SELECT lsuId FROM Users WHERE lsuId=?
        ''', (lsu_id,))

        # If the LSU ID does not exist, show an error message
        if query.fetchone() is None:
            self.show_message("LSU ID not found.")
            return

        # Make sure the user doesn't already have a dorm registered
        dormQuery = self.controller.cursor.execute('''
        SELECT lsuId FROM Dorm WHERE lsuId=?
        ''', (lsu_id,))

        if dormQuery.fetchone() is not None:
            self.show_message("User already has a dorm registered. Must get it changed through front desk.")
            return

        # Insert into Dorm table
        try:
            self.controller.cursor.execute('''
            INSERT INTO DormMembers (lsuId, pin, dormNumber)
            VALUES (?, ?, ?)
            ''', (lsu_id, pin, dorm_number))
        except Exception as e:
            self.show_message("User already registered with dorm or dorm already registered with user.")
            print(e)
            return

        self.controller.conn.commit()

        self.show_message("Registration successful.")

    def show_message(self, message):
        message_label = ttk.Label(self, text=message, font=("Helvetica", 12))
        message_label.grid(row=6, column=1, pady=10)