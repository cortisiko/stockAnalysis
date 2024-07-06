"""
Net income page
"""
from app.charts import plot_net_income
from app.helpers import message_box
from app.pages.base_page import BasePage


class NetIncome(BasePage): # pylint: disable=too-many-ancestors
    """
         Revenue class represents the page for displaying a company's  net income.

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
        super().__init__(parent, controller, "Net Income Charts", 'q', 'a', bg_color='#1B6666')
        self.text_input_box.config(width=6)

    def selected_radio_button_option(self):
        """
        Handles the selection of the radio button option and updates the chart accordingly.
        """
        user_input = self.get_text_input()
        radio_button_frequency_option = self.radio_text.get()
        if not income.canvas:
            income.plot_net_income(self, user_input, radio_button_frequency_option)
        else:
            income.clear_plot()
            income.plot_net_income(self, user_input, radio_button_frequency_option)

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
        income.clear_plot()


income = plot_net_income.NetIncomeGraph()
