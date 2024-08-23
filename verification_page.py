import ttkbootstrap as ttk
import random
import string

class VerificationPage(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(4, weight=1)

        label = ttk.Label(self, text="Phone Verification", font=("Helvetica", 18))
        label.grid(row=1, column=1, pady=10)

        self.verification_code_entry = ttk.Entry(self)
        self.verification_code_entry.grid(row=2, column=1, pady=5)
        self.verification_code_entry.insert(0, "Verification Code")

        verify_button = ttk.Button(self, text="Verify", command=self.verify_code)
        verify_button.grid(row=3, column=1, pady=20)

        self.generate_verification_code()

    def generate_verification_code(self):
        self.verification_code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
        # Here you would send the verification code to the user's phone number
        print(f"Verification code sent: {self.verification_code}")

    def verify_code(self):
        entered_code = self.verification_code_entry.get()
        if entered_code == self.verification_code:
            self.show_message("Verification successful.")
        else:
            self.show_message("Invalid verification code.")

    def show_message(self, message):
        message_label = ttk.Label(self, text=message, font=("Helvetica", 12))
        message_label.grid(row=4, column=1, pady=10)