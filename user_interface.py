"""
Installing the tkinter library  """
try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk
import sys
import os
from PIL import Image, ImageTk

from app.pages import (
    netincomepage,
    cash_to_earnings_page,
    cash_flow_page,
    debtpage,
    homepage,
    revenuePage,
)

# Add the project root directory to the Python path

sys.path.append(os.path.dirname(os.path.dirname(__file__)))


class UserInterFace(tk.Tk):
    """
      User interface class
      """

    def __init__(self):
        tk.Tk.__init__(self)
        self.window_title = self.title("Stock Analyzer")
        container = tk.Frame(self)
        self.icon_image = Image.open("app/charticon2ICO.ico")
        self.icon_photo = ImageTk.PhotoImage(self.icon_image)

        # Set the window icon
        self.iconphoto(False, self.icon_photo)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        menu = tk.Menu(container)
        home = tk.Menu(menu, tearoff=0)
        menu.add_cascade(menu=home, label="Main")
        home.add_command(
            label="Home", command=lambda: self.show_frame(homepage.StartPage)
        )
        menu.add_separator()

        charts = tk.Menu(menu, tearoff=0)
        menu.add_cascade(menu=charts, label="Charts")

        charts.add_command(
            label="Cash Flow", command=lambda: self.show_frame(cashflowpage.CashFlow)
        )
        charts.add_command(
            label="Cash to Earnings",
            command=lambda: self.show_frame(cashtoearningspage.CashToEarnings),
        )
        charts.add_command(
            label="Long Term Debt", command=lambda: self.show_frame(debtpage.Debt)
        )
        charts.add_command(
            label="Net Income", command=lambda: self.show_frame(netincomepage.NetIncome)
        )
        charts.add_command(
            label="Revenue", command=lambda: self.show_frame(revenuePage.Revenue)
        )

        menu.add_separator()
        tk.Tk.config(self, menu=menu)

        for F in (
                homepage.StartPage,
                cash_flow_page.CashFlow,
                debtpage.Debt,
                netincomepage.NetIncome,
                revenuePage.Revenue,
                cash_to_earnings_page.CashToEarnings,
        ):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(homepage.StartPage)

    def show_frame(self, cont):
        """
        Shows frame
        """
        frame = self.frames[cont]
        frame.tkraise()

    def get_page(self, page_class):
        """
          gets the page
        """
        return self.frames[page_class]

    def on_closing(self):
        """
        Perform any cleanup here before closing
        """
        print("Cleaning up and closing the application...")
        self.destroy()


if __name__ == "__main__":
    try:
        app = UserInterFace()
        app.geometry("800x600")
        app.protocol("WM_DELETE_WINDOW", app.on_closing)
        app.mainloop()
    except KeyboardInterrupt as e:
        print("closing app")
