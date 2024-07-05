import tkinter as tk
import tkinter.font
from tkinter import Label, StringVar, Text, Radiobutton, Button


class BasePage(tk.Frame):
    def __init__(self, parent, controller, title, bg_color='#1B6666'):
        tk.Frame.__init__(self, parent)
        self['bg'] = bg_color
        self.controller = controller
        self.my_font = tkinter.font.Font(self, family="Sans Serif", size=20)
        self.page_title = Label(self, text=title, font=self.my_font)

        self.radio_text = StringVar()
        self.quarterly_text_string = 'quarterly'
        self.yearly_text_string = 'yearly'

        self.text_input_box = Text(self, relief=tk.RIDGE, height=1, width=6, borderwidth=2)
        self.frequency_text = Label(self, text="Frequency")
        self.quarterly_radio_button = Radiobutton(self, text="Quarterly", variable=self.radio_text,
                                                  value=self.quarterly_text_string,
                                                  command=self.selected_radio_button_option)
        self.yearly_radio_button = Radiobutton(self, text="Annual", variable=self.radio_text,
                                               value=self.yearly_text_string,
                                               command=self.selected_radio_button_option)

        self.clear_button = Button(self, text='Clear', command=self.clear, bg='red')
        self.page_title.pack()
        self.text_input_box.pack()
        self.quarterly_radio_button.pack(side='left', padx=50)
        self.yearly_radio_button.pack(side='right', padx=50)
        self.clear_button.pack()

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
            self.show_error_message()

    def selected_radio_button_option(self):
        pass

    def clear(self):
        self.text_input_box.delete("1.0", "end")
        self.yearly_radio_button.deselect()
        self.quarterly_radio_button.deselect()

    def show_error_message(self):
        pass
