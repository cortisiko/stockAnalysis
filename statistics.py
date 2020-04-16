import pandas as pd

def getStatistics(ticker):
    allFinancialData = ticker.financial_data
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', -1)

    return allFinancialData

def getDebtToEquity(financialData,ticker):
    debtToEquity = financialData[ticker].get('debtToEquity', None)
    if debtToEquity is not None:
        return   print("this is the debt to equity ratio MRQ: {:0.2f}\n".format(debtToEquity))
    else:
        return   print("No Debt to Equity Ratio here here")


def getReturnOnEquity(financialData,ticker):
    returnOnEquity = financialData[ticker].get('returnOnEquity', None)
    if returnOnEquity is not None:
        return  print("this is the return on equity ratio TTM: {:0.2f}\n".format(returnOnEquity))
    else:
        return print("No return on equity ratio here")


def getProfitMargins(financialData,ticker):
    profitMargins = financialData[ticker].get('profitMargins', None)
    if profitMargins is not None:
       return print("The net profit margin is: {:0.2f}\n".format(profitMargins))
    else:
        return print("No net profit margin here")
