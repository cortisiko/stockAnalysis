"""
 This is the class that plots the cash-based earnings graph.
 """

from app.charts.base_graph import BaseGraph
from app.financials import (
    cash_flow as cash_flow_page,
    income_statements as income,
    price as price_data,
)
from app.helpers import dates_cleanup as dates, tickers as ticker


class CashBasedEarningGraph(BaseGraph):
    """
    Cash-based earnings graph class.

    This class provides functionality to plot cash-based earnings graphs for a given stock symbol
    and frequency (annual or quarterly). It utilizes matplotlib for plotting and
    displays the graph in a Tkinter container.
    """
    # pylint: disable=too-few-public-methods

    def __init__(self):
        """
        Initializes the CashBasedEarningGraph class.
        """
        super().__init__("Amount in $")
        self.title = "Cash Based Earnings"

    def plot_cash_to_earnings(self, container, ticker_symbol, frequency):
        """
        Plots the Cash to Earnings ratio for a given stock symbol and frequency.

        Parameters:
        container (tkinter.Frame): The container widget where the plot will be displayed.
        ticker_symbol (str): The stock symbol.
        frequency (str): The frequency of the data (annual or quarterly).

        Returns:
        None
        """
        ticker_object = ticker.get_ticker(ticker_symbol)
        income_statements_df = income.get_income_statement(ticker_object, frequency)
        net_income = income.get_net_income(income_statements_df)
        cash_flow_df = cash_flow_page.get_cash_flow_data(ticker_object, frequency)
        operating_cash_flow = cash_flow_page.get_operating_cash_flow(cash_flow_df)

        company_name = price_data.get_company_name(ticker_object, ticker_symbol)
        all_dates = dates.get_dates(cash_flow_df)

        # Ensure the lengths of the arrays match before plotting
        min_length = min(len(all_dates), len(net_income), len(operating_cash_flow))
        all_dates = all_dates[:min_length]
        net_income = net_income[:min_length]
        operating_cash_flow = operating_cash_flow[:min_length]

        if operating_cash_flow.iloc[-1] > net_income.iloc[-1]:
            print(f"{company_name} has high quality earnings")
        else:
            print(f"{company_name} has low quality earnings")

        ax = self.fig.add_subplot(111)
        graph_title = f"{company_name} {self.title}"
        self.setup_ax(ax, graph_title, "Period", self.ylabel_text)

        ax.plot(all_dates, operating_cash_flow, "-o", label="Cash From Operations")
        ax.plot(all_dates, net_income, "-o", label="Net Income")

        ax.legend()
        self.draw_canvas(container)
