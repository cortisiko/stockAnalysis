"""
This is the class that plots the Revenue graph.
"""

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import matplotlib

from app.financials import balancesheet, price as price_data
from app.helpers import datescleanup as date, tickers as ticker

matplotlib.use("TkAgg")

class DebtGraph:
    """
    Debt graph class.

    This class provides functionality to plot long-term debt graphs for a given stock symbol
    and frequency (annual or quarterly). It utilizes matplotlib for plotting and
    displays the graph in a Tkinter container.
    """

    def __init__(self):
        """
        Initializes the DebtGraph class.

        Creates a Figure object for the plot and sets default values for
        the y-axis label.
        """
        self.canvas = None
        self.fig = Figure(figsize=(12, 5), dpi=80)
        self.ylabel_text = "Long term Debt $"

    def plot_debt_graph(self, container, ticker_symbol, frequency):
        """
        Plots the Long Term Debt graph for a given stock symbol and frequency.

        Parameters:
        container (tkinter.Frame): The container widget where the plot will be displayed.
        ticker_symbol (str): The stock symbol.
        frequency (str): The frequency of the data (annual or quarterly).

        Returns:
        None

        This method fetches the long-term debt data for the given stock symbol and frequency,
        creates a bar graph with the data, and displays it in the provided container.
        """
        ticker_object = ticker.get_ticker(
            ticker_symbol
        )  # Gets the ticker object to access various data
        balance_sheet_data_frame = balancesheet.get_balance_sheet_data(
            ticker_object, frequency
        )
        long_term_debt = balancesheet.get_long_term_debt(balance_sheet_data_frame)
        company_name = price_data.get_company_name(ticker_object, ticker_symbol)
        dates = date.get_dates(balance_sheet_data_frame)
        graph_title = "Long Term Debt"

        ax = self.fig.add_subplot(111)

        graph_title = company_name + " " + graph_title
        ax.set_title(graph_title)
        ax.set_xlabel("Period")
        ax.set_ylabel(self.ylabel_text)

        ax.get_yaxis().set_major_formatter(
            matplotlib.ticker.FuncFormatter(lambda x, p: format(int(x), ","))
        )

        ax.bar(dates, long_term_debt, color="r")
        for i, v in enumerate(long_term_debt):
            ax.text(
                i, v * 0.75, f"${v:,.0f}", fontweight="bold", va="center", ha="center"
            )

        if not self.canvas:
            self.canvas = FigureCanvasTkAgg(self.fig, container)
            self.canvas.get_tk_widget().pack(side="top", fill="both", expand=True)
        self.canvas.draw_idle()

    def clear_plot(self):
        """
        Clears the plot page.

        This method clears the current figure and redraws the canvas to be empty.
        """
        self.fig.clear()  # clear your figure
        self.canvas.draw_idle()  # redraw your canvas so it becomes empty
