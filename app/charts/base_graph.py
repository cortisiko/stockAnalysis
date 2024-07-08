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
        self.fig.patch.set_facecolor('#2C3E50')  # Set background color of the figure
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
        ax.set_title(title, color='white')
        ax.set_xlabel(xlabel, color='white')
        ax.set_ylabel(ylabel, color='white')
        ax.get_yaxis().set_major_formatter(
            matplotlib.ticker.FuncFormatter(lambda x, p: format(int(x), ",")))
        ax.set_facecolor('#2C3E50')  # Set background color of the axes
        ax.tick_params(axis='x', colors='white')
        ax.tick_params(axis='y', colors='white')

    def add_legend(self, ax, positive_label="positive cash flow", negative_label="negative cash flow"):
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
            for color in ["green", "red"]
        ]
        ax.legend(legend_handles, [positive_label, negative_label], facecolor='#2C3E50', framealpha=1,
                  edgecolor='white', fontsize=10, labelcolor='white')

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
