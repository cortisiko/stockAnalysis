from yahooquery import Ticker


def get_ticker(ticker):
        if ticker is not None:
                stock_ticker = Ticker(ticker)
                return stock_ticker
        else:
         print("User did not enter a valid ticker")
