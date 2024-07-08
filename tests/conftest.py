"""
Learn this tutorial on Python Pytest: being productive
https://www.youtube.com/watch?v=ixqeebhUa-w

You are up to 'post-process test reports/failures:
https://docs.pytest.org/en/6.0.1/example/simple.html
'

Notes:
To profile which tests run the slowest, use the --durations=3 flag.
"""

import pytest
from app.helpers import tickers as ticker


def pytest_addoption(parser):
    """
    Add a custom command-line option to pytest.

    Args:
        parser: The pytest parser object used to add custom command-line options.
    """
    parser.addoption("--ticker", action="store", default="V", help="Ticker symbol, default: V")


@pytest.fixture(scope="session")
def get_ticker_symbol(pytestconfig):
    """
    A pytest fixture that retrieves the ticker symbol from the command-line options.

    Args:
        pytestconfig: The pytest configuration object used to access command-line options.

    Returns:
        str: The ticker symbol in uppercase.
    """
    return pytestconfig.getoption("--ticker").upper()


@pytest.fixture(scope="session")
def ticker_object(get_ticker_symbol):
    """
    A pytest fixture that creates and returns a ticker object based on the provided ticker symbol.

    Args:
        get_ticker_symbol: The ticker symbol for which to retrieve the ticker object.

    Returns:
        object: The ticker object.

    Raises:
        AssertionError: If the ticker object is None.
    """
    ticker_symbol_obj = ticker.get_ticker(get_ticker_symbol)
    assert ticker_symbol_obj is not None, "Ticker object should not be None"
    return ticker_symbol_obj


@pytest.fixture
def user_ticker(get_ticker_symbol):
    """
    A pytest fixture that returns the ticker symbol.

    Args:
        get_ticker_symbol: The ticker symbol retrieved from the command-line options.

    Returns:
        str: The ticker symbol in uppercase.
    """
    return get_ticker_symbol
