import platform
import threading
import time
import tkinter as tk
import tkinter.font as tkFont
from tkinter import *

if platform.system() == "Darwin":
    from tkmacosx import Button
else:
    from tkinter import Button

from app.financials import analyze as analyze

class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
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

        self.stock_symbol_text = Label(self.input_frame, text="Enter Stock Symbol:", font=self.label_font,
                                       background='#34495e', fg='#ecf0f1')
        self.stock_symbol_text.grid(row=0, column=0, padx=5, pady=5, sticky='w')

        self.text_input_box = Entry(self.input_frame, relief=SOLID, width=20, borderwidth=2, font=self.label_font)
        self.text_input_box.grid(row=0, column=1, padx=5, pady=5, sticky='w')
        self.text_input_box.focus()
        self.text_input_box.bind('<Return>', self.analyze)

        self.analyze_button = Button(self.input_frame, text='Analyze Stock', bg='#27ae60', fg='#ecf0f1',
                                     font=self.label_font, borderless=True, command=self.analyze)
        self.analyze_button.grid(row=0, column=2, padx=5, pady=5, sticky='w')

        self.clear_button = Button(self.input_frame, text="Clear", bg='#c0392b', fg='#ecf0f1', font=self.label_font,
                                   borderless=True, command=self.clear_values)
        self.clear_button.grid(row=0, column=3, padx=5, pady=5, sticky='w')

        # Results Frame
        self.results_frame = Frame(self.content_frame, background='#34495e', bd=2, relief=SOLID)
        self.results_frame.grid(row=1, column=0, pady=5, padx=5, sticky='n')

        self.company_name_label_text = Label(self.results_frame, text="", font=self.my_font, bg='#34495e', fg='#ecf0f1',
                                             anchor="w")
        self.company_name_label_text.grid(row=0, column=0, columnspan=2, pady=5)

        labels = [
            "Sector:", "Current Stock Price:", "Earnings Per Share:",
            "PE Ratio:", "Return on Equity Ratio:", "Debt to Equity Ratio:", "Net Profit Margin:"
        ]
        self.value_labels = {}

        for i, label in enumerate(labels):
            lbl = Label(self.results_frame, text=label, width=25, anchor="w", font=self.label_font, background='#34495e',
                        fg='#ecf0f1')
            lbl.grid(row=i + 1, column=0, padx=5, pady=5, sticky='w')
            value_label = Label(self.results_frame, text="", width=25, anchor="w", font=self.label_font,
                                background='#34495e', fg='#ecf0f1')
            value_label.grid(row=i + 1, column=1, padx=5, pady=5, sticky='w')
            self.value_labels[label] = value_label

        self.parent.bind('<Return>', self.analyze)

    def analyze(self, event=None):
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
                    self.controller.after(0, self.update_company_name, company_name)
                    self.controller.after(0, self.update_value, 'Sector:', self.get_company_sector())
                    self.controller.after(0, self.update_value, 'Current Stock Price:', self.current_stock_price())
                    self.controller.after(0, self.update_value, 'Earnings Per Share:', self.get_eps())
                    self.controller.after(0, self.update_value, 'PE Ratio:', self.get_pe_ratio())
                    self.controller.after(0, self.update_value, 'Return on Equity Ratio:', self.get_return_on_equity())
                    self.controller.after(0, self.update_value, 'Debt to Equity Ratio:', self.get_debt_to_equity_ratio())
                    self.controller.after(0, self.update_value, 'Net Profit Margin:', self.get_profit_margin())
                else:
                    self.show_error("User did not enter a valid ticker")

            finally:
                self.controller.after(0, lambda: self.set_widget_state('normal'))
                self.controller.after(0, self.clear_user_input_box)

        analysis_thread = threading.Thread(target=analyze_thread)
        analysis_thread.start()

    def set_widget_state(self, state):
        for widget in (self.text_input_box, self.analyze_button, self.clear_button):
            widget.config(state=state)

    def update_company_name(self, value):
        self.company_name_label_text["text"] = value

    def update_value(self, label, value):
        if label in self.value_labels:
            try:
                self.controller.after(0, self._update_value_gui, label, value)
            except KeyError as e:
                print(f"KeyError: {e} while updating {label} with value {value}")
            except Exception as e:
                print(f"Unexpected error: {e}")
        else:
            print(f"Label '{label}' not found in value_labels.")

    def _update_value_gui(self, label, value):
        self.value_labels[label]["text"] = value
        print(f"Updated {label} to {value}")

    def get_text_input(self):
        return self.text_input_box.get().strip().upper()

    def get_company_name(self):
        ticker = self.get_text_input()
        return str(analyze.get_stock_name(ticker))

    def get_company_sector(self):
        ticker = self.get_text_input()
        return str(analyze.get_company_sector(ticker))

    def get_eps(self):
        ticker = self.get_text_input()
        return f'${analyze.get_eps(ticker)}'

    def get_pe_ratio(self):
        ticker = self.get_text_input()
        return str(analyze.get_pe_ratio(ticker))

    def get_return_on_equity(self):
        ticker = self.get_text_input()
        return f'{analyze.get_return_on_equity(ticker)}%'

    def current_stock_price(self):
        ticker = self.get_text_input()
        return f'${analyze.get_current_stock_price(ticker)}'

    def get_debt_to_equity_ratio(self):
        ticker = self.get_text_input()
        return str(analyze.get_debt_to_equity(ticker))

    def get_profit_margin(self):
        ticker = self.get_text_input()
        return f'{analyze.get_profit_margin(ticker)}%'

    def clear_values(self):
        self.company_name_label_text["text"] = ""
        for label in self.value_labels.values():
            label["text"] = ""

    def clear_user_input_box(self):
        self.text_input_box.delete(0, END)

    def show_error(self, message):
        error_window = Toplevel(self)
        error_window.title("Error")
        error_label = Label(error_window, text=message, font=self.label_font, fg='red')
        error_label.pack(padx=20, pady=20)
        ok_button = Button(error_window, text="OK", command=error_window.destroy)
        ok_button.pack(pady=10)
