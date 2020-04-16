import ticker as Ticker
import cashFlowSheet as cashFlowPage
from helpers import getDate as date
import  balanceSheet as bs
import incomeStatementSheet as incomeStatement
import statistics as statsPage
import summary as summaryPage



Frequency = 'q'
tickerSymbol = 'GIS'

getTickerObject = Ticker.getTicker(tickerSymbol)
getCashFlowDataFrame = cashFlowPage.getCashFlowData(getTickerObject,Frequency)
freeCashFlow = cashFlowPage.getFreeCashFlow(getCashFlowDataFrame)

getDateInFrame = date.getDates(getCashFlowDataFrame)

getstats = statsPage.getStatistics(getTickerObject)
getDERatio = statsPage.getDebtToEquity(getTickerObject,tickerSymbol)
getROE = statsPage.getReturnOnEquity(getTickerObject,tickerSymbol)
getProfitMargin = statsPage.getProfitMargins(getTickerObject,tickerSymbol)


#### Calculating the PE ratio
eps = summaryPage.getEarningsPerShare(getTickerObject,tickerSymbol)
currentStockPrice = statsPage.getCurrentStockPrice(getTickerObject,tickerSymbol)
peRatio = summaryPage.getPERatio(eps,currentStockPrice)
#print(getCashFlowDataFrame)
#print(getDateInFrame)

print("This is the earnings per share is:",eps)
print("This is the PE ratio",peRatio)



