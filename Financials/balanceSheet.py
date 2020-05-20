## This is the balance sheet tab on the financials page in yahoo finance
def getBalanceSheetData(tickerSymbol,Frequency):
    balanceSheetData = tickerSymbol.balance_sheet(frequency=Frequency)

    return balanceSheetData


def getLongTermDebt(longTermDebtData):
    longTermDebt = longTermDebtData['LongTermDebt']
    longTermDebt = longTermDebt / 1e3

    return longTermDebt