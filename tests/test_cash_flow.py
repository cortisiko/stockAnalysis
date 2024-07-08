"""
https://stackoverflow.com/questions/34466027/in-pytest-what-is-the-use-of-conftest-py-files
"""
from app.financials import cash_flow


class TestCashFlow:
    """
    Unit tests for validating the cash flow data used within the app.
    """

    def test_cash_flow_data_returned(self, ticker_object):
        """
        Test that the cash flow data is returned and contains data.

        Args:
            ticker_object: The object containing the ticker information.
        """
        cash_flow_data = cash_flow.get_cash_flow_data(ticker_object, "a")
        assert len(cash_flow_data) > 0, "There is no cash flow data returned"

    def test_free_cash_flow(self, ticker_object):
        """
        Test that the 'FreeCashFlow' field is present in the yearly cash flow data.

        Args:
            ticker_object: The object containing the ticker information.
        """
        yearly_free_cash_flow = cash_flow.get_cash_flow_data(ticker_object, "a")
        assert "FreeCashFlow" in yearly_free_cash_flow, "Free cash flow data is missing"

    def test_operating_cash_flow(self, ticker_object):
        """
        Test that the 'OperatingCashFlow' field is present in the quarterly cash flow data.

        Args:
            ticker_object: The object containing the ticker information.
        """
        quarterly_operating_cash_flow_data = cash_flow.get_cash_flow_data(ticker_object, "a")
        assert "OperatingCashFlow" in quarterly_operating_cash_flow_data, "No Operating cash flow"
