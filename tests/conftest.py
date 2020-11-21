import pytest
from app.helpers import tickers as ticker

"""
learn this tutorial on python pytests. being productive 
https://www.youtube.com/watch?v=ixqeebhUa-w
"""


@pytest.fixture
def ticker_symbol():
    ticker_symbol = "C"
    ticker_symbol_object = ticker.get_ticker(
        ticker_symbol)
    assert ticker_symbol_object is not None

    return ticker_symbol_object
