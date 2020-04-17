## This is the income statement tab on the financials page in yahoo finance

import pandas as pd


def getIncomeStatements(ticker):
    incomeStatements = ticker.income_statement(frequency='q')
    incomeStatements = pd.DataFrame(incomeStatements)
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', -1)

    return incomeStatements

## Basic EPS no need for this. YET
def getEarningsPerShare(incomeStatements):
    basicEPS = incomeStatements["BasicEPS"]

    return basicEPS

