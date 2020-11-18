# This is the income statement tab on the financials page in yahoo finance

def get_income_statement(ticker_object, frequency):
    income_statements = ticker_object.income_statement(frequency)

    return income_statements


def get_net_income(income_statement_data):
    net_income = income_statement_data['NetIncome']

    if net_income is not None:
        net_income = net_income / 1e3
        return net_income
    else:
        print("There is no net income for", net_income)


# Basic EPS no need for this. YET
def get_earnings_per_share(income_statement_data):
    basic_eps = income_statement_data["BasicEPS"]

    if basic_eps is not None:
        return basic_eps
    else:
        print("There is no basic EPS for", basic_eps)
