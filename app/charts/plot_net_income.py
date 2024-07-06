"""
This is the class that plots the Net Income graph.
"""

from app.charts.base_graph import BaseGraph
from app.financials import income_statements as income, price as priceData
from app.helpers import dates_cleanup as date, tickers as ticker


class NetIncomeGraph(BaseGraph):
    """
    Net Income graph class.

    This class provides functionality to plot net income graphs for a given stock symbol
    and frequency (annual or quarterly). It utilizes matplotlib for plotting and
    displays the graph in a Tkinter container.
    """
    # pylint: disable=too-few-public-methods

    def __init__(self):
        """
        Initializes the NetIncomeGraph class.
        """
        # pylint: disable=too-few-public-methods

        super().__init__("Net Income in $")

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
        ticker_object = ticker.get_ticker(ticker_symbol)
        income_statements_data_frame = income.get_income_statement(
            ticker_object, frequency
        )
        income_statement = income.get_net_income(income_statements_data_frame)
        company_name = priceData.get_company_name(ticker_object, ticker_symbol)
        dates = date.get_dates(income_statements_data_frame)
        income_statement_title = "Net income"

        ax = self.fig.add_subplot(111)
        graph_title = f"{company_name} {income_statement_title}"
        self.setup_ax(ax, graph_title, "Period", self.ylabel_text)

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

        self.add_legend(ax, "positive net income", "negative net income")
        self.draw_canvas(container)
