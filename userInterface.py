try:
    import Tkinter as tk
except:
    import tkinter as tk
from charts import plotCashFlow as pltCashFlow, plotIncome as pltIncome, plotEarnings as pltEarnings
import tkinter.font
from Financials import analyze as anlyze
from tkinter import *
from tkinter import messagebox as messageBox


class UserInterFace(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        container = tk.Frame(self)
        self.windowTitle = self.title("Stock Analyzer")

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
        Charts.add_command(label="Income Statement", command=lambda: self.show_frame(PlotIncomeStatementChart))
        Charts.add_command(label="Earnings", command=lambda: self.show_frame(plotEarningsChart))


        menu.add_separator()
        tk.Tk.config(self, menu=menu)

        for F in (Startpage,PlotCashFlowChart,PlotIncomeStatementChart,plotEarningsChart):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(Startpage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()


class Startpage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.my_font = tkinter.font.Font(self, family="Comic Sans MS",size=20)
        self.stockSymbolText = Label(self, text="Enter Stock Symbol: ")
        self.textInputBox = Text(self, relief=RIDGE, height=1, width = 10, borderwidth=4)
        self.analyzeButton = Button(self,
                                       text='Analyze Stock', relief=RIDGE,
                                       command=self.combineFunc(self.getCompanyName,self.getEPS, self.getPERatio, self.getReturnOnEquity,
                                                        self.currentStockPrice, self.getDebtToEquityRatio,
                                                        self.getProfitMargin))
        self.clearButton = Button(self,text="Clear",relief = RIDGE,command=self.clearValues)
        #self.graphCashFlowButton = Button(self, text="See Cash Flow Graph",command=lambda: controller.show_frame(PlotCashFlowChart))

        self.earningsPerShareLabelText = Label(self, text="Earnings Per Share: ")
        self.peRatioLabelText = Label(self, text="PE Ratio: ")
        self.returnOnEquityLabelText = Label(self, text="Return on Equity Ratio: ")
        self.currentStockPriceLabelText = Label(self, text="Current Stock Price: ")
        self.debtToEquityRatioLabelText = Label(self, text="Debt to Equity Ratio: ")
        self.profitMarginLabelText = Label(self, text="Profit Margin: ")
        self.CompanyNameLabelText = Label(self,text="",font=self.my_font)

        self.earningsPerShareLabelDefault = "Earnings Per Share: "
        self.companyNameLabelDefault = ""
        self.peRatioLabelDefault = "PE Ratio: "
        self.returnOnEquityLabelDefault = "Return on Equity Ratio: "
        self.currentStockPriceLabelDefault = "Current Stock Price: "
        self.debtToEquityRatioLabelDefault = "Debt to Equity Ratio: "
        self.profitMarginLabelDefault = "Profit Margin: "

        self.stockSymbolText.grid(row=0, column=3)
        self.textInputBox.grid(row=0, column=4,sticky="nsew")
        self.analyzeButton.grid(row=3, column=3, pady=4,sticky="nsew")
        self.clearButton.grid(row=3, column=4, ipadx=10)
        #self.graphCashFlowButton.grid(row=3, column=5, ipadx=10)

        self.CompanyNameLabelText.grid(row=5, column=4)
        self.currentStockPriceLabelText.grid(row=6, column=4)
        self.earningsPerShareLabelText.grid(row=7, column=4)
        self.peRatioLabelText.grid(row=8, column=4)
        self.returnOnEquityLabelText.grid(row=9, column=4)
        self.debtToEquityRatioLabelText.grid(row=10, column=4)
        self.profitMarginLabelText.grid(row=11, column=4)

    def getCompanyName(self):
        tickerFromUser = self.getTextInput()
        companyName = anlyze.getStockName(tickerFromUser)
        self.CompanyNameLabelText["text"] = self.CompanyNameLabelText["text"] + str(companyName)

    def getEPS(self):
        tickerFromUser = self.getTextInput()
        eps = anlyze.getEPS(tickerFromUser)

        self.earningsPerShareLabelText["text"] = self.earningsPerShareLabelText["text"] + str(eps)

    def getPERatio(self):
        tickerFromUser = self.getTextInput()
        peRatio = anlyze.getPERatio(tickerFromUser)

        self.peRatioLabelText["text"] = self.peRatioLabelText["text"] + str(peRatio)

    def getReturnOnEquity(self):
        tickerFromUser = self.getTextInput()
        returnOnEquity = anlyze.getReturnOnEquity(tickerFromUser)
        self.returnOnEquityLabelText["text"] = self.returnOnEquityLabelText["text"] + str(returnOnEquity)

    def currentStockPrice(self):
        tickerFromUser = self.getTextInput()
        stockPrice = anlyze.getCurrentStockPrice(tickerFromUser)
        self.currentStockPriceLabelText["text"] = self.currentStockPriceLabelText["text"] +'$'+ str(stockPrice)

    def getDebtToEquityRatio(self):
        tickerFromUser = self.getTextInput()
        debtToEquityRatio = anlyze.getDebtToEquity(tickerFromUser)
        self.debtToEquityRatioLabelText["text"] = self.debtToEquityRatioLabelText["text"] + str(debtToEquityRatio)

    def getProfitMargin(self):
        tickerFromUser = self.getTextInput()
        profitMargin = anlyze.getProfitMargin(tickerFromUser)
        self.profitMarginLabelText["text"] = self.profitMarginLabelText["text"] + str(profitMargin) +'%'

    def getTextInput(self):
        result = self.textInputBox.get("1.0", "end")
        result = result.rstrip()
        if len(result) > 0:
            results = result.upper()
            results = str(results)
            return results

        else:
            self.showErrorMessage()

    def clearValues(self):
        self.CompanyNameLabelText["text"]  = ""
        self.earningsPerShareLabelText["text"]  = self.earningsPerShareLabelDefault
        self.peRatioLabelText["text"]           = self.peRatioLabelDefault
        self.returnOnEquityLabelText["text"]    = self.returnOnEquityLabelDefault
        self.currentStockPriceLabelText["text"] = self.currentStockPriceLabelDefault
        self.debtToEquityRatioLabelText["text"] = self.debtToEquityRatioLabelDefault
        self.profitMarginLabelText["text"]      = self.profitMarginLabelDefault
        self.textInputBox.delete("1.0", "end")


    def combineFunc(self, *funcs):

        def combinedFunc(*args, **kwargs):
            for f in funcs:
                f(*args, **kwargs)

        return combinedFunc

    def showErrorMessage(self):

        messageBox.showerror("Error", "Sorry, you need to enter a ticker symbol")

#   *****   PAGES   *****

class PlotCashFlowChart(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.my_font = tkinter.font.Font(self, family="Sans Serif",size=20)
        self.pageTitle = Label(self, text="Cash Flow Page",font=self.my_font)
        self.RadioText = StringVar()
        self.quarterlyTextString = 'q'
        self.yearlyTextString = 'a'

        self.textInputBox = tk.Text(self, relief=tk.RIDGE, height=1, width=6, borderwidth=2)
        self.frequencyText = tk.Label(self, text="Frequency")
        self.quarterlyRadioButton = Radiobutton(self, text="Quarterly",variable=self.RadioText, value=self.quarterlyTextString,command=self.selectedRadioButtonOption)
        self.yearlyRadioButton = Radiobutton(self, text="Annual", variable=self.RadioText, value=self.yearlyTextString,command=self.selectedRadioButtonOption)

        self.plotGraphButton = tk.Button(self, text='plot cash Flow Graph', command=self.plotCashFlowGraph)

        self.clearButton = tk.Button(self, text='Clear', command=self.clear)

        self.pageTitle.pack()
        self.textInputBox.pack()
        self.quarterlyRadioButton.pack()
        self.yearlyRadioButton.pack()
        self.clearButton.pack()
        #self.plotGraphButton.pack()

        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(Startpage))
        #button1.pack()

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
            messageBox.showerror("Error", "Sorry, you need to enter a ticker symbol")

    def selectedRadioButtonOption(self):
        userInput = self.getTextInput()
        radioButtonFrequencyOption = self.RadioText.get()
        plotCashFlow.plotCashGraph(self, userInput,radioButtonFrequencyOption)

    def destroyGraph(self):
        plotCashFlow.clearPlotPage()

    def clearChart(self): ## redundant
        plotCashFlow.clearPlotPage()

    def clear(self):
        self.textInputBox.delete("1.0", "end")
        plotCashFlow.clearPlotPage()
        self.yearlyRadioButton.deselect()
        self.quarterlyRadioButton.deselect()

     ## no need for this puppy. keeping for now
    def plotCashFlowGraph(self):
        userInput = self.getTextInput()
        plotCashFlow.plotCashGraph(self, userInput)


class PlotIncomeStatementChart(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.my_font = tkinter.font.Font(self, family="Sans Serif", size=20)
        self.pageTitle = Label(self, text="Income Statement Page", font=self.my_font)
        self.RadioText = StringVar()
        self.quarterlyTextString = 'q'
        self.yearlyTextString = 'a'

        self.textInputBox = tk.Text(self, relief=tk.RIDGE, height=1, width=6, borderwidth=2)
        self.frequencyText = tk.Label(self, text="Frequency")
        self.quarterlyRadioButton = Radiobutton(self, text="Quarterly",variable=self.RadioText, value=self.quarterlyTextString,command=self.selectedRadioButtonOption)
        self.yearlyRadioButton = Radiobutton(self, text="Annual", variable=self.RadioText, value=self.yearlyTextString,command=self.selectedRadioButtonOption)

        #self.plotGraphButton = tk.Button(self, text='plot Income Statement', command=self.incomeStatementChart)

        self.clearButton = tk.Button(self, text='Clear', command=self.clear)

        self.pageTitle.pack()
        self.textInputBox.pack()
        self.quarterlyRadioButton.pack()
        self.yearlyRadioButton.pack()
        self.clearButton.pack()

        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(Startpage))
        #button1.pack()

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
            messageBox.showerror("Error", "Sorry, you need to enter a ticker symbol")

    def selectedRadioButtonOption(self):
        userInput = self.getTextInput()
        radioButtonFrequencyOption = self.RadioText.get()
        plotIncome.incomeStatementChart(self, userInput,radioButtonFrequencyOption)

    def destroyGraph(self):
        plotIncome.clearPlotPage()

    def clearChart(self): ## redundant
        plotIncome.clearPlotPage()

    def clear(self):
        self.textInputBox.delete("1.0", "end")
        plotIncome.clearPlotPage()
        self.yearlyRadioButton.deselect()
        self.quarterlyRadioButton.deselect()

class plotEarningsChart(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.my_font = tkinter.font.Font(self, family="Sans Serif", size=20)
        self.pageTitle = Label(self, text="Earnings Page", font=self.my_font)
        self.RadioText = StringVar()
        self.quarterlyTextString = 'quarterly'
        self.yearlyTextString = 'yearly'

        self.textInputBox = tk.Text(self, relief=tk.RIDGE, height=1, width=6, borderwidth=2)
        self.frequencyText = tk.Label(self, text="Frequency")
        self.quarterlyRadioButton = Radiobutton(self, text="Quarterly",variable=self.RadioText, value=self.quarterlyTextString,command=self.selectedRadioButtonOption)
        self.yearlyRadioButton = Radiobutton(self, text="Annual", variable=self.RadioText, value=self.yearlyTextString,command=self.selectedRadioButtonOption)

        #self.plotGraphButton = tk.Button(self, text='plot Income Statement', command=self.incomeStatementChart)

        self.clearButton = tk.Button(self, text='Clear', command=self.clear)

        self.pageTitle.pack()
        self.textInputBox.pack()
        self.yearlyRadioButton.pack()
        self.quarterlyRadioButton.pack()
        self.clearButton.pack()

        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(Startpage))
        #button1.pack()

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
            messageBox.showerror("Error", "Sorry, you need to enter a ticker symbol")

    def selectedRadioButtonOption(self):
        userInput = self.getTextInput()
        radioButtonFrequencyOption = self.RadioText.get()
        plotEarnings.plotEarnings(self, userInput,radioButtonFrequencyOption)

    def destroyGraph(self):
        plotEarnings.clearPlotPage()

    def clearChart(self): ## redundant
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

app.geometry("1200x600")
app.mainloop()