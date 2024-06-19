"""
This is the class that plots the graphs.
"""
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import matplotlib
from matplotlib.lines import Line2D

matplotlib.use("TkAgg")


class BaseGraph:
    """
    Base class for all financial graphs.
    """

    def __init__(self, ylabel_text):
        """
        Initializes the BaseGraph class.

        Parameters:
        ylabel_text (str): The label for the y-axis.
        """
        self.canvas = None
        self.fig = Figure(figsize=(12, 5), dpi=80)
        self.ylabel_text = ylabel_text

    def setup_ax(self, ax, title, xlabel, ylabel):
        """
        Sets up the axes for the graph.

        Parameters:
        ax (matplotlib.axes.Axes): The axes to set up.
        title (str): The title of the graph.
        xlabel (str): The label for the x-axis.
        ylabel (str): The label for the y-axis.
        """
        ax.set_title(title)
        ax.set_xlabel(xlabel)
        ax.set_ylabel(ylabel)
        ax.get_yaxis().set_major_formatter(
            matplotlib.ticker.FuncFormatter(lambda x, p: format(int(x), ","))
        )

    def add_legend(self, ax, positive_label="positive", negative_label="negative"):
        """
        Adds a legend to the graph.

        Parameters:
        ax (matplotlib.axes.Axes): The axes to add the legend to.
        positive_label (str): The label for positive values.
        negative_label (str): The label for negative values.
        """
        legend_handles = [
            Line2D(
                [0],
                [0],
                linewidth=0,
                marker="o",
                markerfacecolor=color,
                markersize=12,
                markeredgecolor="none",
            )
            for color in ["g", "r"]
        ]
        ax.legend(legend_handles, [positive_label, negative_label])

    def draw_canvas(self, container):
        """
        Draws the canvas in the given container.

        Parameters:
        container (tkinter.Frame): The container to draw the canvas in.
        """
        if not self.canvas:
            self.canvas = FigureCanvasTkAgg(self.fig, container)
            self.canvas.get_tk_widget().pack(side="top", fill="both", expand=True)
        self.canvas.draw_idle()

    def clear_plot(self):
        """
        Clears the plot.
        """
        self.fig.clear()
        if self.canvas:
            self.canvas.draw_idle()
