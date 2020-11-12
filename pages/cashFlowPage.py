try:
    import Tkinter as tk
except:
    import tkinter as tk
import tkinter.font
from tkinter import *

from charts import plotcashflow as pltCashFlow
from helpers import messagebox as messagebox

class CashFlow(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self['bg'] = '#1B6666'
        self.my_font = tkinter.font.Font(self, family="Sans Serif", size=20)
        self.pageTitle = Label(self, text="Cash Flow Charts", font=self.my_font)
        self.RadioText = StringVar()
        self.quarterlyTextString = 'q'
        self.yearlyTextString = 'a'

        self.textInputBox = Text(self, relief=tk.RIDGE, height=1, width=6, borderwidth=2)
        #self.textInputBox.focus()
        self.frequencyText = Label(self, text="Frequency")
        self.quarterlyRadioButton = Radiobutton(self, text="Quarterly", variable=self.RadioText,
                                                value=self.quarterlyTextString, command=self.selectedRadioButtonOption)
        self.yearlyRadioButton = Radiobutton(self, text="Annual", variable=self.RadioText, value=self.yearlyTextString,
                                             command=self.selectedRadioButtonOption)
        self.clearButton = Button(self, text='Clear', bg='red', command=self.clear)
        self.pageTitle.pack()
        self.textInputBox.pack()
        self.clearButton.pack()
        self.quarterlyRadioButton.pack(side='left', padx=50)
        self.yearlyRadioButton.pack(side='right', padx=50)

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
            messagebox.showErrorMessage(self)

    def selectedRadioButtonOption(self):
        userInput = self.getTextInput()

        radioButtonFrequencyOption = self.RadioText.get()
        if not cashFlow.canvas:
            cashFlow.plotCashGraph(self, userInput, radioButtonFrequencyOption)
        else:
            cashFlow.clearPlotPage()
            cashFlow.plotCashGraph(self, userInput, radioButtonFrequencyOption)

    def clear(self):
        self.textInputBox.delete("1.0", "end")
        cashFlow.clearPlotPage()
        self.yearlyRadioButton.deselect()
        self.quarterlyRadioButton.deselect()
        self.textInputBox.focus()


cashFlow = pltCashFlow.CashFlowGraph()
