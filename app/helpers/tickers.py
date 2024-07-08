"""
Helper function to get stock ticker object
"""
from  yahooquery import Ticker


def get_ticker(ticker):
    """
    Helper function to get stock ticker object
    """
    try:
        if ticker is not None:
            stock_ticker = Ticker(ticker)
            return stock_ticker
        print("User did not enter a valid ticker")
    except (AttributeError, KeyError) as e:
        print(e)
    return None
