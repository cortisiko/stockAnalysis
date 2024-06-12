from app.financials import cash_flow_sheet

"""
https://stackoverflow.com/questions/34466027/in-pytest-what-is-the-use-of-conftest-py-files
"""


class TestCashFlow:

    def test_cash_flow_data_returned(self, ticker_object):
        cash_flow_data = cash_flow_sheet.get_cash_flow_data(ticker_object, "a")
        assert len(cash_flow_data) > 0, "there is not cash flow data"

    def test_free_cash_flow(self, ticker_object):
        yearly_free_cash_flow = cash_flow_sheet.get_cash_flow_data(ticker_object, "a")

        assert 'FreeCashFlow' in yearly_free_cash_flow, "I do not see the free cash flow data"

    def test_operating_cash_flow(self, ticker_object):
        quarterly_operating_cash_flow_data = cash_flow_sheet.get_cash_flow_data(ticker_object,"a")

        assert 'OperatingCashFlow' in quarterly_operating_cash_flow_data, "I do not see the operating cash flow data"
