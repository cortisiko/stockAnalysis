

def getSummaryData(tickerObject):
    summaryData = tickerObject.key_stats
    return summaryData

def getEarningsPerShare(tickerObject,tickerSymbol):
    summaryData = getSummaryData(tickerObject)
    trailingEarningPerShare = summaryData[tickerSymbol]['trailingEps']
    trailingEarningPerShare = float(round(trailingEarningPerShare, 2))
    return trailingEarningPerShare


def getPERatio(eps,currentStockPrice):
    peRatio = currentStockPrice / eps
    peRatio = float(round(peRatio, 2))

    return peRatio