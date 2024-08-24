import ttkbootstrap as ttk

class LoginPage(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.attempts = 0

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(4, weight=1)

        label = ttk.Label(self, text="Login to Dorm", font=("Helvetica", 18))
        label.grid(row=1, column=0, pady=10, columnspan=2)

        # LSU ID Entry
        lsuid_label = ttk.Label(self, text="LSU ID")
        lsuid_label.grid(row=2, column=0, columnspan=1, pady=5, padx=30, sticky='w')

        self.lsu_id_entry = ttk.Entry(self)
        self.lsu_id_entry.grid(row=2, column=1, pady=5, padx=30, sticky='e')
        self.lsu_id_entry.insert(0, "")

        # Dorm number
        dorm_number = ttk.Label(self, text="Dorm Number")
        dorm_number.grid(row=3, column=0, pady=5, padx=30, sticky='w')

        self.dorm_num = ttk.Entry(self, show="*")
        self.dorm_num.grid(row=3, column=1, pady=5, padx=30, sticky='e')
        self.dorm_num.insert(0, "")

        # Pin Entry
        pin_label = ttk.Label(self, text="PIN")
        pin_label.grid(row=4, column=0, pady=5, padx=30, sticky='w')

        self.pin_entry = ttk.Entry(self, show="*")
        self.pin_entry.grid(row=4, column=1, pady=5, padx=30, sticky='e')
        self.pin_entry.insert(0, "")

        login_button = ttk.Button(self, text="Verify Access ", command=self.login)
        login_button.grid(row=5, column=1, pady=20)

        # Back button
        back_button = ttk.Button(self, text="Back", command=lambda: controller.show_frame("LandingPage"))
        back_button.grid(row=5, column=0, pady=20)

    def login(self):
        # Gets the information from the insert fields
        lsu_id = self.lsu_id_entry.get()
        dorm_num = self.dorm_num.get()

        # If the lsu ID does not start with 89, it is invalid
        if not lsu_id.startswith("89"):
            self.show_message("Invalid LSU ID. Should start with 89*******")
            self.increment_attempts()
            return
        else:
            # Check to see if the LSU ID exists in the User table and then check to see if that dorm number is
            # associated with the LSU ID
            query = self.controller.cursor.execute('''
                            SELECT lsuId FROM DormMembers WHERE lsuId=?
                            ''', (lsu_id,))

            if query.fetchone() is None:
                self.show_message("Invalid LSU ID")
                self.increment_attempts()
                return

            query = self.controller.cursor.execute('''
                            SELECT dormNumber FROM DormMembers WHERE lsuId=? AND dormNumber=?
                            ''', (lsu_id, dorm_num))

            if query.fetchone() is None:
                self.show_message("Invalid Dorm Number or unassociated with LSU ID")
                self.increment_attempts()
                return

            # If the pin is correct, the user is now must verify themselves
            pin = self.pin_entry.get()
            query = self.controller.cursor.execute('''
                            SELECT pin FROM DormMembers WHERE lsuId=?
                            ''', (lsu_id,))

            if query.fetchone()[0] == pin:
                self.controller.lsu_id = lsu_id
                self.controller.show_frame("VerificationPage")
            else:
                self.show_message("Invalid PIN, please try again")
                self.increment_attempts()
                return

    def increment_attempts(self):
        self.attempts += 1
        if self.attempts >= 3:
            self.controller.show_frame("AccessExpiredPage")

    def show_message(self, message):
        message_label = ttk.Label(self, text=message, font=("Helvetica", 12))
        message_label.grid(row=6, column=1, pady=10)