import matplotlib

matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

from Financials import price as price_data
from Financials import incomestatementsheet as income
from Financials import cashflowsheet as cash_flow_page

from helpers import datecleanup as dates
from helpers import tickers as ticker


class CashBasedEarningGraph:
    def __init__(self):
        self.canvas = None
        self.fig = Figure(figsize=(12, 5), dpi=80)

    def plotCashToEarnings(self, container, ticker_symbol, frequency):
        ticker_object = ticker.get_ticker(ticker_symbol)  # Gets the ticker object so you can access the various objects
        income_statements_data_frame = income.get_income_statement(ticker_object, frequency)
        net_income = income.get_net_income(income_statements_data_frame)
        cash_flow_data_frame = cash_flow_page.get_cash_flow_data(ticker_object, frequency)
        operating_cash_flow = cash_flow_page.get_operating_cash_flow(cash_flow_data_frame)

        company_name = price_data.get_company_name(ticker_object, ticker_symbol)
        all_dates = dates.get_dates(cash_flow_data_frame)

        if operating_cash_flow.iloc[-1] > net_income.iloc[-1]:
            print(f'{company_name} has high quality earnings')
        else:
            print(f'{company_name} has low quality earnings')

        title = 'Cash Based Earnings'

        ax = self.fig.add_subplot(111)
        yLabelText = "Amount in $"
        graph_title = company_name + " " + title
        ax.set_title(graph_title)
        ax.set_xlabel('Period')
        ax.set_ylabel(yLabelText)

        ax.get_yaxis().set_major_formatter(matplotlib.ticker.FuncFormatter(lambda x, p: format(int(x), ',')))

        ax.plot(all_dates, operating_cash_flow, '-o', label='Cash From Operations')
        ax.plot(all_dates, net_income, '-o', label='Net Income')

        ax.legend()

        if not self.canvas:
            self.canvas = FigureCanvasTkAgg(self.fig, container)
            self.canvas.get_tk_widget().pack(side="top", fill="both", expand=True)
        self.canvas.draw_idle()

    def clearPlotPage(self):
        self.fig.clear()  # clear your figure
        self.canvas.draw_idle()  # redraw your canvas so it becomes empty
