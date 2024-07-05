try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk
import tkinter.font
from tkinter import Label, StringVar, Text, Radiobutton, Button

from app.helpers import message_box
from app.charts import plot_cash_based_earnings
from app.pages.base_page import BasePage


class CashToEarnings(BasePage):
    def __init__(self, parent, controller):
        super().__init__(parent, controller, "Cash to Earnings Charts", 'q', 'a', bg_color='#1B6666')
        self.text_input_box.config(width=8)
        self.text_input_box.focus()

    def selected_radio_button_option(self):
        user_input = self.get_text_input()
        radio_button_frequency_option = self.radio_text.get()
        if not cash_to_earnings.canvas:
            cash_to_earnings.plot_cash_to_earnings(self, user_input, radio_button_frequency_option)
        else:
            cash_to_earnings.clear_plot()
            cash_to_earnings.plot_cash_to_earnings(self, user_input, radio_button_frequency_option)

    def show_error_message(self):
        message_box.show_error_message()

    def clear(self):
        super().clear()
        cash_to_earnings.clear_plot()


cash_to_earnings = plot_cash_based_earnings.CashBasedEarningGraph()
