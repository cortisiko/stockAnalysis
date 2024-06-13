"""
tests for validating the company profile data used within the app.


"""

import app.financials.companyprofile as company_profile


class TestCompanyProfile:
    """
     tests for validating the company profile data used within the app.
    """

    def test_company_profile_data_returned(self, ticker_object):
        """
        Test that the company profile data is returned and is not None.

        Args:
            ticker_object: The object containing the ticker information.
        """
        company_profile_data = company_profile.get_company_profile(ticker_object)
        assert company_profile_data is not None, "Nothing is returned for the company profile data"

    def test_get_company_sector(self, ticker_object, user_ticker):
        """
        Test that the 'sector' field is present in the company profile data for a given ticker.

        Args:
            ticker_object: The object containing the ticker information.
            user_ticker: The specific ticker for which to retrieve the sector information.
        """
        company_profile_ = company_profile.get_company_profile(ticker_object)
        company_sector = company_profile_[user_ticker]
        assert "sector" in company_sector, "'Sector' is missing from the company profile object"

    def test_company_details(self, ticker_object, user_ticker):
        """
        Test that the 'longBusinessSummary' field is present in the company profile data.
        param:
            :ticker_object: The object containing the ticker information.
            user_ticker: The specific ticker for which to retrieve the company details.
        """
        company_profile_ = company_profile.get_company_profile(ticker_object)
        company_details = company_profile_[user_ticker]
        assert "longBusinessSummary" in company_details, "'longBusinessSummary' is missing"
