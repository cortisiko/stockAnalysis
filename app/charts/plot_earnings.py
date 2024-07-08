"""
 Earnings graph class.
 """

import pandas as pd
from app.charts.base_graph import BaseGraph
from app.financials import price as price_data
from app.helpers import tickers as ticker


class EarningsGraph(BaseGraph):
    """
    Earnings graph class.

    This class provides functionality to plot earnings graphs for a given stock symbol
    and frequency (annual or quarterly). It utilizes matplotlib for plotting and
    displays the graph in a Tkinter container.
    """

    def __init__(self):
        """
        Initializes the EarningsGraph class.
        """
        super().__init__("Amount in $")
        self.earnings_title = "Earnings"

    def plot_earnings(self, container, ticker_symbol, frequency):
        """
        Plots the Earnings graph for a given stock symbol and frequency.

        Parameters:
        container (tkinter.Frame): The container widget where the plot will be displayed.
        ticker_symbol (str): The stock symbol.
        frequency (str): The frequency of the data (annual or quarterly).

        Returns:
        None
        """
        ticker_object = ticker.get_ticker(ticker_symbol)
        earnings_data = ticker_symbol.earnings
        company_name = price_data.get_company_name(ticker_object, ticker_symbol)

        data = self.get_freqency(earnings_data, ticker_symbol, frequency)
        earnings_data_frame = pd.DataFrame(data)
        dates = earnings_data_frame["date"].astype(str)
        earns = earnings_data_frame["earnings"] / 1000

        ax = self.fig.add_subplot(111)
        self.setup_ax(
            ax, f"{company_name} {self.earnings_title}", "Period", self.ylabel_text
        )
        ax.bar(dates, earns, color=["r" if v < 0 else "g" for v in earns])

        for i, v in enumerate(earns):
            ax.text(
                i, v * 0.75, f"${v:,.0f}", fontweight="bold", va="center", ha="center"
            )

        self.add_legend(ax, "positive earnings", "negative earnings")
        self.draw_canvas(container)

    def get_freqency(self, earnings_data, ticker_symbol, frequency):
        """
        Retrieves the earnings data for a given stock symbol and frequency.

        Parameters:
        earnings_data (dict): The dictionary containing earnings data.
        ticker_symbol (str): The stock symbol.
        frequency (str): The frequency of the data (annual or quarterly).

        Returns:
        dict: A dictionary containing the earnings data for the specified frequency.
        """
        return earnings_data[ticker_symbol]["financialsChart"][frequency]
