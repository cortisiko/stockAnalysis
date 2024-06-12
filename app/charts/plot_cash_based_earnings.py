"""
This is the class that plots the cash-based earnings graph.
"""

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import matplotlib
from app.financials import (
    cash_flow_sheet as cash_flow_page,
    incomestatementsheet as income,
    price as price_data,
)
from app.helpers import datescleanup as dates, tickers as ticker

matplotlib.use("TkAgg")


class CashBasedEarningGraph:
    """
    Cash-based earnings graph class.
    """

    def __init__(self):
        self.canvas = None
        self.fig = Figure(figsize=(12, 5), dpi=80)
        self.title = "Cash Based Earnings"

    def plot_cash_to_earnings(self, container, ticker_symbol, frequency):
        """
        Plots the Cash to Earnings ratio for a given stock symbol and frequency.

        :param container: The container widget where the plot will be displayed.
        :param ticker_symbol: The stock symbol.
        :param frequency: The frequency of the data (annual or quarterly).
        :return: None
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
        y_label_text = "Amount in $"
        graph_title = company_name + " " + self.title
        ax.set_title(graph_title)
        ax.set_xlabel("Period")
        ax.set_ylabel(y_label_text)

        ax.get_yaxis().set_major_formatter(
            matplotlib.ticker.FuncFormatter(lambda x, p: format(int(x), ","))
        )

        ax.plot(all_dates, operating_cash_flow, "-o", label="Cash From Operations")
        ax.plot(all_dates, net_income, "-o", label="Net Income")

        ax.legend()

        if not self.canvas:
            self.canvas = FigureCanvasTkAgg(self.fig, container)
            self.canvas.get_tk_widget().pack(side="top", fill="both", expand=True)
        self.canvas.draw_idle()

    def clear_plot_page(self):
        """
        This method clears the canvas.
        """
        self.fig.clear()  # clear your figure
        self.canvas.draw_idle()  # redraw your canvas so it becomes empty
