import app.financials.companyprofile as company_profile


class TestCompanyProfile():

    def test_get_company_sector(self, ticker_object):
        conpany_profile = company_profile.get_company_profile(ticker_object)
        conpany_sector = conpany_profile["BA"]
        assert "sector" in conpany_sector
