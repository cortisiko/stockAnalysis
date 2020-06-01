## This is the cashflow tab on the financials page in yahoo finance

def getCashFlowData(tickerObject,Frequency):
    cashFlowData = tickerObject.cash_flow(frequency=Frequency)
    return cashFlowData


def getFreeCashFlow(cashFlowData):
     freeCashFlow = cashFlowData['FreeCashFlow']
     freeCashFlow = freeCashFlow / 1e3

     return freeCashFlow

def getMostRecentCashFlowTotal(cashFlowData):
    mostRecentCashFlow = cashFlowData['FreeCashFlow'].iloc[-1] ## takes the most recent cashflow
    mostRecentCashFlow = mostRecentCashFlow / 1e3

    return mostRecentCashFlow


def calculateCashBurn(CashAndCashEquivalents,freeCashFlow):
    cashBurn = CashAndCashEquivalents / freeCashFlow
    cashBurn = cashBurn * 12

    return cashBurn