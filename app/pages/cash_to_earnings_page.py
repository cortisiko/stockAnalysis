"""
Cash to earnings page
"""
from app.helpers import message_box
from app.charts import plot_cash_based_earnings
from app.pages.base_page import BasePage


class CashToEarnings(BasePage): # pylint: disable=too-many-ancestors
    """
    CashToEarnings class represents the page for displaying cash to earnings charts.

    Inherits from:
        BasePage: A base page class that handles common functionalities for all pages.

    Methods:
        __init__(parent, controller):
            Initializes the CashToEarnings page with specific configurations.

        selected_radio_button_option():
            Handles the selection of the radio button option and updates the chart accordingly.

        show_error_message():
            Displays an error message using the message box helper.

        clear():
            Clears the input and the chart plot.
    """

    def __init__(self, parent, controller):
        """
        Initializes the CashToEarnings page with specific configurations.

        Args:
            parent (tk.Frame): The parent frame or window.
            controller (tk.Tk): The main controller handling the different frames.
        """
        # pylint: disable=line-too-long
        super().__init__(parent, controller, "Cash to Earnings Charts", 'q', 'a')
        self.text_input_box.config(width=8)
        self.text_input_box.focus()

    def selected_radio_button_option(self):
        """
        Handles the selection of the radio button option and updates the chart accordingly.
        """
        user_input = self.get_text_input()
        radio_button_frequency_option = self.radio_text.get()
        if not cash_to_earnings.canvas:
            cash_to_earnings.plot_cash_to_earnings(self, user_input, radio_button_frequency_option)
        else:
            cash_to_earnings.clear_plot()
            cash_to_earnings.plot_cash_to_earnings(self, user_input, radio_button_frequency_option)

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
        cash_to_earnings.clear_plot()


cash_to_earnings = plot_cash_based_earnings.CashBasedEarningGraph()
