from Financials import cashFlowSheet as cashFlowPage
from Financials import statistics as statisticsTab
from Financials import summary as summaryPage
from Financials import price as priceData

from Financials import balanceSheet as balancesheet
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
def getCompanyDetails(tickerSymbol):
    try:
        tickerObject = ticker.getTicker(tickerSymbol)  ## Gets the ticker object so you can access the various objects
        companyDetails = companyprofile.getCompanySummaryDetails(tickerObject,tickerSymbol)
        return companyDetails
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

def getCashBurnNumber(tickerSymbol):
    global mostRecentCashFlow
    tickerObject = ticker.getTicker(tickerSymbol)  ## Gets the ticker object so you can access the various objects
    balanceSheetDataFrame = balancesheet.getBalanceSheetData(tickerObject, Frequency='a')
    cashFlowDataFrame = cashFlowPage.getCashFlowData(tickerObject, Frequency='a')

    CashAndCashEquivalents = balancesheet.getCashAndExpenses(balanceSheetDataFrame)

    ## because balance sheet does not have a TTM.## if the size of the cash flow data frame > balance sheet select
    ## the most recent year(not TTM)
    if cashFlowDataFrame.shape[0] > balanceSheetDataFrame.shape[0]:
        mostRecentCashFlow = cashFlowPage.getMostRecentCashFlowTotal(cashFlowDataFrame,-2)

    cashBurn = cashFlowPage.calculateCashBurn(CashAndCashEquivalents, mostRecentCashFlow)

    tickerName = getStockName(tickerSymbol)
    if cashBurn < 0:
        print(f'{tickerName} is already running out of money. their cash burn is: {cashBurn:,.1f} months')
    else:
        print(f'It will take {cashBurn:,.1f} months before {tickerName} runs out of money')
