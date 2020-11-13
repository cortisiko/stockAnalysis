import pandas as pd

import matplotlib

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from matplotlib.lines import Line2D

from Financials import price as price_data
from Financials import earnings as earning

from helpers import tickers as ticker

matplotlib.use("TkAgg")


class RevenueGraph:
    def __init__(self):
        self.canvas = None
        self.fig = Figure(figsize=(12, 5), dpi=80)

    def plot_revenue(self, container, ticker_symbol, frequency):
        ticker_object = ticker.get_ticker(
            ticker_symbol)  # Gets the ticker object so you can access the various objects
        earnings_data = earning.get_earnings_data(ticker_object)
        company_name = price_data.get_company_name(ticker_object, ticker_symbol)

        data = self.get_freqency(earnings_data,ticker_symbol,frequency)
        earnings_data_frame = pd.DataFrame(data)
        dates = earnings_data_frame['date'].astype(str)
        revenue = earnings_data_frame['revenue']
        revenue = revenue / 100  # This scales the earnings value to Millions or Billions depends on how you want to read the chart

        ax = self.fig.add_subplot(111)
        yLabelText = "Amount in $"
        graph_title = company_name + " " + 'Revenue'
        ax.set_title(graph_title)
        ax.set_xlabel('Period')
        ax.set_ylabel(yLabelText)

        ax.get_yaxis().set_major_formatter(matplotlib.ticker.FuncFormatter(lambda x, p: format(int(x), ',')))

        ax.bar(dates, revenue, color=['r' if v < 0 else 'g' for v in revenue])  ## adding color to bar graphs
        for i, v in enumerate(revenue):
            ax.text(i, v * 0.75, f'${v:,.0f}', fontweight='bold', va='center',
                    ha='center')  ## printing values into the bar graphs

        legend_handles = [
            Line2D([0], [0], linewidth=0, marker='o', markerfacecolor=color, markersize=12, markeredgecolor='none')
            for color in ['g', 'r']]
        ax.legend(legend_handles, ['positive revenue', 'negative revenue'])

        # ax.legend()

        if not self.canvas:
            self.canvas = FigureCanvasTkAgg(self.fig, container)
            self.canvas.get_tk_widget().pack(side="top", fill="both", expand=True)
        self.canvas.draw_idle()

    def get_freqency(self, earnings_data,ticker_symbol,frequency):
        if frequency == 'yearly':
            yearly_finaincal_earnings = earnings_data[ticker_symbol]['financialsChart'][frequency]
            return yearly_finaincal_earnings
        else:
            quarterly_finaincal_earnings = earnings_data[ticker_symbol]['financialsChart'][frequency]
            return quarterly_finaincal_earnings

    def clearPlotPage(self):
        self.fig.clear()  # clear your figure
        self.canvas.draw_idle()  # redraw your canvas so it becomes empty
