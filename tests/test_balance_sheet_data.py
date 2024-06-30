"""
   Unit tests for validating the balance sheet data used within the app.
   """
import app.financials.balance_sheet as _balance_sheet


class TestBalanceSheet:
    """
    Unit tests for validating the balance sheet data used within the app.
    """

    def test_balance_sheet_data_returned(self, ticker_object):
        """
        Test that the balance sheet data is returned and contains rows and columns.

        Args:
            ticker_object: The object containing the ticker information.
        """
        balance_sheet = _balance_sheet.get_balance_sheet_data(ticker_object, "a")
        assert len(balance_sheet) > 0, "The rows are missing in the balance sheet"
        assert len(balance_sheet.columns) > 0, "The balance sheet is not returning data"

    def test_long_term_debt(self, ticker_object):
        """
        Test that the 'LongTermDebt' field is present in the balance sheet data.

        Args:
        ticker_object: The object containing the ticker information.
        """
        balance_sheet = _balance_sheet.get_balance_sheet_data(ticker_object, "a")
        assert "LongTermDebt" in balance_sheet, "'LongTermDebt' is not in the balance sheet data"
