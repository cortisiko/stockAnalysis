from yahooquery import Ticker


def getTicker(ticker):
        if ticker is not None:
                stockTicker = Ticker(ticker)
                return stockTicker
        else:
                return print("User did not enter a valid ticker")
