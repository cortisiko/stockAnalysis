import ticker as Ticker
import cashFlowSheet as cashFlow
import balanceSheet as bs
import incomeStatementSheet as incomeStatement

Frequency = 'q'
tickerSymbol = 'GIS'

getTicker = Ticker.getTicker(tickerSymbol)
getCashFlow = cashFlow.getCashFlowData(getTicker,Frequency)
freeCashFlow = cashFlow.getFreeCashFlow(getCashFlow)

print(getCashFlow)
#print(freeCashFlow)