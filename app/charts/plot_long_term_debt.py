"""
 This is the class that plots the Long term debt graph.
 """

from app.charts.base_graph import BaseGraph
from app.financials import balance_sheet, price as price_data
from app.helpers import tickers as ticker, dates_cleanup as date


class DebtGraph(BaseGraph):
    """
    Debt graph class.

    This class provides functionality to plot long-term debt graphs for a given stock symbol
    and frequency (annual or quarterly). It utilizes matplotlib for plotting and
    displays the graph in a Tkinter container.
    """
    # pylint: disable=too-few-public-methods

    def __init__(self):
        """
        Initializes the DebtGraph class.
        """
        super().__init__("Long term Debt $")

    def plot_debt_graph(self, container, ticker_symbol, frequency):
        """
        Plots the Long Term Debt graph for a given stock symbol and frequency.

        Parameters:
        container (tkinter.Frame): The container widget where the plot will be displayed.
        ticker_symbol (str): The stock symbol.
        frequency (str): The frequency of the data (annual or quarterly).

        Returns:
        None
        """
        ticker_object = ticker.get_ticker(ticker_symbol)
        balance_sheet_data_frame = balance_sheet.get_balance_sheet_data(
            ticker_object, frequency
        )
        long_term_debt = balance_sheet.get_long_term_debt(balance_sheet_data_frame)
        company_name = price_data.get_company_name(ticker_object, ticker_symbol)
        dates = date.get_dates(balance_sheet_data_frame)

        ax = self.fig.add_subplot(111)
        self.setup_ax(ax, f"{company_name} Long Term Debt", "Period", self.ylabel_text)
        ax.bar(dates, long_term_debt, color="r")

        for i, v in enumerate(long_term_debt):
            ax.text(
                i, v * 0.75, f"${v:,.0f}", fontweight="bold", va="center", ha="center"
            )

        self.draw_canvas(container)
