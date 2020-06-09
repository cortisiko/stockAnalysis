from tkinter import messagebox as messageBox
invalidTickerErrorMessage = "Sorry, you need to enter a ticker symbol"

def showErrorMessage(self):
    messageBox.showerror("Error", invalidTickerErrorMessage)