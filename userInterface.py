from Financials import analyze as anlyze
from helpers import plotChart as plot

from tkinter import *


class Application(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master.title("Stock Analyzer")
        self.stockSymbolText = Label(root, text="Enter Stock Symbol: ")
        self.textInputBox = Text(root, relief=RIDGE, height=1, width = 6, borderwidth=2)
        self.analyzeButton = Button(root,
                                       text='Analyze Stock', relief=RIDGE,
                                       command=lambda: [self.getCompanyName(),self.getEPS(), self.getPERatio(), self.getReturnOnEquity(),
                                                        self.currentStockPrice(), self.getDebtToEquityRatio(),
                                                        self.getProfitMargin()])
        self.clearButton = Button(root,text="Clear",relief = RIDGE,command=self.clearValues)
        self.graphCashFlowButton = Button(root, text="See Cash Flow Graph",command=self.plotCashFlowGraph)


        self.earningsPerShareLabelText = Label(root, text="Earnings Per Share:")
        self.peRatioLabelText = Label(root, text="PE Ratio:")
        self.returnOnEquityLabelText = Label(root, text="Return on Equity Ratio:")
        self.currentStockPriceLabelText = Label(root, text="Current Stock Price:")
        self.debtToEquityRatioLabelText = Label(root, text="Debt to Equity Ratio:")
        self.profitMarginLabelText = Label(root, text="Profit Margin")
        self.CompanyNameLabelText = Label(root,text="")


        self.earningsPerShareLabelDefault = "Earnings Per Share: "
        self.companyNameLabelDefault = ""
        self.peRatioLabelDefault = "PE Ratio: "
        self.returnOnEquityLabelDefault = "Return on Equity Ratio: "
        self.currentStockPriceLabelDefault = "Current Stock Price: "
        self.debtToEquityRatioLabelDefault = "Debt to Equity Ratio: "
        self.profitMarginLabelDefault = "Profit Margin: "
        self.noInputText = "Enter a value"


        self.stockSymbolText.grid(row=0, column=1,columnspan=2)
        self.textInputBox.grid(row=1, column=2)
        self.analyzeButton.grid(row=3, column=2, pady=4)
        self.clearButton.grid(row=3, column=3, ipadx=10)
        self.graphCashFlowButton.grid(row=3, column=4, ipadx=10)

        self.CompanyNameLabelText.grid(row=5, column=2)
        self.earningsPerShareLabelText.grid(row=6, column=2)
        self.peRatioLabelText.grid(row=7, column=2)
        self.returnOnEquityLabelText.grid(row=8, column=2)
        self.currentStockPriceLabelText.grid(row=9, column=2)
        self.debtToEquityRatioLabelText.grid(row=10, column=2)
        self.profitMarginLabelText.grid(row=11, column=2)


    def getTextInput(self):
        result = self.textInputBox.get("1.0", "end")
        results = result.upper()
        results = results.rstrip()
        return results

    def getStockInfo(self):
        userInput = self.getTextInput()

        if len(userInput) == 0:
            anlyze.analyzeStock(userInput)
        else:
            print("enter some valid shit")

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
        peRatio = anlyze.getCurrentStockPrice(tickerFromUser)
        self.currentStockPriceLabelText["text"] = self.currentStockPriceLabelText["text"] + str(peRatio)

    def getDebtToEquityRatio(self):
        tickerFromUser = self.getTextInput()
        debtToEquityRatio = anlyze.getDebtToEquity(tickerFromUser)
        self.debtToEquityRatioLabelText["text"] = self.debtToEquityRatioLabelText["text"] + str(debtToEquityRatio)

    def getProfitMargin(self):
        tickerFromUser = self.getTextInput()
        profitMargin = anlyze.getProfitMargin(tickerFromUser)
        self.profitMarginLabelText["text"] = self.profitMarginLabelText["text"] + str(profitMargin)



    def plotCashFlowGraph(self):
        userInput = self.getTextInput()
        anlyze.graphFreeCashFlow(userInput)

    def destroyGraph(self):
        plot.killGraph()

    def clearValues(self):
        self.earningsPerShareLabelText["text"] = self.earningsPerShareLabelDefault
        self.peRatioLabelText["text"] = self.peRatioLabelDefault
        self.returnOnEquityLabelText["text"] = self.returnOnEquityLabelDefault
        self.currentStockPriceLabelText["text"] = self.currentStockPriceLabelDefault
        self.debtToEquityRatioLabelText["text"] = self.debtToEquityRatioLabelDefault
        self.profitMarginLabelText["text"] = self.profitMarginLabelDefault
        self.CompanyNameLabelText["text"] = self.companyNameLabelDefault
        self.textInputBox.delete("1.0", "end")
        self.destroyGraph()


root = Tk()
root.geometry("400x300")
app = Application(root).grid()
root.mainloop()