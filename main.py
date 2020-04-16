import ticker as Ticker
import cashFlowSheet as cashFlow
from helpers import getDate as date
import  balanceSheet as bs
import incomeStatementSheet as incomeStatement
import statistics as stat
Frequency = 'q'
tickerSymbol = 'C'

getTicker = Ticker.getTicker(tickerSymbol)
getCashFlowDataFrame = cashFlow.getCashFlowData(getTicker,Frequency)
freeCashFlow = cashFlow.getFreeCashFlow(getCashFlowDataFrame)

#getDateInFrame = date.getDates(getCashFlow)

getstats = stat.getStatistics(getTicker)
getDERatio = stat.getDebtToEquity(getstats,tickerSymbol)
getROE = stat.getReturnOnEquity(getstats,tickerSymbol)
getProfitMargin = stat.getProfitMargins(getstats,tickerSymbol)


#print(getCashFlowDataFrame)
#print(getDateInFrame)
print(getstats)


