import ticker as Ticker
import cashFlowSheet as cashFlowPage
from helpers import getDate as date
import  balanceSheet as balanceSheetPage
import incomeStatementSheet as incomeStatementPage
import statistics as statsPage
import summary as summaryPage



Frequency = 'q'
tickerSymbol = 'JPM'

getTickerObject = Ticker.getTicker(tickerSymbol) ## Gets the ticker object so you can access the various objects
getCashFlowDataFrame = cashFlowPage.getCashFlowData(getTickerObject,Frequency)

## Need these two to plot the cash flow chart
freeCashFlow = cashFlowPage.getFreeCashFlow(getCashFlowDataFrame)
getDateInFrame = date.getDates(getCashFlowDataFrame)


#### Fundamentals ###
debtToEquityRatio = statsPage.getDebtToEquity(getTickerObject,tickerSymbol)
returnOnEquity = statsPage.getReturnOnEquity(getTickerObject,tickerSymbol)
profitMargin = statsPage.getProfitMargins(getTickerObject,tickerSymbol)

eps = summaryPage.getEarningsPerShare(getTickerObject,tickerSymbol)
currentStockPrice = statsPage.getCurrentStockPrice(getTickerObject,tickerSymbol)
peRatio = summaryPage.getPERatio(eps,currentStockPrice)


print("The earnings per share is:",eps)
print("The PE ratio is:",peRatio)
print("The MRQ debt to equity ratio is:",debtToEquityRatio)## MRQ (most recent quarter)
print("The return on equity ratio is:",returnOnEquity)
print("The net profit margin is:",profitMargin)


