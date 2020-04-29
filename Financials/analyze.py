from Financials import cashFlowSheet as cashFlowPage
from Financials import statistics as statisticsTab
from Financials import summary as summaryPage
from Financials import price as priceData

from Financials import incomeStatementSheet as income
from helpers import Ticker as ticker
from helpers import plotChart as plot
from helpers import getDate as date

Frequency = 'a'

def graphFreeCashFlow(tickerSymbol,root):
    tickerObject = ticker.getTicker(tickerSymbol)  ## Gets the ticker object so you can access the various objects
    cashFlowDataFrame = cashFlowPage.getCashFlowData(tickerObject, Frequency)
    freeCashFlow = cashFlowPage.getFreeCashFlow(cashFlowDataFrame)
    companyName = priceData.getCompanyName(tickerObject,tickerSymbol)
    dates = date.getDates(cashFlowDataFrame)
    cashFlowGraphTitle = 'Free cash flow '
    plot.plotGraph(dates, freeCashFlow, companyName, cashFlowGraphTitle,root)  ## plotting free cash flow



def getStockName(tickerSymbol):
    tickerObject = ticker.getTicker(tickerSymbol)  ## Gets the ticker object so you can access the various objects
    stockName = priceData.getCompanyName(tickerObject,tickerSymbol)

    return stockName

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