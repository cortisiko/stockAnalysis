from app.charts import plot_revenue
from app.helpers import message_box
from app.pages.base_page import BasePage


class Revenue(BasePage):
    def __init__(self, parent, controller):
        super().__init__(parent, controller, "Revenue Charts", 'quarterly', 'yearly')

    def selected_radio_button_option(self):
        user_input = self.get_text_input()
        radio_button_frequency_option = self.radio_text.get()
        if not revenue.canvas:
            revenue.plot_revenue(self, user_input, radio_button_frequency_option)
        else:
            revenue.clear_plot()
            revenue.plot_revenue(self, user_input, radio_button_frequency_option)

    def show_error_message(self):
        message_box.show_error_message()

    def clear(self):
        super().clear()
        revenue.clear_plot()


revenue = plot_revenue.RevenueGraph()
