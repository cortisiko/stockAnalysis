try:
    import Tkinter as tk
except:
    import tkinter as tk
import tkinter.font
from tkinter import *
from pages import homePage

from charts import plotearnings as pltEarnings
from helpers import messagebox as messagebox


class plotEarningsChart(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self['bg'] = '#1B6666'
        self.controller = controller
        self.my_font = tkinter.font.Font(self, family="Sans Serif", size=20)
        self.pageTitle = Label(self, text="Earnings Charts", font=self.my_font)
        self.RadioText = StringVar()
        self.quarterlyTextString = 'quarterly'
        self.yearlyTextString = 'yearly'

        self.textInputBox = Text(self, relief=tk.RIDGE, height=1, width=6, borderwidth=2)
        self.frequencyText = Label(self, text="Frequency")
        self.quarterlyRadioButton = Radiobutton(self, text="Quarterly", variable=self.RadioText,
                                                value=self.quarterlyTextString, command=self.selectedRadioButtonOption)
        self.yearlyRadioButton = Radiobutton(self, text="Annual", variable=self.RadioText, value=self.yearlyTextString,
                                             command=self.selectedRadioButtonOption)

        # self.plotGraphButton = tk.Button(self, text='plot Income Statement', command=self.incomeStatementChart)

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
            messagebox.showErrorMessage(self)

    def selectedRadioButtonOption(self):
        userInput = self.getTextInput()
        radioButtonFrequencyOption = self.RadioText.get()
        if not earnings.canvas:
            earnings.plot_earnings(self, userInput, radioButtonFrequencyOption)
        else:
            earnings.clear_plot()
            earnings.plot_earnings(self, userInput, radioButtonFrequencyOption)

    def destroyGraph(self):
        earnings.clearPlotPage()

    def clear(self):
        self.textInputBox.delete("1.0", "end")
        earnings.clearPlotPage()
        self.yearlyRadioButton.deselect()
        self.quarterlyRadioButton.deselect()


earnings = pltEarnings.PlotGraph()
