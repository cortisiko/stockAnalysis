from app.pages import homepage
from app.charts import plot_cash_flow
from app.helpers import message_box
from app.pages.base_page import BasePage


class CashFlow(BasePage):
    def __init__(self, parent, controller):
        super().__init__(parent, controller, "Cash Flow Charts", 'q', 'a')

    def selected_radio_button_option(self):
        user_input = self.get_text_input()
        radio_button_frequency_option = self.radio_text.get()
        if not cash_flow.canvas:
            cash_flow.plot_cash_graph(self, user_input, radio_button_frequency_option)
        else:
            cash_flow.clear_plot()
            cash_flow.plot_cash_graph(self, user_input, radio_button_frequency_option)

    def show_error_message(self):
        message_box.show_error_message()

    def clear(self):
        super().clear()
        cash_flow.clear_plot()
        self.text_input_box.focus()


cash_flow = plot_cash_flow.CashFlowGraph()
