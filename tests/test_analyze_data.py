
from app.financials.analyze import get_company_sector, get_current_stock_price


def test_get_company_sector():
    conpany_sector = get_company_sector("C")
    assert conpany_sector is not None


def test_current_stock_price():
    conpany_price = get_current_stock_price("C")
    assert conpany_price > 0
