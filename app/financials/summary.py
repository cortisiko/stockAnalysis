# This is the summary tab


def key_stats_data(ticker_object):
    key_stats = ticker_object.key_stats
    return key_stats


def summary_details_data(ticker_object):
    summary_data = ticker_object.summary_detail
    return summary_data


def earnings_per_share(ticker_object, ticker_symbol):
    key_stats = key_stats_data(ticker_object)

    trailing_earning_per_share = key_stats[ticker_symbol].get("trailingEps", None)

    if trailing_earning_per_share is not None:
        trailing_earning_per_share = float(round(trailing_earning_per_share, 2))
        return trailing_earning_per_share
    else:
        return print("There is no EPS Ratio for", ticker_symbol)


def get_pe_ratio(ticker_object, ticker_symbol):
    summary_data = summary_details_data(ticker_object)

    pe_ratio = summary_data[ticker_symbol].get("trailingPE", None)

    if pe_ratio is not None:
        pe_ratio = float(round(pe_ratio, 2))
        return pe_ratio
    else:
        return print("There is no PE Ratio for", ticker_symbol)
