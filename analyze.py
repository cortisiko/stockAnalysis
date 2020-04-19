import self as self
from click._compat import raw_input

from Financials import cashFlowSheet as cashFlowPage
from Financials import statistics as statisticsTab
from Financials import summary as summaryPage
from Financials import incomeStatementSheet as income
from helpers import Ticker as ticker
from helpers import plotChart as plot
from helpers import getDate as date
from tkinter import *
from PIL import ImageTk,Image

#starting new GUI window
window = Tk()
window.title("Stock Anlaysis App")


b1 = Button()

#canvas1 = Canvas(window, width=400, height=300)
#canvas1.pack()

l1 = Label(window, text="Enter Stock Symbol:").grid(row=0)
e1 = Entry(window)
e1.grid(row=0, column=2)
#canvas1.create_window(200, 140, window=11)

Frequency = 'a'

def clearForm():
    #e1.destroy()
    #b1.destroy()
    e1 = Entry(window)
    e1.grid(row=0, column=2)
    l1 = Label(window, text="               ", fg="white", bg="white", font="Helvetica 14 bold italic")
    l1.grid(row=1, column=2)

    # Space Padding
   # l1 = Label(window, text="")
   # l1.grid(row=2, column=0)
    # Space Padding

    l1 = Label(window, text="                ", fg="white", bg="white", font="Helvetica 14 bold italic")
    l1.grid(row=3, column=2)

    l1 = Label(window, text="                ", fg="white", bg="white", font="Helvetica 14 bold italic")
    l1.grid(row=4, column=2)

    l1 = Label(window, text="                ", fg="white", bg="white", font="Helvetica 14 bold italic")
    l1.grid(row=5, column=2)

    l1 = Label(window, text="                ", fg="white", bg="white", font="Helvetica 14 bold italic")
    l1.grid(row=6, column=2)

    l1 = Label(window, text="                ", fg="white", bg="white", font="Helvetica 14 bold italic")
    l1.grid(row=7, column=2)

def analyzeStock ():
    tickerSymbol = e1.get()
    tickerSymbol = tickerSymbol.upper()
    tickerObject = ticker.getTicker(tickerSymbol)  ## Gets the ticker object so you can access the various objects
    cashFlowDataFrame = cashFlowPage.getCashFlowData(tickerObject, Frequency)
    incomeStatementDataFrame = income.getIncomeStatements(tickerObject, Frequency)
    freeCashFlow = cashFlowPage.getFreeCashFlow(cashFlowDataFrame)
    netIncome = income.getNetIncome(incomeStatementDataFrame)
    dates = date.getDates(cashFlowDataFrame)
    #### Fundamentals ###
    debtToEquityRatio = statisticsTab.getDebtToEquity(tickerObject,tickerSymbol)
    returnOnEquity = statisticsTab.getReturnOnEquity(tickerObject,tickerSymbol)
    profitMargin = statisticsTab.getProfitMargins(tickerObject,tickerSymbol)

    eps = summaryPage.getEarningsPerShare(tickerObject,tickerSymbol)
    currentStockPrice = statisticsTab.getCurrentStockPrice(tickerObject,tickerSymbol)
    peRatio = summaryPage.getPERatio(eps,currentStockPrice)
    print("The symbol you entered is: ",tickerSymbol)

    # COLUMN 2
    l1 = Label(window, text=tickerSymbol, fg="light green", bg="dark green", font="Helvetica 14 bold italic")
    l1.grid(row=1, column=2)
    labels.append(l1)

    # Space Padding
    l1 = Label(window, text="")
    l1.grid(row=2, column=0)
    # Space Padding

    l1 = Label(window, text=eps, fg="light green", bg="dark green", font="Helvetica 14 bold italic")
    l1.grid(row=3, column=2)
    labels.append(l1)

    l1 = Label(window, text = peRatio, fg="light green", bg="dark green", font="Helvetica 14 bold italic")
    l1.grid(row=4, column=2)
    labels.append(l1)

    l1 = Label(window, text=debtToEquityRatio, fg="light green", bg="dark green", font="Helvetica 14 bold italic")
    l1.grid(row=5, column=2)
    labels.append(l1)

    l1 = Label(window, text=returnOnEquity, fg="light green", bg="dark green", font="Helvetica 14 bold italic")
    l1.grid(row=6, column=2)
    labels.append(l1)

    l1 = Label(window, text=profitMargin, fg="light green", bg="dark green", font="Helvetica 14 bold italic")
    l1.grid(row=7, column=2)
    labels.append(l1)

    def graphFreeCashFlow():
        cashFlowGraphTitle = 'Free cash flow'
        plot.plotGraph(dates, freeCashFlow, tickerSymbol, cashFlowGraphTitle)  ## plotting free cash flow

    b1 = Button(window, text='Graph Free Cash Flow', command=graphFreeCashFlow).grid(row=10,
                                                         column=2,
                                                         sticky=W,
                                                         pady=4)


Button(window, text='Analyze Stock', command=analyzeStock).grid(row=0,
                                                               column=4,
                                                               sticky=W,
                                                               pady=4)

Button(window, text='CLEAR', command=clearForm).grid(row=10,
                                                               column=4,
                                                               sticky=W,
                                                               pady=4)


## Plotting graphs
#cashFlowGraphTitle = 'Free cash flow'
#plot.plotGraph(date,freeCashFlow,tickerSymbol,cashFlowGraphTitle) ## plotting free cash flow

#netIncomeGraphTitle = 'Net Income'
#plot.plotGraph(date,netIncome,tickerSymbol,netIncomeGraphTitle) ## plotting net income
# code to build GUI

# column 0

l1 = Label(window, text="Stock Symbol:", fg="blue", bg="yellow", font="Helvetica 14 bold")
l1.grid(row=1, column=0)

# Space Padding

l1 = Label(window, text="")
l1.grid(row=2, column=0)
# Space Padding

l1 = Label(window, text="Earnings Per Share:", fg="blue", bg="yellow", font="Helvetica 14 bold")
l1.grid(row=3, column=0)

l1 = Label(window, text="PE Ratio:", fg="blue", bg="yellow", font="Helvetica 14 bold")
l1.grid(row=4, column=0)

l1 = Label(window, text="MRQ to Equity Ratio:", fg="blue", bg="yellow", font="Helvetica 14 bold")
l1.grid(row=5, column=0)

l1 = Label(window, text="Return On Equity Ratio:", fg="blue", bg="yellow", font="Helvetica 14 bold")
l1.grid(row=6, column=0)

l1 = Label(window, text="Net Profit Margin:", fg="blue", bg="yellow", font="Helvetica 14 bold")
l1.grid(row=7, column=0)


# adding image
#stockphoto = Image.open("stockgif.gif")
#photoimg=ImageTk.PhotoImage(stockphoto)
#l1 = Label(window, justify=LEFT,compound = LEFT,padx = 10,  image=photoimg)
#l1.grid(row=12, column=2)


window.mainloop()