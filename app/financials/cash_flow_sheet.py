"""
This module provides functions to retrieve and process cash flow data from Yahoo Finance.
It includes functions to get cash flow data, free cash flow, operating cash flow, most recent
cash flow total, and calculate the cash burn.

Functions:
    get_cash_flow_data(ticker_object, frequency)
    get_free_cash_flow(cash_flow_data)
    get_operating_cash_flow(cash_flow_data)
    get_most_recent_cash_flow_total(cash_flow_data, position)
    calculate_cash_burn(cash_and_cash_equivalents, free_cash_flow)
"""

# This is the cashflow tab on the financials page in yahoo finance


def get_cash_flow_data(ticker_object, frequency):
    """
    Get cash flow data for a given ticker object and frequency.

    Args:
        ticker_object (object): The ticker object.
        frequency (str): The frequency of the data ('a' for annual, 'q' for quarterly).

    Returns:
        DataFrame: A DataFrame containing the cash flow data.
    """
    cash_flow_data = ticker_object.cash_flow(frequency=frequency)
    return cash_flow_data


def get_free_cash_flow(cash_flow_data):
    """
    Get the free cash flow from the cash flow data.

    Args:
        cash_flow_data (DataFrame): The DataFrame containing cash flow data.

    Returns:
        float: The free cash flow in thousands.
    """
    free_cash_flow = cash_flow_data["FreeCashFlow"]
    free_cash_flow = free_cash_flow / 1e3

    return free_cash_flow


def get_operating_cash_flow(cash_flow_data):
    """
    Get the operating cash flow from the cash flow data.

    Args:
        cash_flow_data (DataFrame): The DataFrame containing cash flow data.

    Returns:
        float: The operating cash flow in thousands.
    """
    operating_cash_flow = cash_flow_data["OperatingCashFlow"]
    operating_cash_flow = operating_cash_flow / 1e3

    return operating_cash_flow


def get_most_recent_cash_flow_total(cash_flow_data, position):
    """
    Get the most recent free cash flow total from the cash flow data.

    Args:
        cash_flow_data (DataFrame): The DataFrame containing cash flow data.
        position (int): The position of the data to retrieve (e.g., -1 for most recent).

    Returns:
        float: The most recent free cash flow total in thousands.
    """
    try:
        most_recent_cash_flow = cash_flow_data["FreeCashFlow"].iloc[
            position
        ]  ## takes the most recent cashflow
        most_recent_cash_flow = most_recent_cash_flow / 1e3
        return most_recent_cash_flow
    except Exception as e:
        print(e)


def calculate_cash_burn(cash_and_cash_equivalents, free_cash_flow):
    """
    Calculate the cash burn given cash and cash equivalents and free cash flow.

    Args:
        cash_and_cash_equivalents (float): The cash and cash equivalents in thousands.
        free_cash_flow (float): The free cash flow in thousands.

    Returns:
        float: The cash burn in months.
    """
    cash_burn = cash_and_cash_equivalents / free_cash_flow
    cash_burn = cash_burn * 12

    return cash_burn
