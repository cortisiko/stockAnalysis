# stockAnalysis
This app was done in python using the yahooquery package to fetch stock data. The data is displayed on the frontend using tkinter. 

### This content is not a recommendation or endorsement of any particular investment or investment strategy. 

DEMO
---------------
When you search a stock symbol a few [finanical ratios](https://www.investopedia.com/financial-ratios-4689817) 
about the stock is displayed: 
![StockAnalysisHomePage](http://g.recordit.co/Ms9TtEM4I9.gif)


Furthermore, the data from a couple line items on the [finanical statements](https://www.investopedia.com/terms/f/financial-statements.asp) were turned into charts so one can visually see the changes over time. The line items in particular are: 

* Free Cash Flow (From the Cash Flow statement)

* Long Term Debt (From the Balance sheet)

* Net income     (From the Income statement)

A chart was also made for a company's Total Revenue. 

On each one of the charts, you can choose either a quarterly or yearly view.
![Charts](http://g.recordit.co/eu6GjJB1yV.gif)




To install:

* [download python3 or later](https://www.python.org/downloads/)

* install these packages: [requests](https://pypi.org/project/requests/), [yahooquery](https://pypi.org/project/yahooquery/),
[mathplotlib](https://pypi.org/project/matplotlib/)

* Run the code via terminal: python userInterface.py 
