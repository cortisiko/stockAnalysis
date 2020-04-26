## This is the summary tab

def getKeyStatsData(tickerObject):
    keyStats = tickerObject.key_stats
    return keyStats

def getSummaryDetailsData(tickerObject):
    summaryData = tickerObject.summary_detail
    return summaryData

def getEarningsPerShare(tickerObject,tickerSymbol):
    keyStats = getKeyStatsData(tickerObject)

    trailingEarningPerShare = keyStats[tickerSymbol].get('trailingEps', None)

    if trailingEarningPerShare is not None:
        trailingEarningPerShare = float(round(trailingEarningPerShare, 2))
        return trailingEarningPerShare
    else:
        return print("There is no EPS Ratio for", tickerSymbol)


def getPERatio(tickerObject,tickerSymbol):
    summaryData = getSummaryDetailsData(tickerObject)

    peRatio = summaryData[tickerSymbol].get('trailingPE', None)

    if peRatio is not None:
        peRatio = float(round(peRatio, 2))
        return peRatio
    else:
        return print("There is no PE Ratio for", tickerSymbol)
