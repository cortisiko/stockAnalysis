"""
method to get earnings
"""


def get_earnings_data(ticker_symbol):
    """
    method to get earnings
    """
    try:
        earnings = ticker_symbol.earnings
        return earnings
    except (AttributeError, KeyError, TypeError, ValueError) as e:
        print(e)
        return None
