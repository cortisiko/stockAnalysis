import pytest

from app.Financials.analyze import get_company_sector, get_current_stock_price


def test_get_company_sector():
    conpany_sector = get_company_sector("C")
    print("HOOOOO", conpany_sector)
    assert get_company_sector("C") is not None


def test_current_stock_price():
    conpany_price = get_current_stock_price("C")
    print("Price", conpany_price)
    assert get_company_sector("C") is not None
