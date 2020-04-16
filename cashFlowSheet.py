## This is the cashflow tab on the financials page in yahoo finance

import matplotlib
from yahooquery import Ticker
import pandas as pd
import matplotlib.pyplot as plt
import ticker as tick

def getCashFlowData(ticks,Frequency):
    cashFlowData = ticks.cash_flow(frequency=Frequency)
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', -1)

    return cashFlowData


def getFreeCashFlow(cashFlowData):
     freeCashFlow = cashFlowData['FreeCashFlow'].astype(str)
     return freeCashFlow