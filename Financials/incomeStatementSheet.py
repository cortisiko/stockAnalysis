## This is the income statement tab on the financials page in yahoo finance

def getIncomeStatements(tickerObject,Frequency):
    incomeStatements = tickerObject.income_statement(frequency=Frequency)

    return incomeStatements


def getNetIncome(incomeStatementData):
    netIncome = incomeStatementData['NetIncome']
    netIncome = netIncome / 1e3
    return netIncome

## Basic EPS no need for this. YET
def getEarningsPerShare(incomeStatements):
    basicEPS = incomeStatements["BasicEPS"]

    return basicEPS

