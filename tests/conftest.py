import pytest
from app.helpers import tickers as ticker

"""
learn this tutorial on python pytests. being productive 
https://www.youtube.com/watch?v=ixqeebhUa-w

and taking args:
https://stackoverflow.com/questions/44441929/how-to-share-global-variables-between-tests
"""


"""
notes:
to profile which tests run the slowest use the --durations=3 flag
 
"""
global ticker_symbol


def pytest_addoption(parser):
    parser.addoption("--ticker", action="store", default="BA", help="By default: BA")


@pytest.fixture
def ticker_object(pytestconfig):
    global ticker_symbol

    ticker_symbol = pytestconfig.getoption("--ticker").upper()
    ticker_symbol_object = ticker.get_ticker(
        ticker_symbol)
    assert ticker_symbol_object is not None
    return ticker_symbol_object

@pytest.fixture
def user_ticker():
    return ticker_symbol
