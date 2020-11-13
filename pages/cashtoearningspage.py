try:
    import Tkinter as tk
except:
    import tkinter as tk
import tkinter.font
from tkinter import *

from pages import homePage
from helpers import messagebox as messagebox
from charts import plotcashbasedearnings as _cash_to_earnings


class CashToEarnings(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self['bg'] = '#1B6666'
        self.controller = controller
        self.my_font = tkinter.font.Font(self, family="Sans Serif", size=20)
        self.page_title = Label(self, text="Cash to Earnings Charts", font=self.my_font)
        self.radio_text = StringVar()
        self.quarterly_text_string = 'q'
        self.yearly_text_string = 'a'

        self.text_input_box = Text(self, relief=tk.RIDGE, height=1, width=8, borderwidth=2)
        self.text_input_box.focus()
        self.frequency_text = Label(self, text="Frequency")
        self.quarterly_radio_button = Radiobutton(self, text="Quarterly", variable=self.radio_text,
                                                  value=self.quarterly_text_string,
                                                  command=self.selectedRadioButtonOption)
        self.yearly_radio_button = Radiobutton(self, text="Annual", variable=self.radio_text,
                                               value=self.yearly_text_string,
                                               command=self.selectedRadioButtonOption)
        self.clear_button = Button(self, text='Clear', command=self.clear, bg='red')

        self.page_title.pack()
        self.text_input_box.pack()
        self.quarterly_radio_button.pack(side='left', padx=50)
        self.yearly_radio_button.pack(side='right', padx=50)
        self.clear_button.pack()

        button1 = Button(self, text="Back to Home",
                         command=lambda: controller.show_frame(homePage.Startpage))

    def getTextInput(self):
        result = self.text_input_box.get("1.0", "end")
        result = result.rstrip()
        if len(result) > 0:
            results = result.upper()
            results = str(results)
            return results
        else:
            self.yearly_radio_button.deselect()
            self.quarterly_radio_button.deselect()
            messagebox.showErrorMessage(self)

    def selectedRadioButtonOption(self):
        user_input = self.getTextInput()
        radio_button_frequency_option = self.radio_text.get()
        if not cash_to_earnings.canvas:
            cash_to_earnings.plotCashToEarnings(self, user_input, radio_button_frequency_option)

        else:
            cash_to_earnings.clearPlotPage()
            cash_to_earnings.plotCashToEarnings(self, user_input, radio_button_frequency_option)

    def clear(self):
        self.text_input_box.delete("1.0", "end")
        cash_to_earnings.clearPlotPage()
        self.yearly_radio_button.deselect()
        self.quarterly_radio_button.deselect()


cash_to_earnings = _cash_to_earnings.CashBasedEarningGraph()
