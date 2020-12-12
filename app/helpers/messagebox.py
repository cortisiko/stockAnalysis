from tkinter import messagebox as message_box
invalid_ticker_error_message = "Sorry, you need to enter a valid ticker symbol. ETF's and mutual funds do not count!"

def showErrorMessage(self):
    message_box.showerror("Error", invalid_ticker_error_message)