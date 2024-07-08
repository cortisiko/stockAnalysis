"""
debt page
"""


from app.charts import plot_long_term_debt as plt_debt
from app.helpers import message_box as messagebox
from app.pages.base_page import BasePage


class Debt(BasePage): # pylint: disable=too-many-ancestors
    """
    Debt class represents the page for displaying a company's debt.

    """
    def __init__(self, parent, controller):
        super().__init__(parent, controller, "Long Term Debt Charts", 'q', 'a')
        self.text_input_box.config(width=6)

    def selected_radio_button_option(self):
        """
        Handles the selection of the radio button option and updates the chart accordingly.
        """
        user_input = self.get_text_input()
        radio_button_frequency_option = self.radio_text.get()
        if not long_term_debt.canvas:
            long_term_debt.plot_debt_graph(self, user_input, radio_button_frequency_option)
        else:
            long_term_debt.clear_plot()
            long_term_debt.plot_debt_graph(self, user_input, radio_button_frequency_option)

    def show_error_message(self):
        """
        Displays an error message using the message box helper.
        """
        messagebox.show_error_message()

    def clear(self):
        """
        Clears the input and the chart plot.
        """
        super().clear()
        long_term_debt.clear_plot()


long_term_debt = plt_debt.DebtGraph()
