# stockAnalysis
The stock analysis app was written in python using the yahooquery package to fetch stock data. The data is then displayed on the frontend using tkinter. 
The goal of this application is to perform ratio analysis as well as give a visual representation (in the form of bar charts) of [line items](https://pakaccountants.com/what-is-line-item/#:~:text=In%20financial%20statement%20line%20items,next%20line%20or%20different%20line.) on the financial statements.


### This application is not a recommendation or endorsement of any particular investment or investment strategy. 

DEMO
---------------
When a user enters a stock symbol, multiple [finanical ratios](https://www.investopedia.com/financial-ratios-4689817) 
appear: 
![StockAnalysisHomePage](http://g.recordit.co/Ms9TtEM4I9.gif)


The data plotted into the bar graphs comes from: 

* Free Cash Flow (From the Cash Flow statement)

* Long Term Debt (From the Balance sheet)

* Net income     (From the Income statement)

* There's a bar graph for a company's Total Revenue. 


There is a trend graph comparing the different between Cash from operations and earnings. Basically performing [cash based earnings quality analysis](https://www.investopedia.com/terms/q/qualityofearnings.asp) of a stock    

On each graph, you can choose either a quarterly or yearly view.
![Charts](http://g.recordit.co/eu6GjJB1yV.gif)




To run:

* [Install pipenv](https://pypi.org/project/pipenv/)

* use `pipenv sync` or `pipenv sync --dev` to install the packages in the pipfile.

* Finally, run the code via terminal: `python userInterface.py` 

__In the off chance that tkinter isn’t install:__ `sudo apt-get install python3-tk`
