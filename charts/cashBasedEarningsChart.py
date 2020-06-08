import matplotlib
matplotlib.use("TkAgg")
import pandas as pd
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from Financials import price as priceData
from Financials import earnings as earning
from helpers import Ticker as ticker
from Financials import incomeStatementSheet as income
from Financials import cashFlowSheet as cashFlowPage
from helpers import getDate as date

class PlotGraph:
    def __init__(self):
        self.canvas = None
        self.fig = Figure(figsize=(12, 5), dpi=80)

    def plotCashToEarnings(self, container,tickerSymbol,Frequency):
        tickerObject = ticker.getTicker(tickerSymbol)  ## Gets the ticker object so you can access the various objects
        incomeStatementsDataFrame = income.getIncomeStatements(tickerObject, Frequency)
        netIncome = income.getNetIncome(incomeStatementsDataFrame)
        cashFlowDataFrame = cashFlowPage.getCashFlowData(tickerObject, Frequency)
        operatingCashFlow = cashFlowPage.getOperatingCashFlow(cashFlowDataFrame)

        companyName = priceData.getCompanyName(tickerObject, tickerSymbol)
        dates = date.getDates(cashFlowDataFrame)

        if operatingCashFlow.iloc[-1] > netIncome.iloc[-1]:
            print(f'{companyName} has high quality earnings')
        else:
            print(f'{companyName} has low quality earnings')

        title = 'Cash Based Earnings'


        ax = self.fig.add_subplot(111)
        yLabelText = "Amount in $"
        graphTitle = companyName + " " + title
        ax.set_title(graphTitle)
        ax.set_xlabel('Period')
        ax.set_ylabel(yLabelText)

        ax.get_yaxis().set_major_formatter(matplotlib.ticker.FuncFormatter(lambda x, p: format(int(x), ',')))

        ax.plot(dates, operatingCashFlow, '-o', label='Cash From Operations')
        ax.plot(dates, netIncome, '-o', label='Net Income')

        ax.legend()

        if not self.canvas:
            self.canvas = FigureCanvasTkAgg(self.fig, container)
            self.canvas.get_tk_widget().pack(side="top", fill="both", expand=True)
        self.canvas.draw_idle()


    def clearPlotPage(self):
        self.fig.clear()  # clear your figure
        self.canvas.draw_idle()  # redraw your canvas so it becomes empty


