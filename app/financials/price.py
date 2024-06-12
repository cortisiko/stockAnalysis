def get_price_data_object(ticker_object):

    if ticker_object is not None:
        price_object = ticker_object.price
        return price_object
    else:
        print("User did not enter a valid ticker")


def get_current_stock_price(ticker_object, ticker_symbol):
    price_object = get_price_data_object(ticker_object)
    current_stock_price = price_object[ticker_symbol]["regularMarketPrice"]
    current_stock_price = float(round(current_stock_price, 2))

    return current_stock_price


def get_company_name(ticker_object, ticker_symbol):
    price_object = get_price_data_object(ticker_object)
    company_name = price_object[ticker_symbol]["shortName"]

    return company_name
