def getCompanyProfile(tickerObject):
    companyProfile = tickerObject.summary_profile
    return companyProfile

def getCompanySector(tickerObject,stockTicker):
    companyProfileObject = getCompanyProfile(tickerObject)
    companySector = companyProfileObject[stockTicker]['sector']

    return companySector


