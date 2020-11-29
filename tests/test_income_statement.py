import app.financials.incomestatementsheet as income_statement


class TestIncomeStatement:

    def test_income_statement_data_returned(self, user_ticker, ticker_object):
        income_data = income_statement.get_income_statement(ticker_object, "a")

        assert income_data is not None,"income data has nothing returned"

    def test_net_income_data_returned(self, user_ticker, ticker_object):
        income_data = income_statement.get_income_statement(ticker_object, "a")

        assert 'NetIncome' in income_data,"'NetIncome' is not in the incomesheet dataframe"
