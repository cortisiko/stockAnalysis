from Financials import analyze as anlyze
from helpers import plotChart as plot
from tkinter import *
import tkinter.font

class Application(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master.title("Stock Analyzer")
        self.my_font = tkinter.font.Font(root, family="Comic Sans MS",size=20)
        self.stockSymbolText = Label(root, text="Enter Stock Symbol: ")
        self.textInputBox = Text(root, relief=RIDGE, height=1, width = 10, borderwidth=4)
        self.analyzeButton = Button(root,
                                       text='Analyze Stock', relief=RIDGE,
                                       command=lambda: [self.getCompanyName(),self.getEPS(), self.getPERatio(), self.getReturnOnEquity(),
                                                        self.currentStockPrice(), self.getDebtToEquityRatio(),
                                                        self.getProfitMargin()])
        self.clearButton = Button(root,text="Clear",relief = RIDGE,command=self.clearValues)
        self.graphCashFlowButton = Button(root, text="See Cash Flow Graph",command=self.plotCashFlowGraph)

        self.earningsPerShareLabelText = Label(root, text="Earnings Per Share: ")
        self.peRatioLabelText = Label(root, text="PE Ratio: ")
        self.returnOnEquityLabelText = Label(root, text="Return on Equity Ratio: ")
        self.currentStockPriceLabelText = Label(root, text="Current Stock Price: ")
        self.debtToEquityRatioLabelText = Label(root, text="Debt to Equity Ratio: ")
        self.profitMarginLabelText = Label(root, text="Profit Margin: ")
        self.CompanyNameLabelText = Label(root,text="",font=self.my_font)

        self.earningsPerShareLabelDefault = "Earnings Per Share: "
        self.companyNameLabelDefault = ""
        self.peRatioLabelDefault = "PE Ratio: "
        self.returnOnEquityLabelDefault = "Return on Equity Ratio: "
        self.currentStockPriceLabelDefault = "Current Stock Price: "
        self.debtToEquityRatioLabelDefault = "Debt to Equity Ratio: "
        self.profitMarginLabelDefault = "Profit Margin: "
        self.noInputText = "Enter something int"


        self.stockSymbolText.grid(row=0, column=3)
        self.textInputBox.grid(row=0, column=4,sticky="nsew")
        self.analyzeButton.grid(row=3, column=3, pady=4,sticky="nsew")
        self.clearButton.grid(row=3, column=4, ipadx=10)
        self.graphCashFlowButton.grid(row=3, column=5, ipadx=10)

        self.CompanyNameLabelText.grid(row=5, column=4)
        self.currentStockPriceLabelText.grid(row=6, column=4)
        self.earningsPerShareLabelText.grid(row=7, column=4)
        self.peRatioLabelText.grid(row=8, column=4)
        self.returnOnEquityLabelText.grid(row=9, column=4)
        self.debtToEquityRatioLabelText.grid(row=10, column=4)
        self.profitMarginLabelText.grid(row=11, column=4)


    def getTextInput(self):
        result = self.textInputBox.get("1.0", "end")
        results = result.upper()
        results = results.rstrip()
        return results

    def getStockInfo(self):
        userInput = self.getTextInput()

        return userInput

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
        currentPrice = anlyze.getCurrentStockPrice(tickerFromUser)
        self.currentStockPriceLabelText["text"] = self.currentStockPriceLabelText["text"] +'$'+ str(currentPrice)

    def getDebtToEquityRatio(self):
        tickerFromUser = self.getTextInput()
        debtToEquityRatio = anlyze.getDebtToEquity(tickerFromUser)
        self.debtToEquityRatioLabelText["text"] = self.debtToEquityRatioLabelText["text"] + str(debtToEquityRatio)

    def getProfitMargin(self):
        tickerFromUser = self.getTextInput()
        profitMargin = anlyze.getProfitMargin(tickerFromUser)
        self.profitMarginLabelText["text"] = self.profitMarginLabelText["text"] + str(profitMargin) +'%'



    def plotCashFlowGraph(self):
        userInput = self.getTextInput()
        anlyze.graphFreeCashFlow(userInput,root)

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
root.geometry("780x500")
root.iconbitmap('stockx.ico')
app = Application(root).grid()
root.mainloop()