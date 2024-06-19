"""
Earnings graph class.
"""

import matplotlib
from matplotlib.lines import Line2D
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import pandas as pd

from app.financials import earnings as earning, price as price_data
from app.helpers import tickers as ticker

matplotlib.use("TkAgg")


class EarningsGraph:
    """
    Earnings graph class.

    This class provides functionality to plot earnings graphs for a given stock symbol
    and frequency (annual or quarterly). It utilizes matplotlib for plotting and
    displays the graph in a Tkinter container.
    """

    def __init__(self):
        """
        Initializes the EarningsGraph class.

        Creates a Figure object for the plot and sets default values for
        the y-axis label and graph title.
        """
        self.canvas = None
        self.fig = Figure(figsize=(12, 5), dpi=80)
        self.y_label_text = "Amount in $"
        self.earnings_title = "Earnings"
        self.company_name = None

    def plot_earnings(self, container, ticker_symbol, frequency):
        """
        Plots the Earnings graph for a given stock symbol and frequency.

        Parameters:
        container (tkinter.Frame): The container widget where the plot will be displayed.
        ticker_symbol (str): The stock symbol.
        frequency (str): The frequency of the data (annual or quarterly).

        Returns:
        None

        This method fetches the earnings data for the given stock symbol and frequency,
        creates a bar graph with the data, and displays it in the provided container.
        Positive earnings values are shown in green, and negative values are shown in red.
        """
        ticker_object = ticker.get_ticker(
            ticker_symbol
        )  # Gets the ticker object to access various data
        earnings_data = earning.get_earnings_data(ticker_object)
        self.company_name = price_data.get_company_name(ticker_object, ticker_symbol)

        data = self.get_freqency(earnings_data,ticker_symbol, frequency)
        earnings_data_frame = pd.DataFrame(data)
        dates = earnings_data_frame["date"].astype(str)
        earns = earnings_data_frame["earnings"]
        earns = (
            earns / 1000
        )  # This scales the earnings value to Millions or Billions depending on your preference

        ax = self.fig.add_subplot(111)
        graph_title = self.company_name + " " + self.earnings_title
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

        if not self.canvas:
            self.canvas = FigureCanvasTkAgg(self.fig, container)
            self.canvas.get_tk_widget().pack(side="top", fill="both", expand=True)
        self.canvas.draw_idle()

    def get_freqency(self, earnings_data, ticker_symbol, frequency):
        """
        Retrieves the earnings data for a given stock symbol and frequency.

        Parameters:
        earnings_data (dict): The dictionary containing earnings data.
        ticker_symbol (str): The stock symbol.
        frequency (str): The frequency of the data (annual or quarterly).

        Returns:
        dict: A dictionary containing the earnings data for the specified frequency.

        This method extracts and returns the financial earnings data from the provided
        earnings data dictionary based on the specified frequency (annual or quarterly).
        """
        financial_earnings = earnings_data[ticker_symbol]["financialsChart"][frequency]
        return financial_earnings

    def clear_plot_page(self):
        """
        Clears the plot page.

        This method clears the current figure and redraws the canvas to be empty.
        """
        self.fig.clear()  # clear your figure
        self.canvas.draw_idle()  # redraw your canvas so it becomes empty
