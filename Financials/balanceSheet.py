## This is the balance sheet tab on the financials page in yahoo finance
def getBalanceSheetData(tickerSymbol,Frequency):
    balanceSheetData = tickerSymbol.balance_sheet(frequency=Frequency)

    return balanceSheetData

errorMessage = "Company Does not have debt"

def getLongTermDebt(longTermDebtData):
    try:
        longTermDebt = longTermDebtData['LongTermDebt']
        longTermDebt = longTermDebt / 1e3

        return longTermDebt
    except KeyError:
        print (errorMessage)

def getCashAndExpenses(balanceSheetData):
    CashAndCashEquivalents = balanceSheetData['CashAndCashEquivalents'].iloc[-1] ## getting the data for the most recent year
    CashAndCashEquivalents = CashAndCashEquivalents / 1e3

    return CashAndCashEquivalents
