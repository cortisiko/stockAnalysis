"""
earnings page
"""

from base_page import BasePage

from app.charts import plot_earnings as plt_earnings
from app.helpers import message_box as messagebox


class Earnings(BasePage):
    """
      CEarnings class represents the page for displaying a company earnings.

      """
    def __init__(self, parent, controller):
        super().__init__(parent, controller, "Earnings Charts", 'quarterly', 'yearly')

    def selected_radio_button_option(self):
        user_input = self.get_text_input()
        radio_button_frequency_option = self.radio_text.get()
        if not earnings.canvas:
            earnings.plot_earnings(self, user_input, radio_button_frequency_option)
        else:
            earnings.clear_plot()
            earnings.plot_earnings(self, user_input, radio_button_frequency_option)

    def show_error_message(self):
        messagebox.show_error_message()

    def clear(self):
        super().clear()
        earnings.clear_plot()


earnings = plt_earnings.EarningsGraph()
