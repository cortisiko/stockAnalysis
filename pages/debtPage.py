try:
    import Tkinter as tk
except:
    import tkinter as tk
import tkinter.font
from tkinter import *

from charts import plotlongtermdebt as pltDebt
from helpers import messagebox as messagebox
from pages import homePage

class Debt(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self['bg'] = '#1B6666'
        self.controller = controller
        self.my_font = tkinter.font.Font(self, family="Sans Serif", size=20)
        self.pageTitle = Label(self, text="Long Term Debt Charts", font=self.my_font)
        self.RadioText = StringVar()
        self.quarterlyTextString = 'q'
        self.yearlyTextString = 'a'

        self.textInputBox = Text(self, relief=tk.RIDGE, height=1, width=6, borderwidth=2)
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

            messagebox.showErrorMessage(self)

    def selectedRadioButtonOption(self):
        userInput = self.getTextInput()
        radioButtonFrequencyOption = self.RadioText.get()
        #if TypeError:
          #      messagebox.showErrorMessage(self, invalidTickerErrorMessage)
        #if KeyError:
         #   messagebox.showErrorMessage(self,noDebtErrorMessage)
        if not longTermDebt.canvas:
            longTermDebt.plotDebtGraph(self, userInput, radioButtonFrequencyOption)

        else:
            longTermDebt.clearPlotPage()
            longTermDebt.plotDebtGraph(self, userInput, radioButtonFrequencyOption)

    def destroyGraph(self):
        longTermDebt.clearPlotPage()

    def clear(self):
        self.textInputBox.delete("1.0", "end")
        longTermDebt.clearPlotPage()
        self.yearlyRadioButton.deselect()
        self.quarterlyRadioButton.deselect()



longTermDebt = pltDebt.PlotGraph()
