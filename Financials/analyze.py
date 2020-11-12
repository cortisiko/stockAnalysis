from Financials import cashFlowSheet as cashFlowPage
from Financials import statistics as statisticsTab
from Financials import summary as summaryPage
from Financials import price as priceData

from Financials import balanceSheet as balancesheet
from helpers import Ticker as ticker
from Financials import companyProfile as companyprofile

error_message = "Invalid Stock Symbol"


def get_company_sector(ticker_symbol):
    try:
        ticker_object = ticker.get_ticker(ticker_symbol)  ## Gets the ticker object so you can access the various objects
        company_sector = companyprofile.get_company_sector(ticker_object, ticker_symbol)
        return company_sector
    except TypeError:
        return error_message


def get_company_details(ticker_symbol):
    try:
        ticker_object = ticker.get_ticker(ticker_symbol)  ## Gets the ticker object so you can access the various objects
        company_details = companyprofile.get_company_summary_details(ticker_object, ticker_symbol)
        return company_details
    except TypeError:
        return error_message


def get_stock_name(ticker_symbol):
    try:
        ticker_object = ticker.get_ticker(ticker_symbol)  ## Gets the ticker object so you can access the various objects
        stock_name = priceData.getCompanyName(ticker_object, ticker_symbol)
        return stock_name
    except TypeError:
        return error_message

    ## Fundamentals ###


def get_current_stock_price(ticker_symbol):
    ticker_object = ticker.get_ticker(ticker_symbol)  ## Gets the ticker object so you can access the various objects
    current_stock_price = priceData.getCurrentStockPrice(ticker_object, ticker_symbol)

    return current_stock_price


def get_eps(ticker_symbol):
    ticker_object = ticker.get_ticker(ticker_symbol)  ## Gets the ticker object so you can access the various objects
    eps = summaryPage.getEarningsPerShare(ticker_object, ticker_symbol)
    return eps


def get_pe_ratio(ticker_symbol):
    ticker_object = ticker.get_ticker(ticker_symbol)  ## Gets the ticker object so you can access the various objects
    pe_ratio = summaryPage.get_pe_ratio(ticker_object, ticker_symbol)

    return pe_ratio


def get_debt_to_equity(ticker_symbol):
    ticker_object = ticker.get_ticker(ticker_symbol)  ## Gets the ticker object so you can access the various objects
    debt_to_equity_ratio = statisticsTab.getDebtToEquity(ticker_object, ticker_symbol)

    return debt_to_equity_ratio


def get_return_on_equity(ticker_symbol):
    ticker_object = ticker.get_ticker(ticker_symbol)  ## Gets the ticker object so you can access the various objects
    return_on_equity = statisticsTab.getReturnOnEquity(ticker_object, ticker_symbol)

    return return_on_equity


def get_profit_margin(ticker_symbol):
    ticker_object = ticker.get_ticker(ticker_symbol)  ## Gets the ticker object so you can access the various objects
    profit_margin = statisticsTab.getProfitMargins(ticker_object, ticker_symbol)

    return profit_margin


def get_cash_burn_number(ticker_symbol):
    global most_recent_cash_flow
    ticker_object = ticker.get_ticker(ticker_symbol)  ## Gets the ticker object so you can access the various objects
    balance_sheet_data_frame = balancesheet.getBalanceSheetData(ticker_object, Frequency='a')
    cash_flow_data_frame = cashFlowPage.getCashFlowData(ticker_object, Frequency='a')

    cash_and_cash_equivalents = balancesheet.getCashAndExpenses(balance_sheet_data_frame)

    ## because balance sheet does not have a TTM.## if the size of the cash flow data frame > balance sheet select
    ## the most recent year(not TTM)
    if cash_flow_data_frame.shape[0] > balance_sheet_data_frame.shape[0]:
        most_recent_cash_flow = cashFlowPage.get_most_recent_cash_flow_total(cash_flow_data_frame, -2)

    cash_burn = cashFlowPage.calculate_cash_burn(cash_and_cash_equivalents, most_recent_cash_flow)

    ticker_name = get_stock_name(ticker_symbol)
    if cash_burn < 0:
        print(f'{ticker_name} is already running out of money. Their cash burn is:{cash_burn:,.1f} months')
    else:
        print(f'It will take {cash_burn:,.1f} months before {ticker_name} runs out of money')
