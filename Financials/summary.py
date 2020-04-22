## This is the summary tab

def getKeyStatsData(tickerObject):
    keyStats = tickerObject.key_stats
    return keyStats

def getSummaryDetailsData(tickerObject):
    summaryData = tickerObject.summary_detail
    return summaryData

def getEarningsPerShare(tickerObject,tickerSymbol):
    keyStats = getKeyStatsData(tickerObject)
    trailingEarningPerShare = keyStats[tickerSymbol]['trailingEps']
    trailingEarningPerShare = float(round(trailingEarningPerShare, 2))
    return trailingEarningPerShare


def getPERatio(tickerObject,tickerSymbol):
    summaryData = getSummaryDetailsData(tickerObject)
    peRatio = summaryData[tickerSymbol]['trailingPE']
    peRatio = float(round(peRatio, 2))

    return peRatio