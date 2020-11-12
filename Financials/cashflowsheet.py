# This is the cashflow tab on the financials page in yahoo finance

def get_cash_flow_data(ticker_object, frequency):
    cash_flow_data = ticker_object.cash_flow(frequency=frequency)
    return cash_flow_data


def get_free_cash_flow(cash_flow_data):
    free_cash_flow = cash_flow_data['FreeCashFlow']
    free_cash_flow = free_cash_flow / 1e3

    return free_cash_flow


def get_operating_cash_flow(cash_flow_data):
    operating_cash_flow = cash_flow_data['OperatingCashFlow']
    operating_cash_flow = operating_cash_flow / 1e3

    return operating_cash_flow


def get_most_recent_cash_flow_total(cash_flow_data, position):
    most_recent_cash_flow = cash_flow_data['FreeCashFlow'].iloc[position]  ## takes the most recent cashflow
    most_recent_cash_flow = most_recent_cash_flow / 1e3

    return most_recent_cash_flow


def calculate_cash_burn(cash_and_cash_equivalents, free_cash_flow):
    cash_burn = cash_and_cash_equivalents / free_cash_flow
    cash_burn = cash_burn * 12

    return cash_burn
