error_message = "Company Does not have debt"


# This is the balance sheet tab on the financials page in yahoo finance
def get_balance_sheet_data(ticker_symbol, frequency):
    try:
        balanceSheetData = ticker_symbol.balance_sheet(frequency)
        return balanceSheetData
    except Exception as e:
        print(e)


def get_long_term_debt(long_term_debt_data):
    try:
        long_term_debt = long_term_debt_data['LongTermDebt']
        long_term_debt = long_term_debt / 1e3

        return long_term_debt
    except KeyError:
        print(error_message)


def get_cash_and_expenses(balance_sheet_data,ticker_symbol):
    try:
        cash_and_cash_equivalents = balance_sheet_data['CashAndCashEquivalents'].iloc[
        -1]  ## getting the data for the most recent year
        cash_and_cash_equivalents = cash_and_cash_equivalents / 1e3
        return cash_and_cash_equivalents
    except Exception as e:
        print(f'I do not see anything on the balance sheet for {ticker_symbol}')