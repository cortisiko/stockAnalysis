import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from Financials import price as priceData
from Financials import earnings as earning

from helpers import Ticker as ticker
from helpers import getDate as date

class PlotGraph:
    def __init__(self):
        self.canvas = None
        self.fig = Figure(figsize=(12, 5), dpi=80)

    def plotEarnings(self, container,tickerSymbol,Frequency):
        tickerObject = ticker.getTicker(tickerSymbol)  ## Gets the ticker object so you can access the various objects
        earningsData = earning.getEarningsData(tickerObject)
        YearlyfinaincalEarnings = earningsData[tickerSymbol]['financialsChart']['yearly']
        quarterlyfinaincalEarnings = earningsData[tickerSymbol]['financialsChart']['quarterly']
        companyName = priceData.getCompanyName(tickerObject, tickerSymbol)
        EarningsTitle = 'Earnings'

        dates, revs, earns = [], [], []
        for a in quarterlyfinaincalEarnings:
            dates.append(a['date'])
            revs.append(a['revenue'])
            earns.append(a['earnings'])

        ax = self.fig.add_subplot(111)

        yLabelText = "Earnings in $"
        graphTitle = companyName + " " + EarningsTitle
        ax.set_title(graphTitle)
        ax.set_xlabel('Years')
        ax.set_ylabel(yLabelText)

        ax.get_yaxis().set_major_formatter(matplotlib.ticker.FuncFormatter(lambda x, p: format(int(x), ',')))

        ax.plot(dates, revs, '-o', label='revenues')
        ax.plot(dates, earns, '-o', label='earnings')
        ax.legend()

        if not self.canvas:
            self.canvas = FigureCanvasTkAgg(self.fig, container)
            self.canvas.get_tk_widget().pack(side="top", fill="both", expand=True)
        self.canvas.draw_idle()


    def clearPlotPage(self):
        self.fig.clear()  # clear your figure
        self.canvas.draw_idle()  # redraw your canvas so it becomes empty


