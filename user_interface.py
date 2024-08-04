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
    net_income_page,
    cash_to_earnings_page,
    cash_flow_page,
    debt_page,
    homepage,
    revenue_page,
)

# Add the project root directory to the Python path

if getattr(sys, 'frozen', False):
    # If running as a PyInstaller bundle
    # pylint: disable=protected-access
    bundle_dir = sys._MEIPASS
else:
    # If running in a normal Python environment
    bundle_dir = os.path.abspath(os.path.dirname(__file__))

icon_path = os.path.join(bundle_dir, "assets/charticon2ICO.ico")


class UserInterFace(tk.Tk):
    """
      User interface class
      """

    def __init__(self):
        tk.Tk.__init__(self)
        self.window_title = self.title("Stock Analyzer")
        container = tk.Frame(self)
        self.icon_image = Image.open(icon_path)
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
            label="Cash Flow", command=lambda: self.show_frame(cash_flow_page.CashFlow)
        )
        charts.add_command(
            label="Cash to Earnings",
            command=lambda: self.show_frame(cash_to_earnings_page.CashToEarnings),
        )
        charts.add_command(
            label="Long Term Debt", command=lambda: self.show_frame(debt_page.Debt)
        )
        charts.add_command(
            label="Net Income", command=lambda: self.show_frame(net_income_page.NetIncome)
        )
        charts.add_command(
            label="Revenue", command=lambda: self.show_frame(revenue_page.Revenue)
        )

        menu.add_separator()
        tk.Tk.config(self, menu=menu)

        for F in (
                homepage.StartPage,
                cash_flow_page.CashFlow,
                debt_page.Debt,
                net_income_page.NetIncome,
                revenue_page.Revenue,
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
        sys.exit(0)  # Ensure the application exits


if __name__ == "__main__":
    try:
        app = UserInterFace()
        app.geometry("1200x800")
        app.protocol("WM_DELETE_WINDOW", app.on_closing)
        app.mainloop()
    except KeyboardInterrupt as e:
        print("closing app")
