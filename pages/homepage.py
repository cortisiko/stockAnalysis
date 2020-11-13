try:
    import Tkinter as tk
except:
    import tkinter as tk
import tkinter.font
from tkinter import *
from PIL import ImageTk, Image as kkImage

from Financials import analyze as anlyze
from helpers import messagebox as messagebox

class Startpage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.parent = parent
        self.configure(background='grey')
        self.my_font = tkinter.font.Font(self, family="Comic Sans MS", size=20)
        self.stock_symbo_text = Label(self, text="Enter Stock Symbol: ")
        self.text_input_box = Entry(self,relief=RIDGE, width=10, borderwidth=4)
        self.analyze_button = Button(self,
                                    text='Analyze Stock', relief=RAISED, borderwidth=7, bg='green',
                                    command=self.analyze)
        self.clear_button = Button(self, text="Clear", relief=RIDGE, command=self.clearValues)
        self.text_input_box.focus()
        self.clear_button = Button(self, text="Clear", relief=RIDGE, command=self.clearValues, bg='red')
        # self.graphCashFlowButton = Button(self, text="See Cash Flow Graph",command=lambda: controller.show_frame(PlotCashFlowChart))

        self.earnings_per_share_label_text = Label(self, text="Earnings Per Share: ", width=30, anchor="w")
        self.pe_ratio_label_text = Label(self, text="PE Ratio: ", width=30, anchor="w")
        self.return_on_equity_label_text = Label(self, text="Return on Equity Ratio: ", width=30, anchor="w")
        self.current_stock_price_label_text = Label(self, text="Current Stock Price: ", width=30, anchor="w")
        self.debt_to_equity_ratio_label_text = Label(self, text="Debt to Equity Ratio: ", width=30, anchor="w")
        self.profit_margin_label_text = Label(self, text="Net Profit Margin: ", width=30, anchor="w")
        self.company_name_label_text = Label(self, text="", font=self.my_font, bg='grey')
        self.company_sector_label_text = Label(self,text="Sector",width=30, anchor="w")
        self.company_details_label_text = Label(self,text="",width=30, anchor="w")

        ##Binding the Enter key
        self.parent.bind('<Return>', self.analyze)

        # making new spots for values returned
        self.earningsPerShareValue = Label(self, text="", width=30, anchor="w")
        self.companySectorValue = Label(self, text="", width=30, anchor="w")
        #self.companyDetailsValue = Label(self, text="",wraplength=700,justify=CENTER)
        self.peRatioValue = Label(self, text="", width=30, anchor="w")
        self.returnOnEquityValue = Label(self, text="", width=30, anchor="w")
        self.currentStockPriceValue = Label(self, text="", width=30, anchor="w")
        self.debtToEquityRatioValue = Label(self, text="", width=30, anchor="w")
        self.profitMarginValue = Label(self, text="", width=30, anchor="w")

        self.earningsPerShareDefaultText = "Earnings Per Share: "
        self.companyNameDefaultText = ""
        self.companySectorDefaultText = "Sector:"
        self.companyDetailsDefaultText = ""
        self.peRatioDefaultText = "PE Ratio: "
        self.returnOnEquityDefaultText = "Return on Equity Ratio: "
        self.currentStockPriceDefaultText = "Current Stock Price: "
        self.debtToEquityRatioDefaultText = "Debt to Equity Ratio: "
        self.profitMarginDefaultText = "Net Profit Margin: "

        self.companySectorDefaultValue = ""
        self.companyDetailsDefaultValue = ""
        self.earningsPerShareDefaultValue = ""
        self.peRatioLabelDefaultValue = ""
        self.returnOnEquityDefaultValue = ""
        self.currentStockPriceDefaultValue = ""
        self.debtToEquityRatioDefaultValue = ""
        self.profitMarginDefaultValue = ""

        # photo addition
        self.Space = Label(self, text="", bg='grey')
        self.Space.grid(row=18, column=0)
        stockphoto = kkImage.open("MainPage.png")
        stockphoto = stockphoto.resize((225, 229), kkImage.ANTIALIAS)
        photoimg = ImageTk.PhotoImage(stockphoto)
        self.imageArea = Label(self, image=photoimg, justify=RIGHT, bg='grey')
        self.imageArea.photo = photoimg
        self.imageArea.grid(row=19, column=2)

        ## Griding Values and Text
        self.stock_symbo_text.grid(row=0, column=3)
        self.text_input_box.grid(row=0, column=4, sticky="nsew")
        self.text_input_box.bind('<Return>', self.analyze)
        self.analyze_button.grid(row=3, column=3, pady=4, sticky="nsew")
        self.clear_button.grid(row=3, column=4, ipadx=10)
        # self.graphCashFlowButton.grid(row=3, column=5, ipadx=10)
        # self.bind('<Return>', lambda event: self.analyze)

        self.company_name_label_text.grid(row=5, column=4)
        self.company_sector_label_text.grid(row=6, column=4)
        self.current_stock_price_label_text.grid(row=7, column=4)
        self.earnings_per_share_label_text.grid(row=8, column=4)
        self.pe_ratio_label_text.grid(row=9, column=4)
        self.return_on_equity_label_text.grid(row=10, column=4)
        self.debt_to_equity_ratio_label_text.grid(row=11, column=4)
        self.profit_margin_label_text.grid(row=12, column=4)
        #self.company_details_label_text.grid(row=22,column =5)

        # Fields for values
        self.companySectorValue.grid(row=6, column=5)
        self.currentStockPriceValue.grid(row=7, column=5)
        self.earningsPerShareValue.grid(row=8, column=5)
        self.peRatioValue.grid(row=9, column=5)
        self.returnOnEquityValue.grid(row=10, column=5)
        self.debtToEquityRatioValue.grid(row=11, column=5)
        self.profitMarginValue.grid(row=12, column=5)
        #self.companyDetailsValue.grid(row=22,column=5)
    def analyze(self,event=None):
        self.getCompanyName()
        self.getCompanySector()
        self.getEPS()
        self.getPERatio()
        self.getReturnOnEquity()
        self.currentStockPrice()
        self.getDebtToEquityRatio()
        self.getProfitMargin()
        #self.getCompanyDetails()
        self.clearUserInputBox()

    def getCompanyName(self):
        tickerFromUser = self.getTextInput()
        companyName = anlyze.get_stock_name(tickerFromUser)
        burn = anlyze.get_cash_burn_number(tickerFromUser) ## can remove whenever. Proof of concept for cash burn
        self.company_name_label_text["text"] = ""
        self.company_name_label_text["text"] = self.company_name_label_text["text"] + str(companyName)

    def getCompanySector(self):
        tickerFromUser = self.getTextInput()
        companySector = anlyze.get_company_sector(tickerFromUser)
        self.companySectorValue["text"] = self.companySectorDefaultValue
        self.companySectorValue["text"] = self.companySectorValue["text"] + str(companySector)

    def getCompanyDetails(self):
        tickerFromUser = self.getTextInput()
        companyDetails = anlyze.get_company_details(tickerFromUser)
        self.company_details_label_text["text"] = ""
        self.companyDetailsValue["text"] = self.companyDetailsValue["text"] + str(companyDetails)

    def getEPS(self):
        tickerFromUser = self.getTextInput()
        eps = anlyze.get_eps(tickerFromUser)
        self.earningsPerShareValue["text"] = self.earningsPerShareDefaultValue
        self.earningsPerShareValue["text"] = self.earningsPerShareValue["text"]+ '$' + str(eps)

    def getPERatio(self):
        tickerFromUser = self.getTextInput()
        peRatio = anlyze.get_pe_ratio(tickerFromUser)
        self.peRatioValue["text"] = self.peRatioLabelDefaultValue
        self.peRatioValue["text"] = self.peRatioValue["text"] + str(peRatio)

    def getReturnOnEquity(self):
        tickerFromUser = self.getTextInput()
        returnOnEquity = anlyze.get_return_on_equity(tickerFromUser)
        self.returnOnEquityValue["text"] = self.returnOnEquityDefaultValue
        self.returnOnEquityValue["text"] = self.returnOnEquityValue["text"] + str(returnOnEquity)+ '%'

    def currentStockPrice(self):
        tickerFromUser = self.getTextInput()
        stockPrice = anlyze.get_current_stock_price(tickerFromUser)
        # self.current_stock_price_label_text["text"] = self.current_stock_price_label_text["text"] +'$'+ str(stockPrice)
        self.currentStockPriceValue["text"] = self.currentStockPriceDefaultValue
        self.currentStockPriceValue["text"] = self.currentStockPriceValue["text"] + '$' + str(
            stockPrice)

    def getDebtToEquityRatio(self):
        tickerFromUser = self.getTextInput()
        debtToEquityRatio = anlyze.get_debt_to_equity(tickerFromUser)
        # self.debt_to_equity_ratio_label_text["text"] = self.debt_to_equity_ratio_label_text["text"] + str(debtToEquityRatio)
        self.debtToEquityRatioValue["text"] = self.debtToEquityRatioDefaultValue
        self.debtToEquityRatioValue["text"] = self.debtToEquityRatioValue["text"] + str(
            debtToEquityRatio)

    def getProfitMargin(self):
        tickerFromUser = self.getTextInput()
        profitMargin = anlyze.get_profit_margin(tickerFromUser)
        # self.profit_margin_label_text["text"] = self.profit_margin_label_text["text"] + str(profitMargin) +'%'
        self.profitMarginValue["text"] = self.profitMarginDefaultValue
        self.profitMarginValue["text"] = self.profitMarginValue["text"] + str(profitMargin) + '%'

    def getTextInput(self):
        result = self.text_input_box.get()
        result = result.rstrip()

        if len(result) > 0:
            results = result.upper()
            results = str(results)
            return results

        else:
            messagebox.showErrorMessage(self)

    def clearUserInputBox(self):
        self.text_input_box.delete(0, END)

    def clearValues(self):
        self.company_name_label_text["text"] = ""
        self.company_sector_label_text["text"] = self.companySectorDefaultText
        self.earnings_per_share_label_text["text"] = self.earningsPerShareDefaultText
        self.pe_ratio_label_text["text"] = self.peRatioDefaultText
        self.return_on_equity_label_text["text"] = self.returnOnEquityDefaultText
        self.current_stock_price_label_text["text"] = self.currentStockPriceDefaultText
        self.debt_to_equity_ratio_label_text["text"] = self.debtToEquityRatioDefaultText
        self.profit_margin_label_text["text"] = self.profitMarginDefaultText
        #self.companyDetailsValue["text"] = self.companyDetailsValue

        self.clearUserInputBox()
        # new method
        self.companySectorValue["text"] = self.companySectorDefaultValue
        self.earningsPerShareValue["text"] = self.earningsPerShareDefaultValue
        self.peRatioValue["text"] = self.peRatioLabelDefaultValue
        self.returnOnEquityValue["text"] = self.returnOnEquityDefaultValue
        self.currentStockPriceValue["text"] = self.currentStockPriceDefaultValue
        self.debtToEquityRatioValue["text"] = self.debtToEquityRatioDefaultValue
        self.profitMarginValue["text"] = self.profitMarginDefaultValue
        #self.companyDetailsValue["text"] = self.companyDetailsDefaultValue

