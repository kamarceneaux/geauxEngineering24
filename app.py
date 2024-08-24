import sqlite3
import ttkbootstrap as ttk

from pages.access_expired import AccessExpiredPage
from pages.landing_page import LandingPage
from pages.login_page import LoginPage
from pages.register_page import RegisterPage
from pages.verification_page import VerificationPage


class App(ttk.Window):
    def __init__(self):
        super().__init__()
        self.title("Dorm Security App")
        self.geometry("500x500")
        self.resizable(False, False)

        self.conn = sqlite3.connect('dorm_security.db')
        self.cursor = self.conn.cursor()

        self.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (LandingPage, RegisterPage, LoginPage, VerificationPage, AccessExpiredPage):
            page_name = F.__name__
            frame = F(parent=self, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="news")

        self.show_frame("LandingPage")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

    def __del__(self):
        self.conn.close()

if __name__ == "__main__":
    app = App()
    app.mainloop()