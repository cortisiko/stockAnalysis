## This is the cashflow tab on the financials page in yahoo finance

def getCashFlowData(tickerObject,Frequency):
    cashFlowData = tickerObject.cash_flow(frequency=Frequency)
    return cashFlowData


def getFreeCashFlow(cashFlowData):
     freeCashFlow = cashFlowData['FreeCashFlow']
     freeCashFlow = freeCashFlow / 1e3

     return freeCashFlow

def getOperatingCashFlow(cashFlowData):
        operatingCashFlow  = cashFlowData['OperatingCashFlow']
        operatingCashFlow = operatingCashFlow / 1e3

        return operatingCashFlow

def get_most_recent_cash_flow_total(cashFlowData,position):
    mostRecentCashFlow = cashFlowData['FreeCashFlow'].iloc[position] ## takes the most recent cashflow
    mostRecentCashFlow = mostRecentCashFlow / 1e3

    return mostRecentCashFlow


def calculate_cash_burn(CashAndCashEquivalents,freeCashFlow):
    cashBurn = CashAndCashEquivalents / freeCashFlow
    cashBurn = cashBurn * 12

    return cashBurn