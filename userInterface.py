try:
    import Tkinter as tk
except:
    import tkinter as tk
from charts import plotCashFlow as pltCashFlow, plotNetIncome as pltIncome, plotEarnings as pltEarnings
import tkinter.font
from Financials import analyze as anlyze
from tkinter import *
from helpers import getMessageBox as messagebox

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
                         command=lambda: self.show_frame(Startpage))
        menu.add_separator()

        Charts = tk.Menu(menu, tearoff=0)
        menu.add_cascade(menu=Charts, label="Charts")

        Charts.add_command(label="Cash Flow", command=lambda: self.show_frame(PlotCashFlowChart))
        Charts.add_command(label="Earnings", command=lambda: self.show_frame(plotEarningsChart))
        Charts.add_command(label="Net Income", command=lambda: self.show_frame(PlotIncomeStatementChart))

        menu.add_separator()
        tk.Tk.config(self, menu=menu)

        for F in (Startpage, PlotCashFlowChart, PlotIncomeStatementChart, plotEarningsChart):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(Startpage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

    def get_page(self, page_class):
        return self.frames[page_class]


class Startpage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.parent = parent
        self.my_font = tkinter.font.Font(self, family="Comic Sans MS", size=20)
        self.stockSymbolText = Label(self, text="Enter Stock Symbol: ")
        self.textInputBox = Entry(self,relief=RIDGE, width=10, borderwidth=4)
        self.analyzeButton = Button(self,
                                    text='Analyze Stock', relief=RAISED, borderwidth=7, bg='green',
                                    command=self.analyze)
        self.clearButton = Button(self, text="Clear", relief=RIDGE, command=self.clearValues)
        self.textInputBox.focus()
        self.clearButton = Button(self, text="Clear", relief=RIDGE, command=self.clearValues, bg='red')
        # self.graphCashFlowButton = Button(self, text="See Cash Flow Graph",command=lambda: controller.show_frame(PlotCashFlowChart))

        self.earningsPerShareLabelText = Label(self, text="Earnings Per Share: ", width=30, anchor="w")
        self.peRatioLabelText = Label(self, text="PE Ratio: ", width=30, anchor="w")
        self.returnOnEquityLabelText = Label(self, text="Return on Equity Ratio: ", width=30, anchor="w")
        self.currentStockPriceLabelText = Label(self, text="Current Stock Price: ", width=30, anchor="w")
        self.debtToEquityRatioLabelText = Label(self, text="Debt to Equity Ratio: ", width=30, anchor="w")
        self.profitMarginLabelText = Label(self, text="Profit Margin: ", width=30, anchor="w")
        self.companyNameLabelText = Label(self, text="", font=self.my_font)
        self.companySectorLabelText = Label(self,text="Sector",width=30, anchor="w")
        ##Binding the Enter key
        self.parent.bind('<Return>', self.analyze)

        # making new spots for values returned
        self.earningsPerShareValue = Label(self, text="", width=30, anchor="w")
        self.companySectorValue = Label(self, text="", width=30, anchor="w")
        self.peRatioValue = Label(self, text="", width=30, anchor="w")
        self.returnOnEquityValue = Label(self, text="", width=30, anchor="w")
        self.currentStockPriceValue = Label(self, text="", width=30, anchor="w")
        self.debtToEquityRatioValue = Label(self, text="", width=30, anchor="w")
        self.profitMarginValue = Label(self, text="", width=30, anchor="w")

        self.earningsPerShareDefaultText = "Earnings Per Share: "
        self.companyNameDefaultText = ""
        self.companySectorDefaultText = "Sector:"
        self.peRatioDefaultText = "PE Ratio: "
        self.returnOnEquityDefaultText = "Return on Equity Ratio: "
        self.currentStockPriceDefaultText = "Current Stock Price: "
        self.debtToEquityRatioDefaultText = "Debt to Equity Ratio: "
        self.profitMarginDefaultText = "Profit Margin: "

        self.companySectorDefaultValue = ""
        self.earningsPerShareDefaultValue = ""
        self.peRatioLabelDefaultValue = ""
        self.returnOnEquityDefaultValue = ""
        self.currentStockPriceDefaultValue = ""
        self.debtToEquityRatioDefaultValue = ""
        self.profitMarginDefaultValue = ""

        ## Griding Values and Text
        self.stockSymbolText.grid(row=0, column=3)
        self.textInputBox.grid(row=0, column=4, sticky="nsew")
        self.textInputBox.bind('<Return>', self.analyze)
        self.analyzeButton.grid(row=3, column=3, pady=4, sticky="nsew")
        self.clearButton.grid(row=3, column=4, ipadx=10)
        # self.graphCashFlowButton.grid(row=3, column=5, ipadx=10)
        # self.bind('<Return>', lambda event: self.analyze)

        self.companyNameLabelText.grid(row=5, column=4)
        self.companySectorLabelText.grid(row=6, column=4)
        self.currentStockPriceLabelText.grid(row=7, column=4)
        self.earningsPerShareLabelText.grid(row=8, column=4)
        self.peRatioLabelText.grid(row=9, column=4)
        self.returnOnEquityLabelText.grid(row=10, column=4)
        self.debtToEquityRatioLabelText.grid(row=11, column=4)
        self.profitMarginLabelText.grid(row=12, column=4)

        # Fields for values
        self.companySectorValue.grid(row=6, column=5)
        self.currentStockPriceValue.grid(row=7, column=5)
        self.earningsPerShareValue.grid(row=8, column=5)
        self.peRatioValue.grid(row=9, column=5)
        self.returnOnEquityValue.grid(row=10, column=5)
        self.debtToEquityRatioValue.grid(row=11, column=5)
        self.profitMarginValue.grid(row=12, column=5)

    def analyze(self,event=None):
        self.getCompanyName()
        self.getCompanySector()
        self.getEPS()
        self.getPERatio()
        self.getReturnOnEquity()
        self.currentStockPrice()
        self.getDebtToEquityRatio()
        self.getProfitMargin()
        self.clearUserInputBox()

    def getCompanyName(self):
        tickerFromUser = self.getTextInput()
        companyName = anlyze.getStockName(tickerFromUser)
        self.companyNameLabelText["text"] = ""
        self.companyNameLabelText["text"] = self.companyNameLabelText["text"] + str(companyName)

    def getCompanySector(self):
        tickerFromUser = self.getTextInput()
        companySector = anlyze.getCompanySector(tickerFromUser)
        self.companySectorValue["text"] = self.companySectorDefaultValue
        self.companySectorValue["text"] = self.companySectorValue["text"] + str(companySector)

    def getEPS(self):
        tickerFromUser = self.getTextInput()
        eps = anlyze.getEPS(tickerFromUser)
        self.earningsPerShareValue["text"] = self.earningsPerShareDefaultValue
        self.earningsPerShareValue["text"] = self.earningsPerShareValue["text"]+ '$' + str(eps)

    def getPERatio(self):
        tickerFromUser = self.getTextInput()
        peRatio = anlyze.getPERatio(tickerFromUser)
        self.peRatioValue["text"] = self.peRatioLabelDefaultValue
        self.peRatioValue["text"] = self.peRatioValue["text"] + str(peRatio)



    def getReturnOnEquity(self):
        tickerFromUser = self.getTextInput()
        returnOnEquity = anlyze.getReturnOnEquity(tickerFromUser)
        self.returnOnEquityValue["text"] = self.returnOnEquityDefaultValue
        self.returnOnEquityValue["text"] = self.returnOnEquityValue["text"] + str(returnOnEquity)+ '%'

    def currentStockPrice(self):
        tickerFromUser = self.getTextInput()
        stockPrice = anlyze.getCurrentStockPrice(tickerFromUser)
        # self.currentStockPriceLabelText["text"] = self.currentStockPriceLabelText["text"] +'$'+ str(stockPrice)
        self.currentStockPriceValue["text"] = self.currentStockPriceDefaultValue
        self.currentStockPriceValue["text"] = self.currentStockPriceValue["text"] + '$' + str(
            stockPrice)

    def getDebtToEquityRatio(self):
        tickerFromUser = self.getTextInput()
        debtToEquityRatio = anlyze.getDebtToEquity(tickerFromUser)
        # self.debtToEquityRatioLabelText["text"] = self.debtToEquityRatioLabelText["text"] + str(debtToEquityRatio)
        self.debtToEquityRatioValue["text"] = self.debtToEquityRatioDefaultValue
        self.debtToEquityRatioValue["text"] = self.debtToEquityRatioValue["text"] + str(
            debtToEquityRatio)

    def getProfitMargin(self):
        tickerFromUser = self.getTextInput()
        profitMargin = anlyze.getProfitMargin(tickerFromUser)
        # self.profitMarginLabelText["text"] = self.profitMarginLabelText["text"] + str(profitMargin) +'%'
        self.profitMarginValue["text"] = self.profitMarginDefaultValue
        self.profitMarginValue["text"] = self.profitMarginValue["text"] + str(profitMargin) + '%'

    def getTextInput(self):
        result = self.textInputBox.get()
        result = result.rstrip()

        if len(result) > 0:
            results = result.upper()
            results = str(results)
            return results

        else:
            messagebox.showErrorMessage(self)

    def clearUserInputBox(self):
        self.textInputBox.delete(0, END)

    def clearValues(self):
        self.companyNameLabelText["text"] = ""
        self.companySectorLabelText["text"] = self.companySectorDefaultText
        self.earningsPerShareLabelText["text"] = self.earningsPerShareDefaultText
        self.peRatioLabelText["text"] = self.peRatioLabelDefault
        self.returnOnEquityLabelText["text"] = self.returnOnEquityDefaultText
        self.currentStockPriceLabelText["text"] = self.currentStockPriceDefaultText
        self.debtToEquityRatioLabelText["text"] = self.debtToEquityRatioDefaultText
        self.profitMarginLabelText["text"] = self.profitMarginDefaultText

        self.clearUserInputBox()
        # new method
        self.companySectorValue["text"] = self.companySectorDefaultValue
        self.earningsPerShareValue["text"] = self.earningsPerShareDefaultValue
        self.peRatioValue["text"] = self.peRatioLabelDefaultValue
        self.returnOnEquityValue["text"] = self.returnOnEquityDefaultValue
        self.currentStockPriceValue["text"] = self.currentStockPriceDefaultValue
        self.debtToEquityRatioValue["text"] = self.debtToEquityRatioDefaultValue
        self.profitMarginValue["text"] = self.profitMarginDefaultValue


#   *****   PAGES   *****
class PlotCashFlowChart(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.my_font = tkinter.font.Font(self, family="Sans Serif", size=20)
        self.pageTitle = Label(self, text="Cash Flow Charts", font=self.my_font)
        self.RadioText = StringVar()
        self.quarterlyTextString = 'q'
        self.yearlyTextString = 'a'

        self.textInputBox = Text(self, relief=tk.RIDGE, height=1, width=6, borderwidth=2)
        #self.textInputBox.focus()
        self.frequencyText = Label(self, text="Frequency")
        self.quarterlyRadioButton = Radiobutton(self, text="Quarterly", variable=self.RadioText,
                                                value=self.quarterlyTextString, command=self.selectedRadioButtonOption)
        self.yearlyRadioButton = Radiobutton(self, text="Annual", variable=self.RadioText, value=self.yearlyTextString,
                                             command=self.selectedRadioButtonOption)
        self.clearButton = Button(self, text='Clear', bg='red', command=self.clear)
        self.pageTitle.pack()
        self.textInputBox.pack()
        self.clearButton.pack()
        self.quarterlyRadioButton.pack(side='left', padx=50)
        self.yearlyRadioButton.pack(side='right', padx=50)

        # self.plotGraphButton.pack()
        button1 = Button(self, text="Back to Home",
                         command=lambda: controller.show_frame(Startpage))
        # button1.pack()

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
            messagebox.showErrorMessage(self)

    def selectedRadioButtonOption(self):
        userInput = self.getTextInput()
        radioButtonFrequencyOption = self.RadioText.get()
        if not plotCashFlow.canvas:
            plotCashFlow.plotCashGraph(self, userInput, radioButtonFrequencyOption)
        else:
            plotCashFlow.clearPlotPage()
            plotCashFlow.plotCashGraph(self, userInput, radioButtonFrequencyOption)

    def destroyGraph(self):
        plotCashFlow.clearPlotPage()

    def clearChart(self):  ## redundant
        plotCashFlow.clearPlotPage()

    def clear(self):
        self.textInputBox.delete("1.0", "end")
        plotCashFlow.clearPlotPage()
        self.yearlyRadioButton.deselect()
        self.quarterlyRadioButton.deselect()
        self.textInputBox.focus()

class PlotIncomeStatementChart(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.my_font = tkinter.font.Font(self, family="Sans Serif", size=20)
        self.pageTitle = Label(self, text="Net Income Charts", font=self.my_font)
        self.RadioText = StringVar()
        self.quarterlyTextString = 'q'
        self.yearlyTextString = 'a'

        self.textInputBox = Text(self, relief=tk.RIDGE, height=1, width=6, borderwidth=2)
        self.textInputBox.focus()
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
                         command=lambda: controller.show_frame(Startpage))

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
            messagebox.showErrorMessage(self)

    def selectedRadioButtonOption(self):
        userInput = self.getTextInput()
        radioButtonFrequencyOption = self.RadioText.get()
        if not plotIncome.canvas:
            plotIncome.netIncomeChart(self, userInput, radioButtonFrequencyOption)
        else:
            plotIncome.clearPlotPage()
            plotIncome.netIncomeChart(self, userInput, radioButtonFrequencyOption)

    def destroyGraph(self):
        plotIncome.clearPlotPage()

    def clear(self):
        self.textInputBox.delete("1.0", "end")
        plotIncome.clearPlotPage()
        self.yearlyRadioButton.deselect()
        self.quarterlyRadioButton.deselect()


class plotEarningsChart(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.my_font = tkinter.font.Font(self, family="Sans Serif", size=20)
        self.pageTitle = Label(self, text="Earnings Charts", font=self.my_font)
        self.RadioText = StringVar()
        self.quarterlyTextString = 'quarterly'
        self.yearlyTextString = 'yearly'

        self.textInputBox = Text(self, relief=tk.RIDGE, height=1, width=6, borderwidth=2)
        self.frequencyText = Label(self, text="Frequency")
        self.quarterlyRadioButton = Radiobutton(self, text="Quarterly", variable=self.RadioText,
                                                value=self.quarterlyTextString, command=self.selectedRadioButtonOption)
        self.yearlyRadioButton = Radiobutton(self, text="Annual", variable=self.RadioText, value=self.yearlyTextString,
                                             command=self.selectedRadioButtonOption)

        # self.plotGraphButton = tk.Button(self, text='plot Income Statement', command=self.incomeStatementChart)

        self.clearButton = Button(self, text='Clear', command=self.clear, bg='red')
        self.pageTitle.pack()
        self.textInputBox.pack()
        self.quarterlyRadioButton.pack(side='left', padx=50)
        self.yearlyRadioButton.pack(side='right', padx=50)
        self.clearButton.pack()
        button1 = Button(self, text="Back to Home",
                         command=lambda: controller.show_frame(Startpage))
        # button1.pack()

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
            messagebox.showErrorMessage(self)

    def selectedRadioButtonOption(self):
        userInput = self.getTextInput()
        # startPageObject = self.controller.get_page(Startpage)
        # userInputFromStartPage = startPageObject.getTextInput()
        # print(userInputFromStartPage)
        # radioButtonFrequencyOption = self.RadioText.set(self.yearlyTextString)
        radioButtonFrequencyOption = self.RadioText.get()
        if not plotEarnings.canvas:
            plotEarnings.plotEarnings(self, userInput, radioButtonFrequencyOption)
        else:
            plotEarnings.clearPlotPage()
            plotEarnings.plotEarnings(self, userInput, radioButtonFrequencyOption)

    def destroyGraph(self):
        plotEarnings.clearPlotPage()

    def clear(self):
        self.textInputBox.delete("1.0", "end")
        plotEarnings.clearPlotPage()
        self.yearlyRadioButton.deselect()
        self.quarterlyRadioButton.deselect()

app = UserInterFace()
plotCashFlow = pltCashFlow.PlotGraph()
plotIncome = pltIncome.PlotGraph()
plotEarnings = pltEarnings.PlotGraph()

app.geometry("1300x600")
app.mainloop()
