""""
 Testing whether the correct data is returned in the income statement object
 """
import app.financials.incomestatementsheet as income_statement


class TestIncomeStatement:
    """"
     Validating the income statement data used within the app is returned correctly
     """
    def test_income_statement_data_returned(self,  ticker_object):
        """
        Test that the income statement data is returned and is not None.
        """
        income_data = income_statement.get_income_statement(ticker_object, "a")

        assert income_data is not None, "income data has nothing returned"

    def test_net_income_data_returned(self,  ticker_object):
        """
        Test that the 'NetIncome' field is present in the income statement data.
        """
        income_data = income_statement.get_income_statement(ticker_object, "a")

        assert (
            "NetIncome" in income_data
        ), "'NetIncome' is not in the incomesheet dataframe"
