error_message = "Company Does not have debt"


# This is the balance sheet tab on the financials page in yahoo finance
def get_balance_sheet_data(ticker_symbol,frequency):
    balanceSheetData = ticker_symbol.balance_sheet(frequency=frequency)

    return balanceSheetData


def getLongTermDebt(long_term_debt_data):
    try:
        long_term_debt = long_term_debt_data['LongTermDebt']
        long_term_debt = long_term_debt / 1e3

        return long_term_debt
    except KeyError:
        print (error_message)

def getCashAndExpenses(balance_sheet_data):
    cash_and_cash_equivalents = balance_sheet_data['CashAndCashEquivalents'].iloc[-1] ## getting the data for the most recent year
    cash_and_cash_equivalents = cash_and_cash_equivalents / 1e3

    return cash_and_cash_equivalents
