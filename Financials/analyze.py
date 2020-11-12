from Financials import cashFlowSheet as cashFlowPage
from Financials import statistics as statisticsTab
from Financials import summary as summaryPage
from Financials import price as priceData

from Financials import balanceSheet as balancesheet
from helpers import Ticker as ticker
from Financials import companyProfile as companyprofile

errorMessage = "Invalid Stock Symbol"


def get_company_sector(ticker_symbol):
    try:
        ticker_object = ticker.getTicker(ticker_symbol)  ## Gets the ticker object so you can access the various objects
        companySector = companyprofile.get_company_sector(ticker_object, ticker_symbol)
        return companySector
    except TypeError:
        return errorMessage


def getCompanyDetails(ticker_symbol):
    try:
        ticker_object = ticker.getTicker(ticker_symbol)  ## Gets the ticker object so you can access the various objects
        companyDetails = companyprofile.getCompanySummaryDetails(ticker_object, ticker_symbol)
        return companyDetails
    except TypeError:
        return errorMessage


def getStockName(ticker_symbol):
    try:
        ticker_object = ticker.getTicker(ticker_symbol)  ## Gets the ticker object so you can access the various objects
        stockName = priceData.getCompanyName(ticker_object, ticker_symbol)
        return stockName
    except TypeError:
        return errorMessage

    ## Fundamentals ###


def getCurrentStockPrice(ticker_symbol):
    ticker_object = ticker.getTicker(ticker_symbol)  ## Gets the ticker object so you can access the various objects
    currentStockPrice = priceData.getCurrentStockPrice(ticker_object, ticker_symbol)

    return currentStockPrice


def getEPS(ticker_symbol):
    ticker_object = ticker.getTicker(ticker_symbol)  ## Gets the ticker object so you can access the various objects
    eps = summaryPage.getEarningsPerShare(ticker_object, ticker_symbol)
    return eps


def getPERatio(ticker_symbol):
    ticker_object = ticker.getTicker(ticker_symbol)  ## Gets the ticker object so you can access the various objects
    peRatio = summaryPage.getPERatio(ticker_object, ticker_symbol)

    return peRatio


def getDebtToEquity(ticker_symbol):
    ticker_object = ticker.getTicker(ticker_symbol)  ## Gets the ticker object so you can access the various objects
    debtToEquityRatio = statisticsTab.getDebtToEquity(ticker_object, ticker_symbol)

    return debtToEquityRatio


def getReturnOnEquity(ticker_symbol):
    ticker_object = ticker.getTicker(ticker_symbol)  ## Gets the ticker object so you can access the various objects
    returnOnEquity = statisticsTab.getReturnOnEquity(ticker_object, ticker_symbol)

    return returnOnEquity


def getProfitMargin(ticker_symbol):
    ticker_object = ticker.getTicker(ticker_symbol)  ## Gets the ticker object so you can access the various objects
    profitMargin = statisticsTab.getProfitMargins(ticker_object, ticker_symbol)

    return profitMargin


def getCashBurnNumber(ticker_symbol):
    global mostRecentCashFlow
    ticker_object = ticker.getTicker(ticker_symbol)  ## Gets the ticker object so you can access the various objects
    balanceSheetDataFrame = balancesheet.getBalanceSheetData(ticker_object, Frequency='a')
    cashFlowDataFrame = cashFlowPage.getCashFlowData(ticker_object, Frequency='a')

    CashAndCashEquivalents = balancesheet.getCashAndExpenses(balanceSheetDataFrame)

    ## because balance sheet does not have a TTM.## if the size of the cash flow data frame > balance sheet select
    ## the most recent year(not TTM)
    if cashFlowDataFrame.shape[0] > balanceSheetDataFrame.shape[0]:
        mostRecentCashFlow = cashFlowPage.getMostRecentCashFlowTotal(cashFlowDataFrame, -2)

    cashBurn = cashFlowPage.calculateCashBurn(CashAndCashEquivalents, mostRecentCashFlow)

    tickerName = getStockName(ticker_symbol)
    if cashBurn < 0:
        print(f'{tickerName} is already running out of money. Their cash burn is:{cashBurn:,.1f} months')
    else:
        print(f'It will take {cashBurn:,.1f} months before {tickerName} runs out of money')
