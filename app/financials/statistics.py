"""
This module provides functions to retrieve and process stock statistics data from Yahoo Finance.
It includes functions to get stock statistics, current stock price, debt to equity ratio,
return on equity, and profit margins.

Functions:
    get_stock_statistics(ticker_object)
    get_current_stock_price(ticker_object, ticker_symbol)
    get_debt_to_equity(ticker_object, ticker_symbol)
    get_return_on_equity(ticker_object, ticker_symbol)
    get_profit_margins(ticker_object, ticker_symbol)
"""


# This is the statistics page in Yahoo Finance

def get_stock_statistics(ticker_object):
    """
    Get stock statistics data for a given ticker object.

    Args:
        ticker_object (object): The ticker object.

    Returns:
        dict: A dictionary containing all financial data.
    """
    try:
        return ticker_object.financial_data
    except (AttributeError, KeyError, TypeError, ValueError) as e:
        print(e)
    return None

def get_current_stock_price(ticker_object, ticker_symbol):
    """
    Get the current stock price for a given ticker object and symbol.

    Args:
        ticker_object (object): The ticker object.
        ticker_symbol (str): The stock ticker symbol.

    Returns:
        float: The current stock price rounded to 2 decimal places.
    """
    try:
        summary_data = get_stock_statistics(ticker_object)
        current_stock_price = summary_data[ticker_symbol]["currentPrice"]
        current_stock_price = float(round(current_stock_price, 2))
        return current_stock_price
    except (AttributeError, KeyError, TypeError, ValueError) as e:
        print(f"KeyError: {e}")
    return None


def get_debt_to_equity(ticker_object, ticker_symbol):
    """
    Get the debt to equity ratio for a given ticker object and symbol.

    Args:
        ticker_object (object): The ticker object.
        ticker_symbol (str): The stock ticker symbol.

    Returns:
        float: The debt to equity ratio rounded to 2 decimal places.
    """
    try:
        financial_data = get_stock_statistics(ticker_object)
        debt_to_equity = financial_data[ticker_symbol].get("debtToEquity", None)
        if debt_to_equity is not None:
            debt_to_equity = debt_to_equity / 100
            debt_to_equity = float(round(debt_to_equity, 2))
            return debt_to_equity
        print("There is no Debt to Equity Ratio for", ticker_symbol)
    except (AttributeError, KeyError, TypeError, ValueError) as e:
        print(f"KeyError: {e}")
    return None



def get_return_on_equity(ticker_object, ticker_symbol):
    """
    Get the return on equity ratio for a given ticker object and symbol.

    Args:
        ticker_object (object): The ticker object.
        ticker_symbol (str): The stock ticker symbol.

    Returns:
        float: The return on equity ratio rounded to 2 decimal places.
    """
    try:
        financial_data = get_stock_statistics(ticker_object)
        return_on_equity = financial_data[ticker_symbol].get("returnOnEquity", None)
        if return_on_equity is not None:
            return_on_equity = float(round(return_on_equity * 100, 2))
            return return_on_equity
        print("There is no return on equity ratio for", ticker_symbol)
    except (AttributeError, KeyError, TypeError, ValueError) as e:
        print(f"KeyError: {e}")
    return None


def get_profit_margins(ticker_object, ticker_symbol):
    """
    Get the profit margins for a given ticker object and symbol.

    Args:
        ticker_object (object): The ticker object.
        ticker_symbol (str): The stock ticker symbol.

    Returns:
        float: The profit margins rounded to 2 decimal places.
    """
    try:
        financial_data = get_stock_statistics(ticker_object)
        profit_margins = financial_data[ticker_symbol].get("profitMargins", None)
        if profit_margins is not None:
            profit_margins = float(round(profit_margins * 100, 2))
            return profit_margins
        print("There is no net profit margin for", ticker_symbol)
    except (AttributeError, KeyError, TypeError, ValueError) as e:
        print(f"KeyError: {e}")
    return None
