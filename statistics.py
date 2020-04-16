## This is the statistics page in yahoo finance

import pandas as pd

def getStatistics(tickerObject):
    allFinancialData = tickerObject.financial_data
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', -1)

    return allFinancialData

def getCurrentStockPrice(tickerObject,tickerSymbol):
    summaryData = getStatistics(tickerObject)
    currentStockPrice = summaryData[tickerSymbol]['currentPrice']
    currentStockPrice = float(round(currentStockPrice, 2))

    return currentStockPrice


def getDebtToEquity(tickerObject,tickerSymbol):
    financialData = getStatistics(tickerObject)
    debtToEquity = financialData[tickerSymbol].get('debtToEquity', None)

    if debtToEquity is not None:
        debtToEquity = float(round(debtToEquity, 2))
        return   debtToEquity
    else:
        return   print("No Debt to Equity Ratio for",tickerSymbol)


def getReturnOnEquity(tickerObject,tickerSymbol):
    financialData = getStatistics(tickerObject)
    returnOnEquity = financialData[tickerSymbol].get('returnOnEquity', None)

    if returnOnEquity is not None:
        returnOnEquity = float(round(returnOnEquity, 2))
        return returnOnEquity
    else:
        return print("No return on equity ratio for",tickerSymbol)


def getProfitMargins(tickerObject,tickerSymbol):
    financialData = getStatistics(tickerObject)
    profitMargins = financialData[tickerSymbol].get('profitMargins', None)

    if profitMargins is not None:
        profitMargins = float(round(profitMargins * 100, 2))
        return profitMargins
    else:
        return print("No net profit margin for",tickerSymbol)
