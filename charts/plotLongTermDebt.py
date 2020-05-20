import matplotlib
matplotlib.use("TkAgg")
from matplotlib.lines import Line2D
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

from Financials import balanceSheet as balancesheet
from Financials import price as priceData

from helpers import Ticker as ticker
from helpers import getDate as date

class PlotGraph:
    def __init__(self):
        self.canvas = None
        self.fig = Figure(figsize=(12, 5), dpi=80)

    def plotDebtGraph(self, container,tickerSymbol,Frequency):
        tickerObject = ticker.getTicker(tickerSymbol)  ## Gets the ticker object so you can access the various objects
        balanceSheetDataFrame = balancesheet.getBalanceSheetData(tickerObject, Frequency)
        longTermDebt = balancesheet.getLongTermDebt(balanceSheetDataFrame)
        companyName = priceData.getCompanyName(tickerObject, tickerSymbol)
        dates = date.getDates(balanceSheetDataFrame)
        graphTitle = 'Long Term Debt'

        ax = self.fig.add_subplot(111)

        yLabelText = "Long term Debt $"
        graphTitle = companyName + " " + graphTitle
        ax.set_title(graphTitle)
        ax.set_xlabel('Years')
        ax.set_ylabel(yLabelText)

        ax.get_yaxis().set_major_formatter(matplotlib.ticker.FuncFormatter(lambda x, p: format(int(x), ',')))

        ax.bar(dates, longTermDebt, color=['r' if v < 0 else 'g' for v in longTermDebt])
        for i, v in enumerate(longTermDebt):
            ax.text(i, v * 0.75, f'${v:,.0f}', fontweight='bold', va='center', ha='center')

        legend_handles = [
            Line2D([0], [0], linewidth=0, marker='o', markerfacecolor=color, markersize=12, markeredgecolor='none')
            for color in ['g', 'r']]
        ax.legend(legend_handles, ['positive cash flow', 'negative cash flow'])

        if not self.canvas:
            self.canvas = FigureCanvasTkAgg(self.fig, container)
            self.canvas.get_tk_widget().pack(side="top", fill="both", expand=True)
        self.canvas.draw_idle()


    def clearPlotPage(self):
        self.fig.clear()  # clear your figure
        self.canvas.draw_idle()  # redraw your canvas so it becomes empty


