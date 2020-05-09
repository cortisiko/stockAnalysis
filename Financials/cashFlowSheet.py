## This is the cashflow tab on the financials page in yahoo finance

def getCashFlowData(tickerObject,Frequency):
    cashFlowData = tickerObject.cash_flow(frequency=Frequency)
    return cashFlowData


def getFreeCashFlow(cashFlowData):
     freeCashFlow = cashFlowData['FreeCashFlow']
     freeCashFlow = freeCashFlow / 1e3
     return freeCashFlow

