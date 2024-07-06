"""
Cash Flow page
"""

from app.charts import plot_cash_flow
from app.helpers import message_box
from app.pages.base_page import BasePage


class CashFlow(BasePage): # pylint: disable=too-many-ancestors
    """
    Cash Flow class represents the page for displaying cash to earnings charts.
    """

    def __init__(self, parent, controller):
        """
            Initializes the Cash Flow page with specific configurations.

            Args:
                parent (tk.Frame): The parent frame or window.
                controller (tk.Tk): The main controller handling the different frames.
            """
        super().__init__(parent, controller, "Cash Flow Charts", 'q', 'a')

    def selected_radio_button_option(self):
        """
        Handles the selection of the radio button option and updates the chart accordingly.
        """
        user_input = self.get_text_input()
        radio_button_frequency_option = self.radio_text.get()
        if not cash_flow.canvas:
            cash_flow.plot_cash_graph(self, user_input, radio_button_frequency_option)
        else:
            cash_flow.clear_plot()
            cash_flow.plot_cash_graph(self, user_input, radio_button_frequency_option)

    def show_error_message(self):
        """
        Displays an error message using the message box helper.
        """
        message_box.show_error_message()

    def clear(self):
        """
            Clears the input and the chart plot.
            """
        super().clear()
        cash_flow.clear_plot()
        self.text_input_box.focus()


cash_flow = plot_cash_flow.CashFlowGraph()
