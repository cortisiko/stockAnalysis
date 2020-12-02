import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from matplotlib.lines import Line2D

from app.financials import incomestatementsheet as income, price as priceData

from app.helpers import dates_cleanup as date, tickers as ticker


class NetIncomeGraph:
    def __init__(self):
        self.canvas = None
        self.fig = Figure(figsize=(12, 5), dpi=80)

    def plot_net_income(self, container,ticker_symbol,Frequency):
        ticker_object = ticker.get_ticker(ticker_symbol)  ## Gets the ticker object so you can access the various objects
        income_statements_data_drame = income.get_income_statement(ticker_object, Frequency)
        income_statement = income.get_net_income(income_statements_data_drame)
        company_name = priceData.get_company_name(ticker_object, ticker_symbol)
        dates = date.get_dates(income_statements_data_drame)
        income_statement_title = 'Net income'

        ax = self.fig.add_subplot(111)

        yLabelText = "Net Income in $"
        graph_title = company_name + " " + income_statement_title
        ax.set_title(graph_title)
        ax.set_xlabel('Period')
        ax.set_ylabel(yLabelText)

        ax.get_yaxis().set_major_formatter(matplotlib.ticker.FuncFormatter(lambda x, p: format(int(x), ',')))

        ax.bar(dates, income_statement, color=['r' if v < 0 else 'g' for v in income_statement])
        for i, v in enumerate(income_statement):
            ax.text(i, v * 0.75, f'${v:,.0f}', fontweight='bold', va='center', ha='center',color ='#0A0A0A')

        legend_handles = [
            Line2D([0], [0], linewidth=0, marker='o', markerfacecolor=color, markersize=12, markeredgecolor='none')
            for color in ['g', 'r']]
        ax.legend(legend_handles, ['positive net income', 'negative net income'])

        if not self.canvas:
            self.canvas = FigureCanvasTkAgg(self.fig, container)
            self.canvas.get_tk_widget().pack(side="top", fill="both", expand=True)
        self.canvas.draw_idle()

    def clearPlotPage(self):
        self.fig.clear()  # clear your figure
        self.canvas.draw_idle()  # redraw your canvas so it becomes empty


