import pytest
from app.helpers import tickers
from app.financials import cashflowsheet

import logging

"""
https://stackoverflow.com/questions/34466027/in-pytest-what-is-the-use-of-conftest-py-files
"""


def test_cash_flow_data_frame(ticker_object):
    cash_flow_data = cashflowsheet.get_cash_flow_data(ticker_object, "a")
    assert len(cash_flow_data) > 0, "there is not cash flow data"


def test_free_cash_flow(ticker_object):
    yearly_free_cash_flow = cashflowsheet.get_cash_flow_data(ticker_object, "a")

    assert 'FreeCashFlow' in yearly_free_cash_flow, "I do not see the free cash flow column"
