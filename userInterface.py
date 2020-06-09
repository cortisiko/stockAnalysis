try:
    import Tkinter as tk
except:
    import tkinter as tk
import tkinter.font
from tkinter import *
from pages import cashFlowPage,homePage,netIncomePage,cashToEarningsPage,debtPage,earningsPage

from charts import plotEarnings as pltEarnings,plotRevenue as pltRevenue
from helpers import getMessageBox as messagebox


invalidTickerErrorMessage = "Sorry, you need to enter a ticker symbol"
noDebtErrorMessage = "Sorry Yahoo finance does not show any long term debt for this company"

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
        Charts.add_command(label="Revenue", command=lambda: self.show_frame(plotRevenueChart))


        menu.add_separator()
        tk.Tk.config(self, menu=menu)

        for F in (homePage.Startpage, cashFlowPage.cashflow, debtPage.plotDebtGraph, netIncomePage.IncomeStatement, plotRevenueChart, cashToEarningsPage.plotCashToEarnings):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(homePage.Startpage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

    def get_page(self, page_class):
        return self.frames[page_class]



#   *****   PAGES   *****

class plotRevenueChart(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self['bg'] = '#1B6666'
        self.controller = controller
        self.my_font = tkinter.font.Font(self, family="Sans Serif", size=20)
        self.pageTitle = Label(self, text="Revenue Charts", font=self.my_font)
        self.RadioText = StringVar()
        self.quarterlyTextString = 'quarterly'
        self.yearlyTextString = 'yearly'

        self.textInputBox = Text(self, relief=tk.RIDGE, height=1, width=6, borderwidth=2)
        self.frequencyText = Label(self, text="Frequency")
        self.quarterlyRadioButton = Radiobutton(self, text="Quarterly", variable=self.RadioText,
                                                value=self.quarterlyTextString, command=self.selectedRadioButtonOption)
        self.yearlyRadioButton = Radiobutton(self, text="Annual", variable=self.RadioText, value=self.yearlyTextString,
                                             command=self.selectedRadioButtonOption)

        self.clearButton = Button(self, text='Clear', command=self.clear, bg='red')
        self.pageTitle.pack()
        self.textInputBox.pack()
        self.quarterlyRadioButton.pack(side='left', padx=50)
        self.yearlyRadioButton.pack(side='right', padx=50)
        self.clearButton.pack()
        button1 = Button(self, text="Back to Home",
                         command=lambda: controller.show_frame(homePage.Startpage))

    def getTextInput(self):
        result = self.textInputBox.get("1.0", "end")
        result = result.rstrip()
        if len(result) > 0:
            results = result.upper()
            results = str(results)
            return results
        else:
            self.yearlyRadioButton.deselect()
            self.quarterlyRadioButton.deselect()
            messagebox.showErrorMessage(self,invalidTickerErrorMessage)

    def selectedRadioButtonOption(self):
        userInput = self.getTextInput()
        radioButtonFrequencyOption = self.RadioText.get()
        if not revenue.canvas:
            revenue.plotRevenue(self, userInput, radioButtonFrequencyOption)
        else:
            revenue.clearPlotPage()
            revenue.plotRevenue(self, userInput, radioButtonFrequencyOption)

    def destroyGraph(self):
        revenue.clearPlotPage()

    def clear(self):
        self.textInputBox.delete("1.0", "end")
        revenue.clearPlotPage()
        self.yearlyRadioButton.deselect()
        self.quarterlyRadioButton.deselect()


app = UserInterFace()
earnings = pltEarnings.PlotGraph()
revenue = pltRevenue.PlotGraph()
app.geometry("1300x600")
app.mainloop()
