from app.financials import statistics as statistics_tab, balancesheet as balance_sheet, \
    companyprofile as company_profile, cashflowsheet as cash_flow_page, summary as summary_page, price as price_data

from app.helpers import tickers as ticker

error_message = "Invalid Stock Symbol"


def get_company_sector(ticker_symbol):
    try:
        ticker_symbol_object = ticker.get_ticker(
            ticker_symbol)  # Gets the ticker_symbol object so you can access the various objects
        company_sector = company_profile.get_company_sector(ticker_symbol_object, ticker_symbol)
        return company_sector
    except TypeError:
        return error_message

def get_company_details(ticker_symbol_symbol):
    try:
        ticker_symbol_object = ticker.get_ticker(
            ticker_symbol_symbol)  # Gets the ticker_symbol object so you can access the various objects
        company_details = company_profile.get_company_summary_details(ticker_symbol_object, ticker_symbol_symbol)
        return company_details
    except TypeError:
        return error_message


def get_stock_name(ticker_symbol_symbol):
    try:
        ticker_symbol_object = ticker.get_ticker(
            ticker_symbol_symbol)  # Gets the ticker_symbol object so you can access the various objects
        stock_name = price_data.get_company_name(ticker_symbol_object, ticker_symbol_symbol)
        return stock_name
    except TypeError:
        return error_message

    ## Fundamentals ###


def get_current_stock_price(ticker_symbol_symbol):
    ticker_symbol_object = ticker.get_ticker(
        ticker_symbol_symbol)  # Gets the ticker_symbol object so you can access the various objects
    current_stock_price = price_data.get_current_stock_price(ticker_symbol_object, ticker_symbol_symbol)

    return current_stock_price


def get_eps(ticker_symbol_symbol):
    ticker_symbol_object = ticker.get_ticker(
        ticker_symbol_symbol)  # Gets the ticker_symbol object so you can access the various objects
    eps = summary_page.earnings_per_share(ticker_symbol_object, ticker_symbol_symbol)
    return eps


def get_pe_ratio(ticker_symbol_symbol):
    ticker_symbol_object = ticker.get_ticker(
        ticker_symbol_symbol)  # Gets the ticker_symbol object so you can access the various objects
    pe_ratio = summary_page.get_pe_ratio(ticker_symbol_object, ticker_symbol_symbol)

    return pe_ratio


def get_debt_to_equity(ticker_symbol):
    ticker_symbol_object = ticker.get_ticker(
        ticker_symbol)  # Gets the ticker_symbol object so you can access the various objects
    debt_to_equity_ratio = statistics_tab.get_debt_to_equity(ticker_symbol_object, ticker_symbol)

    return debt_to_equity_ratio


def get_return_on_equity(ticker_symbol):
    ticker_symbol_object = ticker.get_ticker(
        ticker_symbol)  # Gets the ticker_symbol object so you can access the various objects
    return_on_equity = statistics_tab.get_return_on_equity(ticker_symbol_object, ticker_symbol)

    return return_on_equity


def get_profit_margin(ticker_symbol):
    ticker_symbol_object = ticker.get_ticker(
        ticker_symbol)  # Gets the ticker_symbol object so you can access the various objects
    profit_margin = statistics_tab.get_profit_margins(ticker_symbol_object, ticker_symbol)

    return profit_margin


def get_cash_burn_number(ticker_symbol):
    global most_recent_cash_flow
    ticker_symbol_object = ticker.get_ticker(
        ticker_symbol)  # Gets the ticker_symbol object so you can access the various objects
    balance_sheet_data_frame = balance_sheet.get_balance_sheet_data(ticker_symbol_object, 'a')
    cash_flow_data_frame = cash_flow_page.get_cash_flow_data(ticker_symbol_object, 'a')

    cash_and_cash_equivalents = balance_sheet.get_cash_and_expenses(balance_sheet_data_frame,ticker_symbol)

    """
    because balance sheet does not have a TTM.## if the size of the cash flow data frame > balance sheet select
    the most recent year(not TTM)
    """
    try:
        if cash_flow_data_frame.shape[0] > balance_sheet_data_frame.shape[0]:
            most_recent_cash_flow = cash_flow_page.get_most_recent_cash_flow_total(cash_flow_data_frame, -2)

        cash_burn = cash_flow_page.calculate_cash_burn(cash_and_cash_equivalents, most_recent_cash_flow)

        ticker_symbol_name = get_stock_name(ticker_symbol)
        if cash_burn < 0:
            print(f'{ticker_symbol_name} is already running out of money. Their cash burn is:{cash_burn:,.1f} months')
        else:
          print(f'It will take {cash_burn:,.1f} months before {ticker_symbol_name} runs out of money')
    except Exception as e:
        print(f'yikes, seems like I cannot get the cash burn for {ticker_symbol} because "{e}"')