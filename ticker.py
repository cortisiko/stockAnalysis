from yahooquery import Ticker


def getTicker(ticker):
        stockTicker = Ticker(ticker)
        return stockTicker