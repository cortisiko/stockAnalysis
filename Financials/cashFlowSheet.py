## This is the cashflow tab on the financials page in yahoo finance

import pandas as pd

def getCashFlowData(tickerObject,Frequency):
    cashFlowData = tickerObject.cash_flow(frequency=Frequency)
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', -1)

    return cashFlowData


def getFreeCashFlow(cashFlowData):
     freeCashFlow = cashFlowData['FreeCashFlow']
     freeCashFlow = freeCashFlow / 1e3
     #freeCashFlow = cashFlowData['FreeCashFlow'].astype(str)

     return freeCashFlow