
def getPriceDataObject(tickerObject):
    priceObject = tickerObject.price
    return priceObject


def getCurrentStockPrice(tickerObject,tickerSymbol):
    priceObject = getPriceDataObject(tickerObject)
    currentStockPrice = priceObject[tickerSymbol]['regularMarketPrice']
    currentStockPrice = float(round(currentStockPrice, 2))

    return currentStockPrice

def getCompanyName(tickerObject,tickerSymbol):
    priceObject = getPriceDataObject(tickerObject)
    companyName = priceObject[tickerSymbol]['shortName']

    return companyName