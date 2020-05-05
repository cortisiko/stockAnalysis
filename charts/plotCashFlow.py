import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from Financials import cashFlowSheet as cashFlowPage
from Financials import price as priceData
from Financials import incomeStatementSheet as income

from helpers import Ticker as ticker
from helpers import getDate as date

class PlotGraph:
    def __init__(self):
        self.canvas = None
        self.fig = Figure(figsize=(12, 5), dpi=80)

    def plotCashGraph(self, container,tickerSymbol,Frequency):
        tickerObject = ticker.getTicker(tickerSymbol)  ## Gets the ticker object so you can access the various objects
        cashFlowDataFrame = cashFlowPage.getCashFlowData(tickerObject, Frequency)
        freeCashFlow = cashFlowPage.getFreeCashFlow(cashFlowDataFrame)
        companyName = priceData.getCompanyName(tickerObject, tickerSymbol)
        dates = date.getDates(cashFlowDataFrame)
        cashFlowGraphTitle = 'Free Cash Flow'

        ax = self.fig.add_subplot(111)

        yLabelText = "Free Cash Flow in $"
        graphTitle = companyName + " " + cashFlowGraphTitle
        ax.set_title(graphTitle)
        ax.set_xlabel('Years')
        ax.set_ylabel(yLabelText)

        ax.get_yaxis().set_major_formatter(matplotlib.ticker.FuncFormatter(lambda x, p: format(int(x), ',')))
        ax.plot(dates, freeCashFlow, '-o', color='green')

        if not self.canvas:
            self.canvas = FigureCanvasTkAgg(self.fig, container)
            self.canvas.get_tk_widget().pack(side="top", fill="both", expand=True)
        self.canvas.draw_idle()


    def clearPlotPage(self):
        self.fig.clear()  # clear your figure
        self.canvas.draw_idle()  # redraw your canvas so it becomes empty


