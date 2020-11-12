import matplotlib
import pandas as pd
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from Financials import price as price_data
from Financials import earnings as earning
from helpers import tickers as ticker
from matplotlib.lines import Line2D

matplotlib.use("TkAgg")


class EarningsGraph:
    def __init__(self):
        self.canvas = None
        self.fig = Figure(figsize=(12, 5), dpi=80)

    def plot_earnings(self, container, ticker_symbol, frequency):
        ticker_object = ticker.get_ticker(ticker_symbol)  # Gets the ticker object so you can access the various objects
        earnings_data = earning.get_earnings_data(ticker_object)
        company_name = price_data.get_company_name(ticker_object, ticker_symbol)
        earnings_title = 'Earnings'

        data = self.get_freqency(earnings_data, frequency, ticker_symbol)
        earnings_data_frame = pd.DataFrame(data)
        dates = earnings_data_frame['date'].astype(str)
        # revs = earningsDataFrame['revenue'] no real need for revenue right now
        earns = earnings_data_frame['earnings']
        earns = earns / 1000  # This scales the earnings value to Millions or Billions depends on how you want to read the chart

        ax = self.fig.add_subplot(111)
        yLabelText = "Amount in $"
        graph_title = company_name + " " + earnings_title
        ax.set_title(graph_title)
        ax.set_xlabel('Period')
        ax.set_ylabel(yLabelText)

        ax.get_yaxis().set_major_formatter(matplotlib.ticker.FuncFormatter(lambda x, p: format(int(x), ',')))

        ax.bar(dates, earns, color=['r' if v < 0 else 'g' for v in earns])
        for i, v in enumerate(earns):
            ax.text(i, v * 0.75, f'${v:,.0f}', fontweight='bold', va='center', ha='center')

        legend_handles = [
            Line2D([0], [0], linewidth=0, marker='o', markerfacecolor=color, markersize=12, markeredgecolor='none')
            for color in ['g', 'r']]
        ax.legend(legend_handles, ['positive earnings', 'negative earnings'])

        # ax.legend()

        if not self.canvas:
            self.canvas = FigureCanvasTkAgg(self.fig, container)
            self.canvas.get_tk_widget().pack(side="top", fill="both", expand=True)
        self.canvas.draw_idle()

    def get_freqency(self, earnings_data, frequency, ticker_symbol):
        if frequency == 'yearly':
            yearly_financial_earnings = earnings_data[ticker_symbol]['financialsChart'][frequency]
            return yearly_financial_earnings
        else:
            quarterly_financial_earnings = earnings_data[ticker_symbol]['financialsChart'][frequency]
            return quarterly_financial_earnings

    def clear_plot(self):
        self.fig.clear()  # clear your figure
        self.canvas.draw_idle()  # redraw your canvas so it becomes empty
