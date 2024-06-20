"""
This module provides functions to retrieve and process key statistics and summary details
It includes functions to get key statistics, summary details, EPS and PE ratio.

Functions:
    key_stats_data(ticker_object)
    summary_details_data(ticker_object)
    earnings_per_share(ticker_object, ticker_symbol)
    get_pe_ratio(ticker_object, ticker_symbol)
"""


# This is the summary tab

def key_stats_data(ticker_object):
    """
    Get key statistics data for a given ticker object.

    Args:
        ticker_object (object): The ticker object.

    Returns:
        dict: A dictionary containing key statistics data.
    """
    try:
        return ticker_object.key_stats
    except Exception as e:
        print(e)
        return None


def summary_details_data(ticker_object):
    """
    Get summary details data for a given ticker object.

    Args:
        ticker_object (object): The ticker object.

    Returns:
        dict: A dictionary containing summary details data.
    """
    try:
        return ticker_object.summary_detail
    except Exception as e:
        print(e)
        return None


def earnings_per_share(ticker_object, ticker_symbol):
    """
    Get the earnings per share (EPS) for a given ticker object and symbol.

    Args:
        ticker_object (object): The ticker object.
        ticker_symbol (str): The stock ticker symbol.

    Returns:
        float: The trailing earnings per share rounded to 2 decimal places.
    """
    try:
        key_stats = key_stats_data(ticker_object)
        if key_stats:
            trailing_earning_per_share = key_stats[ticker_symbol].get("trailingEps", None)
            if trailing_earning_per_share is not None:
                return float(round(trailing_earning_per_share, 2))
            print("There is no EPS Ratio for", ticker_symbol)
        return None
    except KeyError as e:
        print(f"KeyError: {e}")
        return None


def get_pe_ratio(ticker_object, ticker_symbol):
    """
    Get the price-to-earnings (PE) ratio for a given ticker object and symbol.

    Args:
        ticker_object (object): The ticker object.
        ticker_symbol (str): The stock ticker symbol.

    Returns:
        float: The PE ratio rounded to 2 decimal places.
    """
    try:
        summary_data = summary_details_data(ticker_object)
        if summary_data:
            pe_ratio = summary_data[ticker_symbol].get("trailingPE", None)
            if pe_ratio is not None:
                return float(round(pe_ratio, 2))
            print("There is no PE Ratio for", ticker_symbol)
        return None
    except KeyError as e:
        print(f"KeyError: {e}")
        return None
