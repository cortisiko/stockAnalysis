import app.financials.companyprofile as company_profile


class TestCompanyProfile:

    def test_company_profile_data_returned(self,ticker_object):
        company_profile_data = company_profile.get_company_profile(ticker_object)
        assert company_profile_data is not None, "Nothing is returned for the company profile data"

    def test_get_company_sector(self, ticker_object):
        conpany_profile = company_profile.get_company_profile(ticker_object)
        conpany_sector = conpany_profile['BA']
        assert "sector" in conpany_sector, "'Sector' is missing from the company profile data object"

    def test_company_details(self,ticker_object):
        conpany_profile = company_profile.get_company_profile(ticker_object)
        company_details = conpany_profile['BA']
        assert "sector" in company_details, "'longBusinessSummary' is missing from the company profile data object"
