import matplotlib

from matplotlib.lines import Line2D
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

from app.financials import cashflowsheet as cash_flow_page, price as price_data

from app.helpers import datecleanup as date, tickers as ticker

matplotlib.use("TkAgg")


class CashFlowGraph:
    def __init__(self):
        self.canvas = None
        self.fig = Figure(figsize=(12, 5), dpi=80)

    def plotCashGraph(self, container, ticker_symbol, frequency):
        ticker_object = ticker.get_ticker(
            ticker_symbol)  ## Gets the ticker object so you can access the various objects
        cash_flow_data_frame = cash_flow_page.get_cash_flow_data(ticker_object, frequency)
        free_cash_flow = cash_flow_page.get_free_cash_flow(cash_flow_data_frame)
        company_name = price_data.get_company_name(ticker_object, ticker_symbol)
        dates = date.get_dates(cash_flow_data_frame)
        cash_flow_graph_title = 'Free Cash Flow'

        ax = self.fig.add_subplot(111)

        yLabelText = "Free Cash Flow in $"
        graphTitle = company_name + " " + cash_flow_graph_title
        ax.set_title(graphTitle)
        ax.set_xlabel('Period')
        ax.set_ylabel(yLabelText)

        ax.get_yaxis().set_major_formatter(matplotlib.ticker.FuncFormatter(lambda x, p: format(int(x), ',')))

        ax.bar(dates, free_cash_flow, color=['r' if v < 0 else 'g' for v in free_cash_flow])
        for i, v in enumerate(free_cash_flow):
            ax.text(i, v * 0.75, f'${v:,.0f}', fontweight='bold', va='center', ha='center')

        legend_handles = [
            Line2D([0], [0], linewidth=0, marker='o', markerfacecolor=color, markersize=12, markeredgecolor='none')
            for color in ['g', 'r']]
        ax.legend(legend_handles, ['positive cash flow', 'negative cash flow'])

        if not self.canvas:
            self.canvas = FigureCanvasTkAgg(self.fig, container)
            self.canvas.get_tk_widget().pack(side="top", fill="both", expand=True)
        self.canvas.draw_idle()

    def clearPlotPage(self):
        self.fig.clear()  # clear your figure
        self.canvas.draw_idle()  # redraw your canvas so it becomes empty
