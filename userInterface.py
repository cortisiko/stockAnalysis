try:
    import Tkinter as tk
except:
    import tkinter as tk
from pages import cashFlowPage,homePage,netIncomePage,cashToEarningsPage,debtPage,earningsPage,revenuePage

class UserInterFace(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        container = tk.Frame(self)
        self.windowTitle = self.title("Stock Analyzer")
        self.iconbitmap('charticon2ICO.ico')

        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        menu = tk.Menu(container)
        Home = tk.Menu(menu, tearoff=0)
        menu.add_cascade(menu=Home, label="Main")
        Home.add_command(label="Home",
                         command=lambda: self.show_frame(homePage.Startpage))
        menu.add_separator()

        Charts = tk.Menu(menu, tearoff=0)
        menu.add_cascade(menu=Charts, label="Charts")

        Charts.add_command(label="Cash Flow", command=lambda: self.show_frame(cashFlowPage.cashflow))
        Charts.add_command(label="Cash to Earnings", command=lambda: self.show_frame(cashToEarningsPage.plotCashToEarnings))
        Charts.add_command(label="Long Term Debt", command=lambda: self.show_frame(debtPage.plotDebtGraph))
        Charts.add_command(label="Net Income", command=lambda: self.show_frame(netIncomePage.IncomeStatement))
        Charts.add_command(label="Revenue", command=lambda: self.show_frame(revenuePage.plotRevenueChart))


        menu.add_separator()
        tk.Tk.config(self, menu=menu)

        for F in (homePage.Startpage, cashFlowPage.cashflow, debtPage.plotDebtGraph, netIncomePage.IncomeStatement, revenuePage.plotRevenueChart, cashToEarningsPage.plotCashToEarnings):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(homePage.Startpage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

    def get_page(self, page_class):
        return self.frames[page_class]


app = UserInterFace()
app.geometry("1300x600")
app.mainloop()
