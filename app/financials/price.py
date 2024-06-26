"""
File that contains helper functions for getting the stock price, and company name
"""


def get_price_data_object(ticker_object):
    """
    Function to get the price data object
    :param ticker_object:
    :return: price object
    """
    if ticker_object is not None:
        price_object = ticker_object.price
        return price_object
    print("User did not enter a valid ticker")
    return None


def get_current_stock_price(ticker_object, ticker_symbol):
    """
     Function to get the current stock price
     :param ticker_object:
     :return: price object
     """
    price_object = get_price_data_object(ticker_object)
    current_stock_price = price_object[ticker_symbol]["regularMarketPrice"]
    current_stock_price = float(round(current_stock_price, 2))

    return current_stock_price


def get_company_name(ticker_object, ticker_symbol):
    """
     Function to get the company name
     :param ticker_object:
     :return: price object
     """

    price_object = get_price_data_object(ticker_object)
    company_name = price_object[ticker_symbol]["shortName"]

    return company_name
