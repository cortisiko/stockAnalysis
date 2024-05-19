import platform
import threading
import time
import tkinter as tk
import tkinter.font as tkFont
from tkinter import *

from openai import OpenAI
# Conditionally import Button from tkmacosx for macOS
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

        # Title and Logo
        self.title_frame = Frame(self, background='#2c3e50')
        self.title_frame.grid(row=0, column=0, pady=10, padx=10, sticky='ew')

        # self.title_label = Label(self.title_frame, text="Stock Analysis", font=self.my_font, background='#2c3e50', fg='#ecf0f1')
        # self.title_label.grid(row=0, column=0, padx=10, pady=10, sticky='ew')

        # Center content
        self.content_frame = Frame(self, background='#2c3e50')
        self.content_frame.grid(row=1, column=0, pady=10, padx=10, sticky='nsew')
        self.content_frame.grid_rowconfigure(0, weight=1)
        self.content_frame.grid_columnconfigure(0, weight=1)

        # Input Frame
        self.input_frame = Frame(self.content_frame, background='#34495e', bd=2, relief=SOLID)
        self.input_frame.grid(row=0, column=0, pady=10, padx=10, sticky='n')

        self.stock_symbol_text = Label(self.input_frame, text="Enter Stock Symbol:", font=self.label_font, background='#34495e', fg='#ecf0f1')
        self.stock_symbol_text.grid(row=0, column=0, padx=10, pady=10, sticky='w')

        self.text_input_box = Entry(self.input_frame, relief=SOLID, width=20, borderwidth=2, font=self.label_font)
        self.text_input_box.grid(row=0, column=1, padx=10, pady=10, sticky='w')
        self.text_input_box.focus()
        self.text_input_box.bind('<Return>', self.analyze)

        # Use Button from tkmacosx for better styling on macOS
        self.analyze_button = Button(self.input_frame, text='Analyze Stock', bg='#27ae60', fg='#ecf0f1', font=self.label_font, borderless=True, command=self.analyze)
        self.analyze_button.grid(row=0, column=2, padx=10, pady=10, sticky='w')

        self.clear_button = Button(self.input_frame, text="Clear", bg='#c0392b', fg='#ecf0f1', font=self.label_font, borderless=True, command=self.clear_values)
        self.clear_button.grid(row=0, column=3, padx=10, pady=10, sticky='w')

        # Results Frame
        self.results_frame = Frame(self.content_frame, background='#34495e', bd=2, relief=SOLID)
        self.results_frame.grid(row=1, column=0, pady=10, padx=10, sticky='n')

        self.company_name_label_text = Label(self.results_frame, text="", font=self.my_font, bg='#34495e', fg='#ecf0f1', anchor="w")
        self.company_name_label_text.grid(row=0, column=0, columnspan=2, pady=10)

        labels = [
            "Sector:", "Current Stock Price:", "Earnings Per Share:",
            "PE Ratio:", "Return on Equity Ratio:", "Debt to Equity Ratio:", "Net Profit Margin:"
        ]
        self.value_labels = {}
        self.skeleton_loaders = {}

        for i, label in enumerate(labels):
            lbl = Label(self.results_frame, text=label, width=25, anchor="w", font=self.label_font, background='#34495e', fg='#ecf0f1')
            lbl.grid(row=i + 1, column=0, padx=10, pady=5, sticky='w')
            canvas = Canvas(self.results_frame, width=200, height=20, bg='#34495e', highlightthickness=0)
            canvas.grid(row=i + 1, column=1, padx=10, pady=5, sticky='w')
            self.skeleton_loaders[label] = canvas
            self.value_labels[label] = Label(self.results_frame, text="", width=25, anchor="w", font=self.label_font, background='#34495e', fg='#ecf0f1')

        # Bindings
        self.parent.bind('<Return>', self.analyze)

    def analyze(self, event=None):
        def analyze_thread():
            # Disable input elements during analysis
            for widget in (self.text_input_box, self.analyze_button, self.clear_button):
                widget.config(state='disabled')

            self.set_skeleton_loaders()  # Set skeleton loaders before starting the analysis thread

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
                    print("User did not enter a valid ticker")
            except Exception as e:
                print(f"An error occurred: {e}")
            finally:
                # Enable input elements after analysis
                for widget in (self.text_input_box, self.analyze_button, self.clear_button):
                    widget.config(state='normal')
                self.controller.after(0, self.clear_user_input_box)

        analysis_thread = threading.Thread(target=analyze_thread)
        analysis_thread.start()

    def set_skeleton_loaders(self):
        for label, canvas in self.skeleton_loaders.items():
            canvas.delete("all")
            rect_id = canvas.create_rectangle(10, 2, 190, 18, fill="light gray", outline="")
            self.animate_loader(canvas, rect_id)

    def animate_loader(self, canvas, rect_id):
        def animate():
            colors = ["#ecf0f1", "#bdc3c7", "#7f8c8d"]
            for i in range(3):
                canvas.after(100 * i, lambda c=canvas, col=colors[i], id=rect_id: c.itemconfig(id, fill=col))

        animate()

    def update_company_name(self, value):
        self.company_name_label_text["text"] = value

    def update_value(self, label, value):
        if label in self.value_labels:
            try:
                row_info = self.skeleton_loaders[label].grid_info()  # Get grid info before removing
                self.skeleton_loaders[label].grid_remove()
                self.value_labels[label]["text"] = value
                self.value_labels[label].grid(row=row_info["row"], column=1, padx=10, pady=5, sticky='w')
            except KeyError as e:
                print(f"KeyError: {e} while updating {label} with value {value}")
            except Exception as e:
                print(f"Unexpected error: {e}")
        else:
            print(f"Label '{label}' not found in value_labels.")

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
        for canvas in self.skeleton_loaders.values():
            canvas.delete("all")

    def clear_user_input_box(self):
        self.text_input_box.delete(0, END)



