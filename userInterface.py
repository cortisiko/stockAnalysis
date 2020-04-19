from tkinter import *
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
        self.label = tk.Label(self.root, text="Stock Symbol: ")
        self.label.pack(side="top")
        self.textInputBox = tk.Text(self.root, relief=RIDGE, height=1, width = 6, borderwidth=2)
        self.analyzeButton = tk.Button(self.root,
                                text='Analyze',relief=RIDGE,
                                command=lambda: [self.getEPS(), self.getPERatio(), self.getReturnOnEquity(),
                                                 self.currentStockPrice(), self.getDebtToEquityRatio(),
                                                 self.getProfitMargin()])

        #self.label = tk.Label(self.root, text="This will be cleared.")
        self.clearButton = tk.Button(self.root, text="Clear",
                           command=lambda: self.clear_widget())

        self.textInputBox.pack()
        self.analyzeButton.pack()
        self.clearButton.pack()

        self.labelA = tk.Label(self.root, text="Earnings Per Share:")
        self.labelB = tk.Label(self.root, text="PE Ratio:")
        self.labelC = tk.Label(self.root, text="Return on Equity Ratio:")
        self.labelD = tk.Label(self.root, text="Current Stock Price:")
        self.labelE = tk.Label(self.root, text="Debt to Equity Ratio:")
        self.labelF = tk.Label(self.root, text="Profit Margin")

        self.labelA.pack()
        self.labelB.pack()
        self.labelC.pack()
        self.labelD.pack()
        self.labelE.pack()
        self.labelF.pack()
        self.root.iconbitmap("stockx.ico")
        self.root.mainloop()

    def getEPS(self):
        tickerFromUser = self.getTextInput()
        eps = anlyze.getEPS(tickerFromUser)

        self.labelA["text"] = self.labelA["text"] + str(eps)

    def getPERatio(self):
        tickerFromUser = self.getTextInput()
        peRatio = anlyze.getPERatio(tickerFromUser)

        self.labelB["text"] = self.labelB["text"] + str(peRatio)

    def getReturnOnEquity(self):
        tickerFromUser = self.getTextInput()
        returnOnEquity = anlyze.getReturnOnEquity(tickerFromUser)
        self.labelC["text"] = self.labelC["text"] + str(returnOnEquity)

    def currentStockPrice(self):
        tickerFromUser = self.getTextInput()
        peRatio = anlyze.getCurrentStockPrice(tickerFromUser)
        self.labelD["text"] = self.labelD["text"] + str(peRatio)

    def getDebtToEquityRatio(self):
        tickerFromUser = self.getTextInput()
        debtToEquityRatio = anlyze.getDebtToEquity(tickerFromUser)
        self.labelE["text"] = self.labelE["text"] + str(debtToEquityRatio)

    def getProfitMargin(self):
        tickerFromUser = self.getTextInput()
        profitMargin = anlyze.getProfitMargin(tickerFromUser)
        self.labelF["text"] = self.labelF["text"] + str(profitMargin)

    def getTextInput(self):
        result = self.textInputBox.get("1.0", "end")
        results = result.upper()
        results = results.rstrip()
        return results

    def getStockInfo(self):
        userInput = self.getTextInput()
        anlyze.analyzeStock(userInput)

    def clear_widget(widget):
        widget.destroy()


app = UserInterface()
