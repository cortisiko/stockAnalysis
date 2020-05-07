import matplotlib
matplotlib.use("TkAgg")
import pandas as pd
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from Financials import price as priceData
from Financials import earnings as earning
from helpers import Ticker as ticker

class PlotGraph:
    def __init__(self):
        self.canvas = None
        self.fig = Figure(figsize=(12, 5), dpi=80)

    def plotEarnings(self, container,tickerSymbol,Frequency):
        tickerObject = ticker.getTicker(tickerSymbol)  ## Gets the ticker object so you can access the various objects
        earningsData = earning.getEarningsData(tickerObject)
        companyName = priceData.getCompanyName(tickerObject, tickerSymbol)
        EarningsTitle = 'Earnings'

        data = self.getFreqency(earningsData, Frequency, tickerSymbol)
        earningsDataFrame = pd.DataFrame(data)
        dates = earningsDataFrame['date'].astype(str)
        revs = earningsDataFrame['revenue']
        earns = earningsDataFrame['earnings']

        ax = self.fig.add_subplot(111)
        yLabelText = "Amount in $"
        graphTitle = companyName + " " + EarningsTitle
        ax.set_title(graphTitle)
        ax.set_xlabel('Period')
        ax.set_ylabel(yLabelText)

        ax.get_yaxis().set_major_formatter(matplotlib.ticker.FuncFormatter(lambda x, p: format(int(x), ',')))

        ax.plot(dates, revs, '-o', label='revenues')
        ax.plot(dates, earns, '-o', label='earnings')
        ax.legend()

        if not self.canvas:
            self.canvas = FigureCanvasTkAgg(self.fig, container)
            self.canvas.get_tk_widget().pack(side="top", fill="both", expand=True)
        self.canvas.draw_idle()

    def getFreqency(self,earningsData,Frequency,tickerSymbol):
        if Frequency=='yearly':
            yearlyFinaincalEarnings = earningsData[tickerSymbol]['financialsChart'][Frequency]
            return yearlyFinaincalEarnings
        else:
            quarterlyfinaincalEarnings = earningsData[tickerSymbol]['financialsChart'][Frequency]
            return quarterlyfinaincalEarnings

    def clearPlotPage(self):
        self.fig.clear()  # clear your figure
        self.canvas.draw_idle()  # redraw your canvas so it becomes empty


