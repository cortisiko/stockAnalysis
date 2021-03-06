"""

I need some try except conditions

"""

def get_company_profile(ticker_object):
    try:
        company_profile = ticker_object.summary_profile
        return company_profile
    except Exception as e:
        print(e)


def get_company_sector(ticker_object, ticker_symbol):
    company_profile_object = get_company_profile(ticker_object)
    company_sector = company_profile_object[ticker_symbol]['sector']

    return company_sector


def get_company_summary_details(ticker_object, ticker_symbol):
    company_profile_object = get_company_profile(ticker_object)
    summary_details = company_profile_object[ticker_symbol]['longBusinessSummary']

    return summary_details
