"""
This module provides functions to retrieve and process income statement data from Yahoo Finance.
It includes functions to get the income statement, net income, and earnings per share (EPS).

Functions:
    get_income_statement(ticker_object, frequency)
    get_net_income(income_statement_data)
    get_earnings_per_share(income_statement_data)
"""


# This is the income statement tab on the financials page in yahoo finance


def get_income_statement(ticker_object, frequency):
    """
    Get income statement data for a given ticker object and frequency.

    Args:
        ticker_object (object): The ticker object.
        frequency (str): The frequency of the data ('a' for annual, 'q' for quarterly).

    Returns:
        DataFrame: A DataFrame containing the income statement data.
    """
    try:
        income_statements = ticker_object.income_statement(frequency)
        return income_statements
    except (AttributeError, KeyError, TypeError, ValueError) as e:
        print(e)
    return None


def get_net_income(income_statement_data):
    """
    Get the net income from the income statement data.

    Args:
        income_statement_data (DataFrame): The DataFrame containing income statement data.

    Returns:
        float: The net income in thousands.
    """
    try:
        net_income = income_statement_data["NetIncome"]
        if net_income is not None:
            net_income = net_income / 1e3
            return net_income
        print("There is no net income for", net_income)
    except (AttributeError, KeyError, TypeError, ValueError) as e:
        print(f"KeyError: {e}")
    return None


def get_earnings_per_share(income_statement_data):
    """
    Get the basic earnings per share (EPS) from the income statement data.

    Args:
        income_statement_data (DataFrame): The DataFrame containing income statement data.

    Returns:
        float: The basic EPS.
    """
    try:
        basic_eps = income_statement_data["BasicEPS"]
        if basic_eps is not None:
            return basic_eps
        print("There is no basic EPS for", basic_eps)
    except (AttributeError, KeyError, TypeError, ValueError) as e:
        print(f"Error: {e}")
    return None
