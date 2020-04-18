import matplotlib.pyplot as plt
import matplotlib
from pandas.plotting import register_matplotlib_converters

fig, ax = plt.subplots()

def plotGraph(dateRange,data,tickerSymbol,graphTitle):
    yLabelText = graphTitle + "in $"
    graphTitle = tickerSymbol +" "+graphTitle
    ax.set_title(graphTitle)
    ax.set_xlabel('Years')
    ax.set_ylabel(yLabelText)

    register_matplotlib_converters()
   # plt.bar(dateRange, data)
    plt.plot(dateRange, data, '-o', color='orange')
    ax.get_yaxis().set_major_formatter(matplotlib.ticker.FuncFormatter(lambda x, p: format(int(x), ',')))
    fig.tight_layout()
    plt.show()

