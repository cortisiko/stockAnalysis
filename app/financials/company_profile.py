"""
This module provides functions to retrieve and process company profile data.
It includes functions to get the company profile, sector, and summary details.

Functions:
    get_company_profile(ticker_object)
    get_company_sector(ticker_object, ticker_symbol)
    get_company_summary_details(ticker_object, ticker_symbol)
"""


def get_company_profile(ticker_object):
    """
    Get the company profile for a given ticker object.

    Args:
        ticker_object (object): The ticker object.

    Returns:
        dict: A dictionary containing the company profile.
    """
    try:
        company_profile = ticker_object.summary_profile
        return company_profile
    except Exception as e:
        print(e)


def get_company_sector(ticker_object, ticker_symbol):
    """
    Get the sector of the company given its ticker object and symbol.

    Args:
        ticker_object (object): The ticker object.
        ticker_symbol (str): The stock ticker symbol.

    Returns:
        str: The sector of the company.
    """
    try:
        company_profile_object = get_company_profile(ticker_object)
        company_sector = company_profile_object[ticker_symbol]["sector"]
        return company_sector
    except Exception as e:
        print(e)


def get_company_summary_details(ticker_object, ticker_symbol):
    """
    Get the summary details of the company given its ticker object and symbol.

    Args:
        ticker_object (object): The ticker object.
        ticker_symbol (str): The stock ticker symbol.

    Returns:
        str: The long business summary of the company.
    """
    try:
        company_profile_object = get_company_profile(ticker_object)
        summary_details = company_profile_object[ticker_symbol]["longBusinessSummary"]
        return summary_details
    except Exception as e:
        print(e)
