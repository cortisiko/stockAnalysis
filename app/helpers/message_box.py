"""
Helper method for error messages
"""
from tkinter import messagebox as message_box

# pylint: disable=line-too-long
INVALID_TICKER_ERROR_MESSAGE = "Sorry, you need to enter a valid ticker symbol. ETF's and mutual funds do not count!"


def show_error_message():
    """
    Method to display error message
    :return:
    """
    message_box.showerror("Error", INVALID_TICKER_ERROR_MESSAGE)
