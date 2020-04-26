import matplotlib.pyplot as plt
import matplotlib
matplotlib.use("TkAgg")
from matplotlib import pyplot as plt
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
# https://github.com/furas/python-examples/tree/master/tkinter/embed-matplotlib

fig, ax = plt.subplots()
def plotGraph(dateRange,data,companyName,graphTitle,root):
    yLabelText = graphTitle + "in $"
    graphTitle = companyName +" "+graphTitle
    ax.set_title(graphTitle)
    ax.set_xlabel('Years')
    ax.set_ylabel(yLabelText)


    # register_matplotlib_converters()
   # plt.bar(dateRange, data)
    plt.plot(dateRange, data, '-o', color='orange')
    ax.get_yaxis().set_major_formatter(matplotlib.ticker.FuncFormatter(lambda x, p: format(int(x), ',')))
    fig.tight_layout()


    plt.show()


def killGraph():
    plt.close('all')