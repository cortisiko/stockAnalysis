import tkinter as tk
import tkinter.font
from tkinter import Label, StringVar, Text, Radiobutton, Button


class BasePage(tk.Frame):
    """
    BasePage is a base class for creating different chart pages in a Tkinter application.
    This class provides common functionalities such as text input, radio buttons, and a clear button

    Attributes:
    parent (tk.Tk): The parent Tkinter widget.
    controller (object): The controller to manage different frames in the application.
    title (str): The title of the page.
    quarterly_text (str): The text value for the quarterly option in the radio button.
    yearly_text (str): The text value for the annual option in the radio button.
    bg_color (str): The background color of the frame.
    """

    def __init__(self, parent, controller, title, quarterly_text, yearly_text, bg_color='#1B6666'):
        """
        Initializes the BasePage with a title, text for quarterly and annual radio buttons, and background color.

        Parameters:
        parent (tk.Tk): The parent Tkinter widget.
        controller (object): The controller to manage different frames in the application.
        title (str): The title of the page.
        quarterly_text (str): The text value for the quarterly option in the radio button.
        yearly_text (str): The text value for the annual option in the radio button.
        bg_color (str): The background color of the frame. Default is '#1B6666'.
        """
        tk.Frame.__init__(self, parent)
        self['bg'] = bg_color
        self.controller = controller
        self.my_font = tkinter.font.Font(self, family="Sans Serif", size=20)
        self.page_title = Label(self, text=title, font=self.my_font)

        self.radio_text = StringVar()
        self.quarterly_text_string = quarterly_text
        self.yearly_text_string = yearly_text

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
        """
        Retrieves and processes the text input from the text box.

        Returns:
        str: The processed text input in uppercase if valid, else None.
        """
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
        """
        Placeholder method to be overridden in derived classes.
        """
        pass

    def clear(self):
        """
        Clears the text input box and deselects the radio buttons.
        """
        self.text_input_box.delete("1.0", "end")
        self.yearly_radio_button.deselect()
        self.quarterly_radio_button.deselect()

    def show_error_message(self):
        """
        Placeholder method to show an error message, to be overridden in derived classes.
        """
        pass
