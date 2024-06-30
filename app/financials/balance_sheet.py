"""
This module provides functions to retrieve and process balance sheet data from Yahoo Finance.
It includes functions to get balance sheet data, long-term debt, and cash and cash equivalents.

Constants:
    ERROR_MESSAGE (str): Error message to print in case the company does not have debt.

Functions:
    get_balance_sheet_data(ticker_symbol, frequency)
    get_long_term_debt(long_term_debt_data)
    get_cash_and_expenses(balance_sheet_data, ticker_symbol)
"""

ERROR_MESSAGE = "Company Does not have debt"


def get_balance_sheet_data(ticker_symbol, frequency):
    """
    Get balance sheet data for a given ticker symbol and frequency.

    Args:
        ticker_symbol (object): The ticker symbol object.
        frequency (str): The frequency of the data ('a' for annual, 'q' for quarterly).

    Returns:
        DataFrame: A DataFrame containing the balance sheet data.
    """
    try:
        balance_sheet_data = ticker_symbol.balance_sheet(frequency)
        return balance_sheet_data

    except (AttributeError, KeyError, TypeError, ValueError) as e:
        print(e)
        return None

def get_long_term_debt(long_term_debt_data):
    """
    Get the long-term debt from the balance sheet data.

    Args:
        long_term_debt_data (DataFrame): The DataFrame containing long-term debt data.

    Returns:
        float: The long-term debt in thousands.
    """
    try:
        long_term_debt = long_term_debt_data["LongTermDebt"]
        long_term_debt = long_term_debt / 1e3

        return long_term_debt
    except (AttributeError, KeyError, TypeError, ValueError) as e:
        print(ERROR_MESSAGE,e)
        return None

def get_cash_and_expenses(balance_sheet_data, ticker_symbol):
    """
    Get the cash and cash equivalents from the balance sheet data for the most recent year.

    Args:
        balance_sheet_data (DataFrame): The DataFrame containing balance sheet data.
        ticker_symbol (str): The stock ticker symbol.

    Returns:
        float: The cash and cash equivalents in thousands.
    """
    try:
        cash_and_cash_equivalents = balance_sheet_data["CashAndCashEquivalents"].iloc[
            -1
        ]  ## getting the data for the most recent year
        cash_and_cash_equivalents = cash_and_cash_equivalents / 1e3
        return cash_and_cash_equivalents
    except (AttributeError, KeyError, TypeError, ValueError) as e:
        print(f"I do not see anything on the balance sheet for {ticker_symbol}")
        print(f"KeyError: {e}")
        return None
