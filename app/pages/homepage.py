"""
  StartPage class is the initial frame of the application where users can input
    a stock symbol and get various financial details about the stock.
"""

import platform
import threading
import time
import tkinter as tk
import tkinter.font as tkFont
from tkinter import Frame, Label, Entry, Toplevel, END, SOLID
from app.financials import analyze

if platform.system() == "Darwin":
    from tkmacosx import Button
else:
    from tkinter import Button



class StartPage(tk.Frame):
    """
    StartPage class is the initial frame of the application where users can input
    a stock symbol and get various financial details about the stock.

    Attributes:
        parent (tk.Tk): The root window or master frame.
        controller (tk.Tk): The main controller handling the different frames.
        my_font (tkFont.Font): The font used for the title and company name.
        label_font (tkFont.Font): The font used for labels and text inputs.
        title_frame (Frame): The frame containing the title and logo.
        content_frame (Frame): The frame containing the main content.
        input_frame (Frame): The frame containing the input fields and buttons.
        results_frame (Frame): The frame displaying the results of the analysis.
        stock_symbol_text (Label): The label for the stock symbol input.
        text_input_box (Entry): The entry widget for stock symbol input.
        analyze_button (Button): The button to trigger stock analysis.
        clear_button (Button): The button to clear input and results.
        company_name_label_text (Label): The label displaying the company name.
        value_labels (dict): A dictionary mapping labels to their value display widgets.
    """

    def __init__(self, parent, controller):
        """
        Initializes the StartPage frame.

        Args:
            parent (tk.Tk): The parent frame or window.
            controller (tk.Tk): The main controller handling the different frames.
        """
        tk.Frame.__init__(self, parent)
        # pylint: disable=too-many-instance-attributes
        self.controller = controller
        self.parent = parent
        self.configure(background='#2c3e50')

        self.my_font = tkFont.Font(self, family="Helvetica", size=20, weight="bold")
        self.label_font = tkFont.Font(self, family="Helvetica", size=12)

        # Configure grid layout for the root frame
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Title and Logo
        self.title_frame = Frame(self, background='#2c3e50')
        self.title_frame.grid(row=0, column=0, pady=5, padx=5, sticky='n')

        # Center content
        self.content_frame = Frame(self, background='#2c3e50')
        self.content_frame.grid(row=1, column=0, pady=(100, 0), padx=5, sticky='n')
        self.content_frame.grid_rowconfigure(0, weight=1)
        self.content_frame.grid_columnconfigure(0, weight=1)

        # Configure grid layout for the content frame
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Input Frame
        self.input_frame = Frame(self.content_frame, background='#34495e', bd=2, relief=SOLID)
        self.input_frame.grid(row=0, column=0, pady=5, padx=5, sticky='n')
        # pylint: disable=line-too-long
        self.stock_symbol_text = Label(self.input_frame, text="Enter Stock Symbol:", font=self.label_font,
                                       background='#34495e', fg='#ecf0f1')
        self.stock_symbol_text.grid(row=0, column=0, padx=5, pady=5, sticky='w')
        # pylint: disable=line-too-long
        self.text_input_box = Entry(self.input_frame, relief=SOLID, width=20, borderwidth=2, font=self.label_font)
        self.text_input_box.grid(row=0, column=1, padx=5, pady=5, sticky='w')
        self.text_input_box.focus()
        self.text_input_box.bind('<Return>', self.analyze)
        # pylint: disable=line-too-long
        self.analyze_button = Button(self.input_frame, text='Analyze Stock', bg='#27ae60', fg='#ecf0f1',
                                     font=self.label_font, borderless=True, command=self.analyze)
        self.analyze_button.grid(row=0, column=2, padx=5, pady=5, sticky='w')
        # pylint: disable=line-too-long
        self.clear_button = Button(self.input_frame, text="Clear", bg='#c0392b', fg='#ecf0f1', font=self.label_font,
                                   borderless=True, command=self.clear_values)
        self.clear_button.grid(row=0, column=3, padx=5, pady=5, sticky='w')

        # Results Frame
        self.results_frame = Frame(self.content_frame, background='#34495e', bd=2, relief=SOLID)
        self.results_frame.grid(row=1, column=0, pady=5, padx=5, sticky='n')
        # pylint: disable=line-too-long
        self.company_name_label_text = Label(self.results_frame, text="", font=self.my_font, bg='#34495e', fg='#ecf0f1',
                                             anchor="w")
        self.company_name_label_text.grid(row=0, column=0, columnspan=2, pady=5)

        labels = [
            "Sector:", "Current Stock Price:", "Earnings Per Share:",
            "PE Ratio:", "Return on Equity Ratio:", "Debt to Equity Ratio:", "Net Profit Margin:"
        ]
        self.value_labels = {}

        for i, label in enumerate(labels):
            lbl = Label(self.results_frame, text=label, width=25, anchor="w", font=self.label_font,
                        background='#34495e', fg='#ecf0f1')
            lbl.grid(row=i + 1, column=0, padx=5, pady=5, sticky='w')
            # pylint: disable=line-too-long
            value_label = Label(self.results_frame, text="", width=25, anchor="w", font=self.label_font,
                                background='#34495e', fg='#ecf0f1')
            value_label.grid(row=i + 1, column=1, padx=5, pady=5, sticky='w')
            self.value_labels[label] = value_label

        self.parent.bind('<Return>', self.analyze)

    def analyze(self, event=None):
        # pylint: disable=unused-argument
        """
        Initiates stock analysis in a separate thread.

        Args:
            event (tk.Event, optional): The event that triggered the method call.
        """
        def analyze_thread():
            ticker = self.get_text_input()
            if not ticker:
                self.show_error("Please enter a valid stock symbol.")
                return

            self.controller.after(0, self.clear_values)
            self.controller.after(0, lambda: self.set_widget_state('disabled'))

            time.sleep(1)  # Simulate delay for demo purposes
            try:
                company_name = self.get_company_name()
                if company_name is not None:
                    # pylint: disable=line-too-long
                    self.controller.after(0, self.update_company_name, company_name)
                    # pylint: disable=line-too-long
                    self.controller.after(0, self.update_value, 'Sector:', self.get_company_sector())
                    # pylint: disable=line-too-long
                    self.controller.after(0, self.update_value, 'Current Stock Price:', self.current_stock_price())
                    # pylint: disable=line-too-long
                    self.controller.after(0, self.update_value, 'Earnings Per Share:', self.get_eps())
                    # pylint: disable=line-too-long
                    self.controller.after(0, self.update_value, 'PE Ratio:', self.get_pe_ratio())
                    # pylint: disable=line-too-long
                    self.controller.after(0, self.update_value, 'Return on Equity Ratio:', self.get_return_on_equity())
                    # pylint: disable=line-too-long
                    self.controller.after(0, self.update_value, 'Debt to Equity Ratio:', self.get_debt_to_equity_ratio())
                    # pylint: disable=line-too-long
                    self.controller.after(0, self.update_value, 'Net Profit Margin:', self.get_profit_margin())
                else:
                    self.show_error("User did not enter a valid ticker")
            finally:
                self.controller.after(0, lambda: self.set_widget_state('normal'))
                self.controller.after(0, self.clear_user_input_box)

        analysis_thread = threading.Thread(target=analyze_thread)
        analysis_thread.start()

    def set_widget_state(self, state):
        """
        Sets the state of the input and button widgets.

        Args:
            state (str): The state to set the widgets to ('normal' or 'disabled').
        """
        for widget in (self.text_input_box, self.analyze_button, self.clear_button):
            widget.config(state=state)

    def update_company_name(self, value):
        """
        Updates the company name label.

        Args:
            value (str): The company name to display.
        """
        self.company_name_label_text["text"] = value

    def update_value(self, label, value):
        """
        Updates the value of a specified label.

        Args:
            label (str): The label to update.
            value (str): The value to set for the label.
        """
        if label in self.value_labels:
            try:
                self.controller.after(0, self._update_value_gui, label, value)
            except (AttributeError, KeyError, TypeError, ValueError) as e:
                print(f"KeyError: {e} while updating {label} with value {value}")
        else:
            print(f"Label '{label}' not found in value_labels.")

    def _update_value_gui(self, label, value):
        """
        Internal method to update the GUI for a specified label.

        Args:
            label (str): The label to update.
            value (str): The value to set for the label.
        """
        self.value_labels[label]["text"] = value
        print(f"Updated {label} to {value}")

    def get_text_input(self):
        """
        Retrieves the text input from the entry widget.

        Returns:
            str: The text input in uppercase.
        """
        return self.text_input_box.get().strip().upper()

    def get_company_name(self):
        """
        Retrieves the company name based on the stock symbol.

        Returns:
            str: The company name.
        """
        ticker = self.get_text_input()
        return str(analyze.get_stock_name(ticker))

    def get_company_sector(self):
        """
        Retrieves the company sector based on the stock symbol.

        Returns:
            str: The company sector.
        """
        ticker = self.get_text_input()
        return str(analyze.get_company_sector(ticker))

    def get_eps(self):
        """
        Retrieves the earnings per share (EPS) based on the stock symbol.

        Returns:
            str: The EPS.
        """
        ticker = self.get_text_input()
        return f'${analyze.get_eps(ticker)}'

    def get_pe_ratio(self):
        """
        Retrieves the price-to-earnings (PE) ratio based on the stock symbol.

        Returns:
            str: The PE ratio.
        """
        ticker = self.get_text_input()
        return str(analyze.get_pe_ratio(ticker))

    def get_return_on_equity(self):
        """
        Retrieves the return on equity (ROE) ratio based on the stock symbol.

        Returns:
            str: The ROE ratio.
        """
        ticker = self.get_text_input()
        return f'{analyze.get_return_on_equity(ticker)}%'

    def current_stock_price(self):
        """
        Retrieves the current stock price based on the stock symbol.

        Returns:
            str: The current stock price.
        """
        ticker = self.get_text_input()
        return f'${analyze.get_current_stock_price(ticker)}'

    def get_debt_to_equity_ratio(self):
        """
        Retrieves the debt-to-equity ratio based on the stock symbol.

        Returns:
            str: The debt-to-equity ratio.
        """
        ticker = self.get_text_input()
        return str(analyze.get_debt_to_equity(ticker))

    def get_profit_margin(self):
        """
        Retrieves the net profit margin based on the stock symbol.

        Returns:
            str: The net profit margin.
        """
        ticker = self.get_text_input()
        return f'{analyze.get_profit_margin(ticker)}%'

    def clear_values(self):
        """
        Clears the values in the result labels.
        """
        self.company_name_label_text["text"] = ""
        for label in self.value_labels.values():
            label["text"] = ""

    def clear_user_input_box(self):
        """
        Clears the user input text box.
        """
        self.text_input_box.delete(0, END)

    def show_error(self, message):
        """
        Displays an error message in a new window.

        Args:
            message (str): The error message to display.
        """
        error_window = Toplevel(self)
        error_window.title("Error")
        error_label = Label(error_window, text=message, font=self.label_font, fg='red')
        error_label.pack(padx=20, pady=20)
        ok_button = Button(error_window, text="OK", command=error_window.destroy)
        ok_button.pack(pady=10)
