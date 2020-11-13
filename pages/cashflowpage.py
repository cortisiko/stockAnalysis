try:
    import Tkinter as tk
except:
    import tkinter as tk
import tkinter.font
from tkinter import *

from charts import plotcashflow as pltCashFlow
from helpers import messagebox as messagebox

class CashFlow(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self['bg'] = '#1B6666'
        self.my_font = tkinter.font.Font(self, family="Sans Serif", size=20)
        self.page_title = Label(self, text="Cash Flow Charts", font=self.my_font)
        self.radio_text = StringVar()
        self.quarterly_text_string = 'q'
        self.yearly_text_string = 'a'

        self.text_input_box = Text(self, relief=tk.RIDGE, height=1, width=6, borderwidth=2)
        #self.text_input_box.focus()
        self.frequency_text = Label(self, text="Frequency")
        self.quarterly_radio_button = Radiobutton(self, text="Quarterly", variable=self.radio_text,
                                                value=self.quarterly_text_string, command=self.selected_radio_button_option)
        self.yearly_radio_button = Radiobutton(self, text="Annual", variable=self.radio_text, value=self.yearly_text_string,
                                             command=self.selected_radio_button_option)
        self.clear_button = Button(self, text='Clear', bg='red', command=self.clear)
        self.page_title.pack()
        self.text_input_box.pack()
        self.clear_button.pack()
        self.quarterly_radio_button.pack(side='left', padx=50)
        self.yearly_radio_button.pack(side='right', padx=50)

    def get_text_input(self):
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

    def selected_radio_button_option(self):
        user_input = self.get_text_input()

        radio_button_frequency_option = self.radio_text.get()
        if not cash_flow.canvas:
            cash_flow.plotCashGraph(self, user_input, radio_button_frequency_option)
        else:
            cash_flow.clearPlotPage()
            cash_flow.plotCashGraph(self, user_input, radio_button_frequency_option)

    def clear(self):
        self.text_input_box.delete("1.0", "end")
        cash_flow.clearPlotPage()
        self.yearly_radio_button.deselect()
        self.quarterly_radio_button.deselect()
        self.text_input_box.focus()


cash_flow = pltCashFlow.CashFlowGraph()
