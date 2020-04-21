import analyze as anlyze

try:
    import Tkinter as tk
except:
    import tkinter as tk


class UserInterface():
    def __init__(self):
        self.root = tk.Tk()
        self.windowTitle = self.root.title("Stock Analyzer")
        self.root.geometry('600x240')
        self.stockSymbolText = tk.Label(self.root, text="Stock Symbol: ")
        self.stockSymbolText.pack(side="top")
        self.textInputBox = tk.Text(self.root, relief=tk.RIDGE, height=1, width = 6, borderwidth=2)
        self.analyzeButton = tk.Button(self.root,
                                text='Analyze Stock',relief=tk.RIDGE,
                                command=lambda: [self.getEPS(), self.getPERatio(), self.getReturnOnEquity(),
                                                 self.currentStockPrice(), self.getDebtToEquityRatio(),
                                                 self.getProfitMargin()])

        #self.label = tk.Label(self.root, text="This will be cleared.")
        self.clearButton = tk.Button(self.root, text="Clear", command=self.clearValues)

        self.textInputBox.pack()
        self.analyzeButton.pack()
        self.clearButton.pack()

        self.earningsPerShareLabelText = tk.Label(self.root, text="Earnings Per Share:")
        self.peRatioLabelText = tk.Label(self.root, text="PE Ratio:")
        self.returnOnEquityLabelText = tk.Label(self.root, text="Return on Equity Ratio:")
        self.currentStockPriceLabelText = tk.Label(self.root, text="Current Stock Price:")
        self.debtToEquityRatioLabelText = tk.Label(self.root, text="Debt to Equity Ratio:")
        self.profitMarginLabelText = tk.Label(self.root, text="Profit Margin")

        self.earningsPerShareLabelDefault = "Earnings Per Share:"
        self.peRatioLabelDefault = "PE Ratio:"
        self.returnOnEquityLabelDefault = "Return on Equity Ratio:"
        self.currentStockPriceLabelDefault = "Current Stock Price:"
        self.debtToEquityRatioLabelDefault = "Debt to Equity Ratio:"
        self.profitMarginLabelDefault = "Profit Margin:"

        self.earningsPerShareLabelText.pack()
        self.peRatioLabelText.pack()
        self.returnOnEquityLabelText.pack()
        self.currentStockPriceLabelText.pack()
        self.debtToEquityRatioLabelText.pack()
        self.profitMarginLabelText.pack()
        self.root.iconbitmap("stockx.ico")
        self.root.mainloop()

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

    def getTextInput(self):
        result = self.textInputBox.get("1.0", "end")
        results = result.upper()
        results = results.rstrip()
        return results

    def getStockInfo(self):
        userInput = self.getTextInput()
        anlyze.analyzeStock(userInput)

    def clearValues(self):
        self.earningsPerShareLabelText["text"]  = self.earningsPerShareLabelDefault
        self.peRatioLabelText["text"]           = self.peRatioLabelDefault
        self.returnOnEquityLabelText["text"]    = self.returnOnEquityLabelDefault
        self.currentStockPriceLabelText["text"] = self.currentStockPriceLabelDefault
        self.debtToEquityRatioLabelText["text"] = self.debtToEquityRatioLabelDefault
        self.profitMarginLabelText["text"]      = self.profitMarginLabelDefault
        self.textInputBox.delete("1.0", "end")

app = UserInterface()
