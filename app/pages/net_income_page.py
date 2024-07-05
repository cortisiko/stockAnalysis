try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

from app.charts import plot_net_income
from app.helpers import message_box
from app.pages.base_page import BasePage


class NetIncome(BasePage):
    def __init__(self, parent, controller):
        super().__init__(parent, controller, "Net Income Charts", 'q', 'a', bg_color='#1B6666')
        self.text_input_box.config(width=6)

    def selected_radio_button_option(self):
        user_input = self.get_text_input()
        radio_button_frequency_option = self.radio_text.get()
        if not income.canvas:
            income.plot_net_income(self, user_input, radio_button_frequency_option)
        else:
            income.clear_plot()
            income.plot_net_income(self, user_input, radio_button_frequency_option)

    def show_error_message(self):
        message_box.show_error_message()

    def clear(self):
        super().clear()
        income.clear_plot()


income = plot_net_income.NetIncomeGraph()
