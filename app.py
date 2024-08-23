
import ttkbootstrap as ttk
from landing_page import LandingPage
from register_page import RegisterPage
from login_page import LoginPage
from verification_page import VerificationPage

# The main runner for the entire app

class App(ttk.Window):
    def __init__(self):
        super().__init__(themename="darkly")
        self.title("Dorm Security App")
        self.geometry("500x500")
        self.resizable(False, False)

        self.frames = {}
        for F in (LandingPage, RegisterPage, LoginPage, VerificationPage):
            page_name = F.__name__
            frame = F(parent=self, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("LandingPage")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

if __name__ == "__main__":
    app = App()
    app.mainloop()