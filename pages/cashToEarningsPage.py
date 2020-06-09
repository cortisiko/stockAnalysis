try:
    import Tkinter as tk
except:
    import tkinter as tk
import tkinter.font
from tkinter import *

from pages import homePage
from helpers import getMessageBox as messagebox
from charts import cashBasedEarningsChart as cashToEarnings

invalidTickerErrorMessage = "Sorry, you need to enter a ticker symbol"

class plotCashToEarnings(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self['bg'] = '#1B6666'
        self.controller = controller
        self.my_font = tkinter.font.Font(self, family="Sans Serif", size=20)
        self.pageTitle = Label(self, text="Cash to Earnings Charts", font=self.my_font)
        self.RadioText = StringVar()
        self.quarterlyTextString = 'q'
        self.yearlyTextString = 'a'

        self.textInputBox = Text(self, relief=tk.RIDGE, height=1, width=8, borderwidth=2)
        self.textInputBox.focus()
        self.frequencyText = Label(self, text="Frequency")
        self.quarterlyRadioButton = Radiobutton(self, text="Quarterly", variable=self.RadioText,
                                                value=self.quarterlyTextString, command=self.selectedRadioButtonOption)
        self.yearlyRadioButton = Radiobutton(self, text="Annual", variable=self.RadioText, value=self.yearlyTextString,
                                             command=self.selectedRadioButtonOption)
        self.clearButton = Button(self, text='Clear', command=self.clear, bg='red')

        self.pageTitle.pack()
        self.textInputBox.pack()
        self.quarterlyRadioButton.pack(side='left', padx=50)
        self.yearlyRadioButton.pack(side='right', padx=50)
        self.clearButton.pack()

        button1 = Button(self, text="Back to Home",
                         command=lambda: controller.show_frame(homePage.Startpage))

    def getTextInput(self):
        result = self.textInputBox.get("1.0", "end")
        result = result.rstrip()
        if len(result) > 0:
            results = result.upper()
            results = str(results)
            return results
        else:
            self.yearlyRadioButton.deselect()
            self.quarterlyRadioButton.deselect()
            messagebox.showErrorMessage(self,invalidTickerErrorMessage)

    def selectedRadioButtonOption(self):
        userInput = self.getTextInput()
        radioButtonFrequencyOption = self.RadioText.get()
        if not cashtoEarnings.canvas:
            cashtoEarnings.plotCashToEarnings(self, userInput, radioButtonFrequencyOption)

        else:
            cashtoEarnings.clearPlotPage()
            cashtoEarnings.plotCashToEarnings(self, userInput, radioButtonFrequencyOption)

    def clear(self):
        self.textInputBox.delete("1.0", "end")
        cashtoEarnings.clearPlotPage()
        self.yearlyRadioButton.deselect()
        self.quarterlyRadioButton.deselect()

cashtoEarnings = cashToEarnings.PlotGraph()
