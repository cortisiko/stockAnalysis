## This is the income statement tab on the financials page in yahoo finance

def getIncomeStatements(tickerObject,Frequency):
    incomeStatements = tickerObject.income_statement(frequency=Frequency)

    return incomeStatements


def getNetIncome(incomeStatementData):
    netIncome = incomeStatementData['NetIncome']

    if netIncome is not None:
         netIncome = netIncome / 1e3
         return netIncome
    else:
        return print("There is no net income for", netIncome)

    return netIncome

## Basic EPS no need for this. YET
def getEarningsPerShare(incomeStatements):
    basicEPS = incomeStatements["BasicEPS"]

    if basicEPS is not None:
        return basicEPS
    else:
        return print("There is no basic EPS for", basicEPS)

    return basicEPS

