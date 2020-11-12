from tkinter import messagebox as message_box
invalid_ticker_error_message = "Sorry, you need to enter a ticker symbol"

def showErrorMessage(self):
    message_box.showerror("Error", invalid_ticker_error_message)