def getCompanyProfile(tickerObject):
    companyProfile = tickerObject.summary_profile
    return companyProfile

def get_company_sector(tickerObject,stockTicker):
    companyProfileObject = getCompanyProfile(tickerObject)
    companySector = companyProfileObject[stockTicker]['sector']

    return companySector

def getCompanySummaryDetails(tickerObject,stockTicker):
    companyProfileObject = getCompanyProfile(tickerObject)
    summaryDetails = companyProfileObject[stockTicker]['longBusinessSummary']

    return summaryDetails

