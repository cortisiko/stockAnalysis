import app.financials.statistics as stats


class TestStockStats:
    def test_statistical_data_returned(self, ticker_object):
        stat_data = stats.get_stock_statistics(ticker_object)
        assert stat_data is not None, "There was no statistics returned"
