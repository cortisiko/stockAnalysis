"""
BasePage is a base class for creating different chart pages in a Tkinter application.
"""
import platform

import tkinter as tk
import tkinter.font
from tkinter import Label, StringVar, Text, Radiobutton

if platform.system() == "Darwin":
    from tkmacosx import Button
else:
    from tkinter import Button


class BasePage(tk.Frame):
    # pylint: disable=too-many-instance-attributes
    """
    BasePage is a base class for creating different chart pages in a Tkinter application.
    This class provides common functionalities such as text input, radio buttons, and a clear button.

    Attributes:
    parent (tk.Tk): The parent Tkinter widget.
    controller (object): The controller to manage different frames in the application.
    title (str): The title of the page.
    quarterly_text (str): The text value for the quarterly option in the radio button.
    yearly_text (str): The text value for the annual option in the radio button.
    bg_color (str): The background color of the frame.
    """

    # pylint: disable=line-too-long

    def __init__(self, parent, controller, title, quarterly_text, yearly_text, bg_color='#2C3E50', fg_color='white'):
        # pylint: disable=too-many-arguments
        """
        Initializes the BasePage with a title, text for quarterly and annual radio buttons, and background color.

        Parameters:
        parent (tk.Tk): The parent Tkinter widget.
        controller (object): The controller to manage different frames in the application.
        title (str): The title of the page.
        quarterly_text (str): The text value for the quarterly option in the radio button.
        yearly_text (str): The text value for the annual option in the radio button.
        bg_color (str): The background color of the frame. Default is '#2C3E50'.
        fg_color (str): The foreground (text) color of the widgets. Default is 'white'.
        """
        tk.Frame.__init__(self, parent, bg=bg_color)
        self.controller = controller
        self.my_font = tkinter.font.Font(self, family="Sans Serif", size=20)

        self.page_title = Label(self, text=title, font=self.my_font, bg=bg_color, fg=fg_color)
        self.page_title.pack(pady=10)

        self.radio_text = StringVar()
        self.quarterly_text_string = quarterly_text
        self.yearly_text_string = yearly_text

        self.text_input_box = Text(self, relief=tk.RIDGE, height=1, width=6, borderwidth=2, bg='#34495E', fg=fg_color)
        self.text_input_box.pack(pady=5)

        self.quarterly_radio_button = Radiobutton(
            self, text="Quarterly", variable=self.radio_text, value=self.quarterly_text_string,
            command=self.selected_radio_button_option, bg=bg_color, fg=fg_color, selectcolor='#34495E'
        )
        self.quarterly_radio_button.pack(side='left', padx=50)

        self.yearly_radio_button = Radiobutton(
            self, text="Annual", variable=self.radio_text, value=self.yearly_text_string,
            command=self.selected_radio_button_option, bg=bg_color, fg=fg_color, selectcolor='#34495E'
        )
        self.yearly_radio_button.pack(side='right', padx=50)

        self.clear_button = Button(self, text='Clear', command=self.clear, bg='red', fg=fg_color)
        self.clear_button.pack(pady=10)

    def get_text_input(self):
        """
        Retrieves and processes the text input from the text box.

        Returns:
            str: The processed text input in uppercase if valid, else None.
        """
        result = self.text_input_box.get("1.0", "end").rstrip()
        if len(result) > 0:
            return result.upper()

        self.yearly_radio_button.deselect()
        self.quarterly_radio_button.deselect()
        self.show_error_message()
        return None

    def selected_radio_button_option(self):
        """
        Placeholder method to be overridden in derived classes.
        """
        # pylint: disable=unnecessary-pass)
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
        # pylint: disable=unnecessary-pass)
        pass
