import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from Financials import price as priceData
from Financials import incomeStatementSheet as income

from helpers import Ticker as ticker
from helpers import getDate as date

class PlotGraph:
    def __init__(self):
        self.canvas = None
        self.fig = Figure(figsize=(12, 5), dpi=80)

    def netIncomeChart(self, container,tickerSymbol,Frequency):
        tickerObject = ticker.getTicker(tickerSymbol)  ## Gets the ticker object so you can access the various objects
        incomeStatementsDataFrame = income.getIncomeStatements(tickerObject, Frequency)
        incomeStatement = income.getNetIncome(incomeStatementsDataFrame)
        companyName = priceData.getCompanyName(tickerObject, tickerSymbol)
        dates = date.getDates(incomeStatementsDataFrame)
        incomeStatementGraphTitle = 'Net income'

        ax = self.fig.add_subplot(111)

        yLabelText = "Net Income in $"
        graphTitle = companyName + " " + incomeStatementGraphTitle
        ax.set_title(graphTitle)
        ax.set_xlabel('Years')
        ax.set_ylabel(yLabelText)

        ax.get_yaxis().set_major_formatter(matplotlib.ticker.FuncFormatter(lambda x, p: format(int(x), ',')))
        ax.plot(dates, incomeStatement, '-o', color='green')

        if not self.canvas:
            self.canvas = FigureCanvasTkAgg(self.fig, container)
            self.canvas.get_tk_widget().pack(side="top", fill="both", expand=True)
        self.canvas.draw_idle()

    def clearPlotPage(self):
        self.fig.clear()  # clear your figure
        self.canvas.draw_idle()  # redraw your canvas so it becomes empty


