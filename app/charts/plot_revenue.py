"""
This is the class that plots the Revenue graph.
"""

import pandas as pd

from app.charts.base_graph import BaseGraph
from app.financials import earnings as earning, price as price_data
from app.helpers import tickers as ticker


class RevenueGraph(BaseGraph):
    """
    Revenue graph class.

    This class provides functionality to plot revenue graphs for a given stock symbol
    and frequency (annual or quarterly). It utilizes matplotlib for plotting and
    displays the graph in a Tkinter container.
    """

    def __init__(self):
        """
        Initializes the RevenueGraph class.
        """
        super().__init__("Amount in $")

    def plot_revenue(self, container, ticker_symbol, frequency):
        """
        Plots the Revenue graph for a given stock symbol and frequency.

        Parameters:
        container (tkinter.Frame): The container widget where the plot will be displayed.
        ticker_symbol (str): The stock symbol.
        frequency (str): The frequency of the data (annual or quarterly).

        Returns:
        None

        This method fetches the revenue data for the given stock symbol and frequency,
        creates a bar graph with the data, and displays it in the provided container.
        Positive revenue values are shown in green, and negative values are shown in red.
        """
        ticker_object = ticker.get_ticker(ticker_symbol)
        earnings_data = earning.get_earnings_data(ticker_object)
        company_name = price_data.get_company_name(ticker_object, ticker_symbol)

        data = self.get_frequency(earnings_data, ticker_symbol, frequency)
        earnings_data_frame = pd.DataFrame(data)
        dates = earnings_data_frame["date"].astype(str)
        revenue = earnings_data_frame["revenue"] / 100  # Scale revenue

        ax = self.fig.add_subplot(111)
        graph_title = f"{company_name} Revenue"
        self.setup_ax(ax, graph_title, "Period", self.ylabel_text)

        ax.bar(dates, revenue, color=["r" if v < 0 else "g" for v in revenue])
        for i, v in enumerate(revenue):
            ax.text(
                i, v * 0.75, f"${v:,.0f}", fontweight="bold", va="center", ha="center"
            )

        self.add_legend(ax, "positive revenue", "negative revenue")
        self.draw_canvas(container)

    def get_frequency(self, earnings_data, ticker_symbol, frequency):
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
        return earnings_data[ticker_symbol]["financialsChart"][frequency]
