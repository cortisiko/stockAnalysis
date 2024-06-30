"""
This module provides various functions to retrieve financial information and statistics
about companies based on their stock ticker symbols. It includes functions to get company
sector, details, stock name, current stock price, EPS, PE ratio, debt to equity ratio, 
return on equity, profit margin, and cash burn number.

Modules:
    statistics_tab: Handles statistical data retrieval.
    balance_sheet: Handles balance sheet data retrieval.
    company_profile: Handles company profile data retrieval.
    cash_flow_page: Handles cash flow data retrieval.
    summary_page: Handles summary data retrieval.
    price_data: Handles price data retrieval.
    ticker: Handles ticker symbol retrieval.

Constants:
    ERROR_MESSAGE (str): Error message to return in case of invalid stock symbol.

Functions:
    get_company_sector(ticker_symbol)
    get_company_details(ticker_symbol_symbol)
    get_stock_name(ticker_symbol_symbol)
    get_current_stock_price(ticker_symbol_symbol)
    get_eps(ticker_symbol_symbol)
    get_pe_ratio(ticker_symbol_symbol)
    get_debt_to_equity(ticker_symbol)
    get_return_on_equity(ticker_symbol)
    get_profit_margin(ticker_symbol)
    get_cash_burn_number(ticker_symbol)
"""

import logging

from app.financials import (
    statistics as statistics_tab,
    balance_sheet,
    company_profile,
    cash_flow_sheet as cash_flow_page,
    summary as summary_page,
    price as price_data,
)

from app.helpers import tickers as ticker

ERROR_MESSAGE = "Invalid Stock Symbol"


def get_company_sector(ticker_symbol):
    """
    Get the sector of a company given its stock ticker symbol.

    Args:
        ticker_symbol (str): The stock ticker symbol.

    Returns:
        str: The sector of the company or an error message if the stock symbol is invalid.
    """
    try:
        ticker_symbol_object = ticker.get_ticker(
            ticker_symbol
        )  # Gets the ticker_symbol object so you can access the various objects
        company_sector = company_profile.get_company_sector(
            ticker_symbol_object, ticker_symbol
        )
        return company_sector
    except TypeError:
        return ERROR_MESSAGE


def get_company_details(ticker_symbol_symbol):
    """
    Get detailed information about a company given its stock ticker symbol.

    Args:
        ticker_symbol_symbol (str): The stock ticker symbol.

    Returns:
    dict: A dictionary containing company details or an error message if the stock symbol is invalid
    """
    try:
        ticker_symbol_object = ticker.get_ticker(
            ticker_symbol_symbol
        )  # Gets the ticker_symbol object so you can access the various objects
        company_details = company_profile.get_company_summary_details(
            ticker_symbol_object, ticker_symbol_symbol
        )
        return company_details
    except TypeError:
        return ERROR_MESSAGE


def get_stock_name(ticker_symbol_symbol):
    """
    Get the name of the stock given its ticker symbol.

    Args:
        ticker_symbol_symbol (str): The stock ticker symbol.

    Returns:
        str: The name of the stock or an error message if the stock symbol is invalid.
    """
    try:
        ticker_symbol_object = ticker.get_ticker(
            ticker_symbol_symbol
        )  # Gets the ticker_symbol object so you can access the various objects
        stock_name = price_data.get_company_name(
            ticker_symbol_object, ticker_symbol_symbol
        )
        return stock_name
    except TypeError:
        return ERROR_MESSAGE


def get_current_stock_price(ticker_symbol_symbol):
    """
    Get the current price of the stock given its ticker symbol.

    Args:
        ticker_symbol_symbol (str): The stock ticker symbol.

    Returns:
        float: The current stock price.
    """
    ticker_symbol_object = ticker.get_ticker(
        ticker_symbol_symbol
    )  # Gets the ticker_symbol object so you can access the various objects
    current_stock_price = price_data.get_current_stock_price(
        ticker_symbol_object, ticker_symbol_symbol
    )

    return current_stock_price


def get_eps(ticker_symbol_symbol):
    """
    Get the earnings per share (EPS) of the stock given its ticker symbol.

    Args:
        ticker_symbol_symbol (str): The stock ticker symbol.

    Returns:
        float: The earnings per share (EPS).
    """
    ticker_symbol_object = ticker.get_ticker(
        ticker_symbol_symbol
    )  # Gets the ticker_symbol object so you can access the various objects
    eps = summary_page.earnings_per_share(ticker_symbol_object, ticker_symbol_symbol)
    return eps


def get_pe_ratio(ticker_symbol_symbol):
    """
    Get the price-to-earnings (PE) ratio of the stock given its ticker symbol.

    Args:
        ticker_symbol_symbol (str): The stock ticker symbol.

    Returns:
        float: The PE ratio.
    """
    ticker_symbol_object = ticker.get_ticker(
        ticker_symbol_symbol
    )  # Gets the ticker_symbol object so you can access the various objects
    pe_ratio = summary_page.get_pe_ratio(ticker_symbol_object, ticker_symbol_symbol)

    return pe_ratio


def get_debt_to_equity(ticker_symbol):
    """
    Get the debt-to-equity ratio of the company given its stock ticker symbol.

    Args:
        ticker_symbol (str): The stock ticker symbol.

    Returns:
        float: The debt-to-equity ratio.
    """
    ticker_symbol_object = ticker.get_ticker(
        ticker_symbol
    )  # Gets the ticker_symbol object so you can access the various objects
    debt_to_equity_ratio = statistics_tab.get_debt_to_equity(
        ticker_symbol_object, ticker_symbol
    )

    return debt_to_equity_ratio


def get_return_on_equity(ticker_symbol):
    """
    Get the return on equity (ROE) of the company given its stock ticker symbol.

    Args:
        ticker_symbol (str): The stock ticker symbol.

    Returns:
        float: The return on equity (ROE).
    """
    ticker_symbol_object = ticker.get_ticker(
        ticker_symbol
    )  # Gets the ticker_symbol object so you can access the various objects
    return_on_equity = statistics_tab.get_return_on_equity(
        ticker_symbol_object, ticker_symbol
    )

    return return_on_equity


def get_profit_margin(ticker_symbol):
    """
    Get the profit margin of the company given its stock ticker symbol.

    Args:
        ticker_symbol (str): The stock ticker symbol.

    Returns:
        float: The profit margin.
    """
    ticker_symbol_object = ticker.get_ticker(
        ticker_symbol
    )  # Gets the ticker_symbol object so you can access the various objects
    profit_margin = statistics_tab.get_profit_margins(
        ticker_symbol_object, ticker_symbol
    )

    return profit_margin


def get_cash_burn_number(ticker_symbol):
    """
    Calculate the cash burn number of the company given its stock ticker symbol.

    Args:
        ticker_symbol (str): The stock ticker symbol.

    Returns:
        None
    """

    ticker_symbol_object = ticker.get_ticker(
        ticker_symbol
    )  # Gets the ticker_symbol object so you can access the various objects
    balance_sheet_data_frame = balance_sheet.get_balance_sheet_data(
        ticker_symbol_object, "a"
    )
    cash_flow_data_frame = cash_flow_page.get_cash_flow_data(ticker_symbol_object, "a")

    cash_and_cash_equivalents = balance_sheet.get_cash_and_expenses(
        balance_sheet_data_frame, ticker_symbol
    )

    # pylint: disable=pointless-string-statement
    """
    because balance sheet does not have a TTM.## 
    if the size of the cash flow data frame > balance sheet select
    the most recent year(not TTM)
    """
    # pylint: disable=global-variable-undefined
    most_recent_cash_flow = None
    try:
        if cash_flow_data_frame.shape[0] > balance_sheet_data_frame.shape[0]:
            most_recent_cash_flow = cash_flow_page.get_most_recent_cash_flow_total(
                cash_flow_data_frame, -2
            )

        cash_burn = cash_flow_page.calculate_cash_burn(
            # pylint: disable=used-before-assignment
            cash_and_cash_equivalents, most_recent_cash_flow
        )

        ticker_symbol_name = get_stock_name(ticker_symbol)
        if cash_burn < 0:
            print(
                # pylint: disable=line-too-long
                f"{ticker_symbol_name} is running out of money. Their cash burn is:{cash_burn:,.1f} months"
            )
        else:
            print(
                # pylint: disable=line-too-long
                f"It will take {cash_burn:,.1f} months before {ticker_symbol_name} runs out of money"
            )
    except (AttributeError, KeyError, TypeError, ValueError) as e:
        logging.error('Failed to calculate cash burn for %s: "%s"', ticker_symbol, e)
