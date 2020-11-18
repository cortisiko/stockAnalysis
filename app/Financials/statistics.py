# This is the statistics page in yahoo finance


def get_statistics(ticker_object):
    all_financial_data = ticker_object.financial_data
    return all_financial_data


def get_current_stock_price(ticker_object, ticker_symbol):
    summaryData = get_statistics(ticker_object)
    current_stock_price = summaryData[ticker_symbol]['currentPrice']
    current_stock_price = float(round(current_stock_price, 2))

    return current_stock_price


def get_debt_to_equity(ticker_object, ticker_symbol):
    financial_data = get_statistics(ticker_object)
    debt_to_equity = financial_data[ticker_symbol].get('debtToEquity', None)

    if debt_to_equity is not None:
        debt_to_equity = debt_to_equity / 100
        debt_to_equity = float(round(debt_to_equity, 2))
        return debt_to_equity
    else:
        return print("There is no Debt to Equity Ratio for", ticker_symbol)


def get_return_on_equity(ticker_object, ticker_symbol):
    financial_data = get_statistics(ticker_object)
    return_on_equity = financial_data[ticker_symbol].get('returnOnEquity', None)

    if return_on_equity is not None:
        return_on_equity = float(round(return_on_equity * 100, 2))
        return return_on_equity
    else:
        return print("There is no return on equity ratio for", ticker_symbol)


def get_profit_margins(ticker_object, ticker_symbol):
    financialData = get_statistics(ticker_object)
    profit_margins = financialData[ticker_symbol].get('profitMargins', None)

    if profit_margins is not None:
        profit_margins = float(round(profit_margins * 100, 2))
        return profit_margins
    else:
        return print("There is no net profit margin for", ticker_symbol)
