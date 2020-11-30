import app.financials.statistics as stats


class TestStatisticsData:

    def test_stock_statistical_data_returned(self, ticker_object):
        statistics_data = stats.get_stock_statistics(ticker_object)
        assert statistics_data is not None, "Stocks statistical data did not return anything"

    def test_current_stock_price(self, ticker_object, user_ticker):
        statistics_data = stats.get_stock_statistics(ticker_object)
        assert 'currentPrice' in statistics_data[
            user_ticker], "I do not see 'currentPrice' in the statiscial data frame"

    def test_debt_to_equity(self, ticker_object, user_ticker):
        statistics_data = stats.get_stock_statistics(ticker_object)
        assert 'debtToEquity' in statistics_data[
            user_ticker], "I do not see 'debtToEquity' in the statiscial data frame"

    def test_return_on_equity(self, ticker_object, user_ticker):
        statistics_data = stats.get_stock_statistics(ticker_object)
        assert 'returnOnEquity' in statistics_data[
            user_ticker], "I do not see 'returnOnEquity' in the statiscial data frame"

    def test_profit_margins(self, ticker_object, user_ticker):
        statistics_data = stats.get_stock_statistics(ticker_object)
        assert 'profitMargins' in statistics_data[
            user_ticker], "I do not see 'profitMargins' in the statiscial data frame"
