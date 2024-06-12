import matplotlib

matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

from app.financials import balancesheet as balancesheet, price as price_data

from app.helpers import datescleanup as date, tickers as ticker


class DebtGraph:
    def __init__(self):
        self.canvas = None
        self.fig = Figure(figsize=(12, 5), dpi=80)

    def plot_debt_graph(self, container, ticker_symbol, frequency):
        ticker_object = ticker.get_ticker(
            ticker_symbol
        )  ## Gets the ticker object so you can access the various objects
        balance_sheet_data_frame = balancesheet.get_balance_sheet_data(
            ticker_object, frequency
        )
        long_term_debt = balancesheet.get_long_term_debt(balance_sheet_data_frame)
        company_name = price_data.get_company_name(ticker_object, ticker_symbol)
        dates = date.get_dates(balance_sheet_data_frame)
        graph_title = "Long Term Debt"

        ax = self.fig.add_subplot(111)

        yLabelText = "Long term Debt $"
        graph_title = company_name + " " + graph_title
        ax.set_title(graph_title)
        ax.set_xlabel("Period")
        ax.set_ylabel(yLabelText)

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

    def clearPlotPage(self):
        self.fig.clear()  # clear your figure
        self.canvas.draw_idle()  # redraw your canvas so it becomes empty
