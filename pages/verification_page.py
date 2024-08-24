import random
import ttkbootstrap as ttk
from twilio.rest import Client


class VerificationPage(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(4, weight=1)

        label = ttk.Label(self, text="Security Question Verification", font=("Helvetica", 18))
        label.grid(row=1, column=1, pady=10)
        # generate the question button
        generate_question_button = ttk.Button(self, text="Generate Question", command=self.generate_security_question)
        generate_question_button.grid(row=3, column=2, pady=5, padx=30, sticky='e')

        # Add to submit security question
        self.security_answer = ttk.Entry(self)
        self.security_answer.grid(row=3, column=1, pady=5, padx=30, sticky='e')

        verify_button = ttk.Button(self, text="Verify", command=self.verify_code)
        verify_button.grid(row=4, column=1, pady=20)

    def generate_security_question(self):
        print("Generating security question")

        query = self.controller.cursor.execute('''
        SELECT securityQuestion FROM Users WHERE lsuId=?
        ''', (self.controller.lsu_id,))
        self.controller.security_question = query.fetchone()[0]

        self.show_message(f"Security Question: {self.controller.security_question}")

    def verify_code(self):
        # Get the security answer from the entry
        security_answer = self.security_answer.get()

        # Check to see if the security answer is correct
        query = self.controller.cursor.execute('''
        SELECT securityAnswer FROM Users WHERE lsuId=?
        ''', (self.controller.lsu_id,))
        correct_answer = query.fetchone()[0]

        if security_answer.lower() == correct_answer.lower():
            print("Correct security answer")
            self.controller.show_frame("AuthenticatedPage")
        else:
            self.show_message("Incorrect security answer. Please try again.")

    def show_message(self, message):
        message_label = ttk.Label(self, text=message, font=("Helvetica", 12))
        message_label.grid(row=5, column=1, pady=10)