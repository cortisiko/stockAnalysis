import pandas as pd


def getIncomeStatements(ticker):
    incomeStatements = ticker.income_statement(frequency='q')
    incomeStatements = pd.DataFrame(incomeStatements)
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', -1)

    return incomeStatements

def getEarningsPerShare(incomeStatements):
    asOfDate = incomeStatements['asOfDate'].astype(str)
    BasicEPS = incomeStatements["BasicEPS"]

    return

