"""
 This is the class that plots the cash-based earnings graph.
 """

from app.charts.base_graph import BaseGraph
from app.financials import cash_flow_sheet as cash_flow_page, price as price_data
from app.helpers import dates_cleanup as date, tickers as ticker


class CashFlowGraph(BaseGraph):
    """
    Free cash flow graph class.

    This class provides functionality to plot free cash flow graphs for a given stock symbol
    and frequency (annual or quarterly). It utilizes matplotlib for plotting and
    displays the graph in a Tkinter container.
    """

    def __init__(self):
        """
        Initializes the CashFlowGraph class.
        """
        super().__init__("Free Cash Flow in $")

    def plot_cash_graph(self, container, ticker_symbol, frequency):
        """
        Plots the Cash flow for a given stock symbol and frequency.

        Parameters:
        container (tkinter.Frame): The container widget where the plot will be displayed.
        ticker_symbol (str): The stock symbol.
        frequency (str): The frequency of the data (annual or quarterly).

        Returns:
        None
        """
        ticker_object = ticker.get_ticker(ticker_symbol)
        cash_flow_data_frame = cash_flow_page.get_cash_flow_data(
            ticker_object, frequency
        )
        free_cash_flow = cash_flow_page.get_free_cash_flow(cash_flow_data_frame)
        company_name = price_data.get_company_name(ticker_object, ticker_symbol)
        dates = date.get_dates(cash_flow_data_frame)
        cash_flow_graph_title = "Free Cash Flow"

        ax = self.fig.add_subplot(111)
        self.setup_ax(
            ax, f"{company_name} {cash_flow_graph_title}", "Period", self.ylabel_text
        )
        ax.bar(
            dates, free_cash_flow, color=["r" if v < 0 else "g" for v in free_cash_flow]
        )

        for i, v in enumerate(free_cash_flow):
            ax.text(
                i, v * 0.75, f"${v:,.0f}", fontweight="bold", va="center", ha="center"
            )

        self.add_legend(ax, "positive cash flow", "negative cash flow")
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
