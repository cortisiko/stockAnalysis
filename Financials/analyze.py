from Financials import cashFlowSheet as cashFlowPage
from Financials import statistics as statisticsTab
from Financials import summary as summaryPage
from Financials import price as priceData

from Financials import incomeStatementSheet as income
from helpers import Ticker as ticker
from Financials import companyProfile as companyprofile

errorMessage = "Invalid Stock Symbol"


def getCompanySector(tickerSymbol):
    try:
        tickerObject = ticker.getTicker(tickerSymbol)  ## Gets the ticker object so you can access the various objects
        companySector = companyprofile.getCompanySector(tickerObject,tickerSymbol)
        return companySector
    except TypeError:
            return errorMessage

def getStockName(tickerSymbol):
    try:
        tickerObject = ticker.getTicker(tickerSymbol)  ## Gets the ticker object so you can access the various objects
        stockName = priceData.getCompanyName(tickerObject,tickerSymbol)
        return stockName
    except TypeError:
            return errorMessage

        ## Fundamentals ###
def getCurrentStockPrice(tickerSymbol):
    tickerObject = ticker.getTicker(tickerSymbol)  ## Gets the ticker object so you can access the various objects
    currentStockPrice = priceData.getCurrentStockPrice(tickerObject,tickerSymbol)

    return currentStockPrice

def getEPS(tickerSymbol):
    tickerObject = ticker.getTicker(tickerSymbol)  ## Gets the ticker object so you can access the various objects
    eps = summaryPage.getEarningsPerShare(tickerObject,tickerSymbol)
    return eps

def getPERatio(tickerSymbol):
    tickerObject = ticker.getTicker(tickerSymbol)  ## Gets the ticker object so you can access the various objects
    peRatio = summaryPage.getPERatio(tickerObject,tickerSymbol)

    return peRatio


def getDebtToEquity(tickerSymbol):
    tickerObject = ticker.getTicker(tickerSymbol)  ## Gets the ticker object so you can access the various objects
    debtToEquityRatio = statisticsTab.getDebtToEquity(tickerObject,tickerSymbol)

    return debtToEquityRatio

def getReturnOnEquity(tickerSymbol):
    tickerObject = ticker.getTicker(tickerSymbol)  ## Gets the ticker object so you can access the various objects
    returnOnEquity = statisticsTab.getReturnOnEquity(tickerObject,tickerSymbol)

    return returnOnEquity

def getProfitMargin(tickerSymbol):
    tickerObject = ticker.getTicker(tickerSymbol)  ## Gets the ticker object so you can access the various objects
    profitMargin = statisticsTab.getProfitMargins(tickerObject,tickerSymbol)

    return profitMargin