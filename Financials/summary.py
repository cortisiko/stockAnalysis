## This is the summary tab

def getKeyStatsData(ticker_object):
    keyStats = ticker_object.key_stats
    return keyStats

def summary_details_data(ticker_object):
    summaryData = ticker_object.summary_detail
    return summaryData

def getEarningsPerShare (ticker_object, ticker_symbol):
    keyStats = getKeyStatsData(ticker_object)

    trailingEarningPerShare = keyStats[ticker_symbol].get('trailingEps', None)

    if trailingEarningPerShare is not None:
        trailingEarningPerShare = float(round(trailingEarningPerShare, 2))
        return trailingEarningPerShare
    else:
        return print("There is no EPS Ratio for", ticker_symbol)


def get_pe_ratio (ticker_object, ticker_symbol):
    summary_data = summary_details_data(ticker_object)

    pe_ratio = summary_data[ticker_symbol].get('trailingPE', None)

    if pe_ratio is not None:
        pe_ratio = float(round(pe_ratio, 2))
        return pe_ratio
    else:
        return print("There is no PE Ratio for", ticker_symbol)
