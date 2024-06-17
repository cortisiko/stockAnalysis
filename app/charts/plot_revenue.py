"""
This is the class that plots the Revenue graph.
"""

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from matplotlib.lines import Line2D
import pandas as pd
import matplotlib

from app.financials import earnings as earning, price as price_data

from app.helpers import tickers as ticker


matplotlib.use("TkAgg")


class RevenueGraph:
    """
      Revenue graph class.
      """
    def __init__(self):
        self.canvas = None
        self.fig = Figure(figsize=(12, 5), dpi=80)
        self.ylabel_text = "Amount in $"
        self.data = None

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

        ticker_object = ticker.get_ticker(
            ticker_symbol
        )  # Gets the ticker object so you can access the various objects
        earnings_data = earning.get_earnings_data(ticker_object)
        company_name = price_data.get_company_name(ticker_object, ticker_symbol)

        self.data = self.get_freqency(earnings_data, ticker_symbol, frequency)
        earnings_data_frame = pd.DataFrame(self.data)
        dates = earnings_data_frame["date"].astype(str)
        revenue = earnings_data_frame["revenue"]
        revenue = (
            revenue / 100
        )  # This scales the earnings value to Millions or Billions depends on you

        ax = self.fig.add_subplot(111)
        graph_title = company_name + " " + "Revenue"
        ax.set_title(graph_title)
        ax.set_xlabel("Period")
        ax.set_ylabel(self.ylabel_text)

        ax.get_yaxis().set_major_formatter(
            matplotlib.ticker.FuncFormatter(lambda x, p: format(int(x), ","))
        )

        ax.bar(
            dates, revenue, color=["r" if v < 0 else "g" for v in revenue]
        )  ## adding color to bar graphs
        for i, v in enumerate(revenue):
            ax.text(
                i, v * 0.75, f"${v:,.0f}", fontweight="bold", va="center", ha="center"
            )  ## printing values into the bar graphs

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
        ax.legend(legend_handles, ["positive revenue", "negative revenue"])

        # ax.legend()

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

    def clear_plot(self):
        """
              This method clears the canvas.
              """
        self.fig.clear()  # clear your figure
        self.canvas.draw_idle()  # redraw your canvas so it becomes empty
