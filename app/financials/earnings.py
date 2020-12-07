def get_earnings_data(ticker_symbol):
    try:
        earnings = ticker_symbol.earnings
        return earnings

    except Exception as e:
        print(e)
