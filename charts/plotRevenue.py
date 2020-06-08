import pandas as pd

import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from matplotlib.lines import Line2D

from Financials import price as priceData
from Financials import earnings as earning

from helpers import Ticker as ticker

class PlotGraph:
    def __init__(self):
        self.canvas = None
        self.fig = Figure(figsize=(12, 5), dpi=80)

    def plotRevenue(self, container,tickerSymbol,Frequency):
        tickerObject = ticker.getTicker(tickerSymbol)  ## Gets the ticker object so you can access the various objects
        earningsData = earning.getEarningsData(tickerObject)
        companyName = priceData.getCompanyName(tickerObject, tickerSymbol)
        RevenueText = 'Revenue'

        data = self.getFreqency(earningsData, Frequency, tickerSymbol)
        earningsDataFrame = pd.DataFrame(data)
        dates = earningsDataFrame['date'].astype(str)
        revs = earningsDataFrame['revenue']
        revs = revs/ 100 ## This scales the earnings value to Millions or Billions depends on how you want to read the chart

        ax = self.fig.add_subplot(111)
        yLabelText = "Amount in $"
        graphTitle = companyName + " " + RevenueText
        ax.set_title(graphTitle)
        ax.set_xlabel('Period')
        ax.set_ylabel(yLabelText)

        ax.get_yaxis().set_major_formatter(matplotlib.ticker.FuncFormatter(lambda x, p: format(int(x), ',')))

        ax.bar(dates, revs, color=['r' if v < 0 else 'g' for v in revs]) ## adding color to bar graphs
        for i, v in enumerate(revs):
            ax.text(i, v * 0.75,f'${v:,.0f}', fontweight='bold', va='center', ha='center') ## printing values into the bar graphs

        legend_handles = [Line2D([0], [0], linewidth=0, marker='o', markerfacecolor=color, markersize=12, markeredgecolor='none')
            for color in ['g', 'r']]
        ax.legend(legend_handles, ['positive revenue', 'negative revenue'])

        #ax.legend()

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


