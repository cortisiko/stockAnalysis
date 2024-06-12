"""
  Earnings graph class.
  """

import matplotlib
from matplotlib.lines import Line2D
import pandas as pd
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from app.financials import earnings as earning, price as price_data
from app.helpers import tickers as ticker


matplotlib.use("TkAgg")


class EarningsGraph:
    """
      Earnings graph class.
      """
    def __init__(self):
        self.canvas = None
        self.fig = Figure(figsize=(12, 5), dpi=80)
        self.y_label_text = "Amount in $"
        self.earnings_title = "Earnings"



    def plot_earnings(self, container, ticker_symbol, frequency):
        ticker_object = ticker.get_ticker(
            ticker_symbol
        )  # Gets the ticker object so you can access the various objects
        earnings_data = earning.get_earnings_data(ticker_object)
        company_name = price_data.get_company_name(ticker_object, ticker_symbol)

        data = self.get_freqency(earnings_data, frequency, ticker_symbol)
        earnings_data_frame = pd.DataFrame(data)
        dates = earnings_data_frame["date"].astype(str)
        # revs = earningsDataFrame['revenue'] no real need for revenue right now
        earns = earnings_data_frame["earnings"]
        earns = (
            earns / 1000
        )  # This scales the earnings value to Millions or Billions depends on how you want to read the chart

        ax = self.fig.add_subplot(111)
        graph_title = company_name + " " + self.earnings_title
        ax.set_title(graph_title)
        ax.set_xlabel("Period")
        ax.set_ylabel(self.y_label_text)

        ax.get_yaxis().set_major_formatter(
            matplotlib.ticker.FuncFormatter(lambda x, p: format(int(x), ","))
        )

        ax.bar(dates, earns, color=["r" if v < 0 else "g" for v in earns])
        for i, v in enumerate(earns):
            ax.text(
                i, v * 0.75, f"${v:,.0f}", fontweight="bold", va="center", ha="center"
            )

        legend_handles = [
            Line2D(
                [0],
                [0],
                linewidth=0,
                marker="o",
                markerfacecolor=color,
                markersize=12,
                markeredgecolor="none",
            )
            for color in ["g", "r"]
        ]
        ax.legend(legend_handles, ["positive earnings", "negative earnings"])

        # ax.legend()

        if not self.canvas:
            self.canvas = FigureCanvasTkAgg(self.fig, container)
            self.canvas.get_tk_widget().pack(side="top", fill="both", expand=True)
        self.canvas.draw_idle()

    def get_freqency(self, earnings_data, frequency, ticker_symbol):
        if frequency == "yearly":
            yearly_financial_earnings = earnings_data[ticker_symbol]["financialsChart"][
                frequency
            ]
            return yearly_financial_earnings
        else:
            quarterly_financial_earnings = earnings_data[ticker_symbol][
                "financialsChart"
            ][frequency]
            return quarterly_financial_earnings

    def clear_plot_page(self):
        """
        This method clears the canvas.
        """
        self.fig.clear()  # clear your figure
        self.canvas.draw_idle()  # redraw your canvas so it becomes empty
