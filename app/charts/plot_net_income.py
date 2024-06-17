"""
This is the class that plots the Net Income graph.
"""


from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from matplotlib.lines import Line2D
import matplotlib

from app.financials import incomestatementsheet as income, price as priceData

from app.helpers import datescleanup as date, tickers as ticker
matplotlib.use("TkAgg")


class NetIncomeGraph:
    """
    Net Income graph class.
    """
    def __init__(self):
        self.canvas = None
        self.fig = Figure(figsize=(12, 5), dpi=80)
        self.ylabel_text = "Net Income in $"


    def plot_net_income(self, container, ticker_symbol, frequency):
        """
        Plots the Net Income graph for a given stock symbol and frequency.

        Parameters:
        container (tkinter.Frame): The container widget where the plot will be displayed.
        ticker_symbol (str): The stock symbol.
        frequency (str): The frequency of the data (annual or quarterly).

        Returns:
        None

        This method fetches the net income data for the given stock symbol and frequency,
        creates a bar graph with the data, and displays it in the provided container.
        Positive net income values are shown in green, and negative values are shown in red.
        """

        ticker_object = ticker.get_ticker(
            ticker_symbol
        )  ## Gets the ticker object so you can access the various objects
        income_statements_data_drame = income.get_income_statement(
            ticker_object, frequency
        )
        income_statement = income.get_net_income(income_statements_data_drame)
        company_name = priceData.get_company_name(ticker_object, ticker_symbol)
        dates = date.get_dates(income_statements_data_drame)
        income_statement_title = "Net income"

        ax = self.fig.add_subplot(111)

        graph_title = company_name + " " + income_statement_title
        ax.set_title(graph_title)
        ax.set_xlabel("Period")
        ax.set_ylabel(self.ylabel_text)

        ax.get_yaxis().set_major_formatter(
            matplotlib.ticker.FuncFormatter(lambda x, p: format(int(x), ","))
        )

        ax.bar(
            dates,
            income_statement,
            color=["r" if v < 0 else "g" for v in income_statement],
        )
        for i, v in enumerate(income_statement):
            ax.text(
                i,
                v * 0.75,
                f"${v:,.0f}",
                fontweight="bold",
                va="center",
                ha="center",
                color="#0A0A0A",
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
        ax.legend(legend_handles, ["positive net income", "negative net income"])

        if not self.canvas:
            self.canvas = FigureCanvasTkAgg(self.fig, container)
            self.canvas.get_tk_widget().pack(side="top", fill="both", expand=True)
        self.canvas.draw_idle()

    def clear_plot(self):
        """
              This method clears the canvas.
              """
        self.fig.clear()  # clear your figure
        self.canvas.draw_idle()  # redraw your canvas so it becomes empty
