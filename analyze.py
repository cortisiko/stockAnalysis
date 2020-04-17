from click._compat import raw_input

from Financials import cashFlowSheet as cashFlowPage
from Financials import statistics as statisticsTab
from Financials import summary as summaryPage

from helpers import Ticker as ticker
from helpers import plotChart as plot
from helpers import getDate as date


Frequency = 'a'
#tickerSymbol = 'gis'.upper()

tickerSymbol = raw_input("Enter Symbol: ")
tickerSymbol = tickerSymbol.upper()
tickerObject = ticker.getTicker(tickerSymbol) ## Gets the ticker object so you can access the various objects
getCashFlowDataFrame = cashFlowPage.getCashFlowData(tickerObject,Frequency)

## Need these two to plot the cash flow chart
freeCashFlow = cashFlowPage.getFreeCashFlow(getCashFlowDataFrame)
getdate = date.getDates(getCashFlowDataFrame)

#### Fundamentals ###
debtToEquityRatio = statisticsTab.getDebtToEquity(tickerObject,tickerSymbol)
returnOnEquity = statisticsTab.getReturnOnEquity(tickerObject,tickerSymbol)
profitMargin = statisticsTab.getProfitMargins(tickerObject,tickerSymbol)

eps = summaryPage.getEarningsPerShare(tickerObject,tickerSymbol)
currentStockPrice = statisticsTab.getCurrentStockPrice(tickerObject,tickerSymbol)
peRatio = summaryPage.getPERatio(eps,currentStockPrice)


print("The earnings per share is:",eps)
print("The PE ratio is:",peRatio)
print("The MRQ debt to equity ratio is:",debtToEquityRatio)## MRQ (most recent quarter)
print("The return on equity ratio is {:0.2f}%".format(returnOnEquity))
print("The net profit margin is {:0.2f}%\n".format(profitMargin))

plot.plotGraph(getdate,freeCashFlow) ## plotting free cash flow
