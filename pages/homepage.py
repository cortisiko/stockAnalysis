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
        self.text_input_box = Entry(self, relief=RIDGE, width=10, borderwidth=4)
        self.analyze_button = Button(self,
                                     text='Analyze Stock', relief=RAISED, borderwidth=7, bg='green',
                                     command=self.analyze)
        self.clear_button = Button(self, text="Clear", relief=RIDGE, command=self.clear_values)
        self.text_input_box.focus()
        self.clear_button = Button(self, text="Clear", relief=RIDGE, command=self.clear_values, bg='red')
        # self.graphCashFlowButton = Button(self, text="See Cash Flow Graph",command=lambda: controller.show_frame(PlotCashFlowChart))

        self.earnings_per_share_label_text = Label(self, text="Earnings Per Share: ", width=30, anchor="w")
        self.pe_ratio_label_text = Label(self, text="PE Ratio: ", width=30, anchor="w")
        self.return_on_equity_label_text = Label(self, text="Return on Equity Ratio: ", width=30, anchor="w")
        self.current_stock_price_label_text = Label(self, text="Current Stock Price: ", width=30, anchor="w")
        self.debt_to_equity_ratio_label_text = Label(self, text="Debt to Equity Ratio: ", width=30, anchor="w")
        self.profit_margin_label_text = Label(self, text="Net Profit Margin: ", width=30, anchor="w")
        self.company_name_label_text = Label(self, text="", font=self.my_font, bg='grey')
        self.company_sector_label_text = Label(self, text="Sector", width=30, anchor="w")
        self.company_details_label_text = Label(self, text="", width=30, anchor="w")

        # Binding the Enter key
        self.parent.bind('<Return>', self.analyze)

        # making new spots for values returned
        self.earnings_per_share_value = Label(self, text="", width=30, anchor="w")
        self.company_sector_value = Label(self, text="", width=30, anchor="w")
        # self.companyDetailsValue = Label(self, text="",wraplength=700,justify=CENTER)
        self.pe_ratio_value = Label(self, text="", width=30, anchor="w")
        self.return_on_equity_value = Label(self, text="", width=30, anchor="w")
        self.current_stock_price_value = Label(self, text="", width=30, anchor="w")
        self.debt_to_equity_ratio_value = Label(self, text="", width=30, anchor="w")
        self.profit_margin_value = Label(self, text="", width=30, anchor="w")

        self.earnings_per_share_default_text = "Earnings Per Share: "
        self.company_name_default_text = ""
        self.company_sector_default_text = "Sector:"
        self.company_details_default_text = ""
        self.pe_ratio_default_text = "PE Ratio: "
        self.return_on_equity_default_text = "Return on Equity Ratio: "
        self.current_stock_price_default_text = "Current Stock Price: "
        self.debt_to_equity_ratio_default_text = "Debt to Equity Ratio: "
        self.profit_margin_default_text = "Net Profit Margin: "

        self.company_sector_default_value = ""
        self.company_details_default_value = ""
        self.earnings_per_share_default_value = ""
        self.pe_ratio_label_default_value = ""
        self.return_on_equity_default_value = ""
        self.current_stock_price_default_value = ""
        self.debt_to_equity_ratio_default_value = ""
        self.profit_margin_default_alue = ""

        # photo addition
        self.space = Label(self, text="", bg='grey')
        self.space.grid(row=18, column=0)
        stock_photo = kkImage.open("MainPage.png")
        stock_photo = stock_photo.resize((225, 229), kkImage.ANTIALIAS)
        photo_img = ImageTk.PhotoImage(stock_photo)
        self.image_area = Label(self, image=photo_img, justify=RIGHT, bg='grey')
        self.image_area.photo = photo_img
        self.image_area.grid(row=19, column=2)

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
        # self.company_details_label_text.grid(row=22,column =5)

        # Fields for values
        self.company_sector_value.grid(row=6, column=5)
        self.current_stock_price_value.grid(row=7, column=5)
        self.earnings_per_share_value.grid(row=8, column=5)
        self.pe_ratio_value.grid(row=9, column=5)
        self.return_on_equity_value.grid(row=10, column=5)
        self.debt_to_equity_ratio_value.grid(row=11, column=5)
        self.profit_margin_value.grid(row=12, column=5)
        # self.companyDetailsValue.grid(row=22,column=5)

    def analyze(self, event=None):
        self.getCompanyName()
        self.getCompanySector()
        self.getEPS()
        self.getPERatio()
        self.getReturnOnEquity()
        self.currentStockPrice()
        self.getDebtToEquityRatio()
        self.getProfitMargin()
        # self.getCompanyDetails()
        self.clear_user_input_box()

    def getCompanyName(self):
        tickerFromUser = self.get_text_input()
        companyName = anlyze.get_stock_name(tickerFromUser)
        burn = anlyze.get_cash_burn_number(tickerFromUser)  ## can remove whenever. Proof of concept for cash burn
        self.company_name_label_text["text"] = ""
        self.company_name_label_text["text"] = self.company_name_label_text["text"] + str(companyName)

    def getCompanySector(self):
        tickerFromUser = self.get_text_input()
        companySector = anlyze.get_company_sector(tickerFromUser)
        self.company_sector_value["text"] = self.company_sector_default_value
        self.company_sector_value["text"] = self.company_sector_value["text"] + str(companySector)

    def getCompanyDetails(self):
        tickerFromUser = self.get_text_input()
        companyDetails = anlyze.get_company_details(tickerFromUser)
        self.company_details_label_text["text"] = ""
        self.companyDetailsValue["text"] = self.companyDetailsValue["text"] + str(companyDetails)

    def getEPS(self):
        tickerFromUser = self.get_text_input()
        eps = anlyze.get_eps(tickerFromUser)
        self.earnings_per_share_value["text"] = self.earnings_per_share_default_value
        self.earnings_per_share_value["text"] = self.earnings_per_share_value["text"] + '$' + str(eps)

    def getPERatio(self):
        tickerFromUser = self.get_text_input()
        peRatio = anlyze.get_pe_ratio(tickerFromUser)
        self.pe_ratio_value["text"] = self.pe_ratio_label_default_value
        self.pe_ratio_value["text"] = self.pe_ratio_value["text"] + str(peRatio)

    def getReturnOnEquity(self):
        tickerFromUser = self.get_text_input()
        returnOnEquity = anlyze.get_return_on_equity(tickerFromUser)
        self.return_on_equity_value["text"] = self.return_on_equity_default_value
        self.return_on_equity_value["text"] = self.return_on_equity_value["text"] + str(returnOnEquity) + '%'

    def currentStockPrice(self):
        tickerFromUser = self.get_text_input()
        stockPrice = anlyze.get_current_stock_price(tickerFromUser)
        # self.current_stock_price_label_text["text"] = self.current_stock_price_label_text["text"] +'$'+ str(stockPrice)
        self.current_stock_price_value["text"] = self.current_stock_price_default_value
        self.current_stock_price_value["text"] = self.current_stock_price_value["text"] + '$' + str(
            stockPrice)

    def getDebtToEquityRatio(self):
        tickerFromUser = self.get_text_input()
        debtToEquityRatio = anlyze.get_debt_to_equity(tickerFromUser)
        # self.debt_to_equity_ratio_label_text["text"] = self.debt_to_equity_ratio_label_text["text"] + str(debtToEquityRatio)
        self.debt_to_equity_ratio_value["text"] = self.debt_to_equity_ratio_default_value
        self.debt_to_equity_ratio_value["text"] = self.debt_to_equity_ratio_value["text"] + str(
            debtToEquityRatio)

    def getProfitMargin(self):
        tickerFromUser = self.get_text_input()
        profitMargin = anlyze.get_profit_margin(tickerFromUser)
        # self.profit_margin_label_text["text"] = self.profit_margin_label_text["text"] + str(profitMargin) +'%'
        self.profit_margin_value["text"] = self.profit_margin_default_alue
        self.profit_margin_value["text"] = self.profit_margin_value["text"] + str(profitMargin) + '%'

    def get_text_input(self):
        result = self.text_input_box.get()
        result = result.rstrip()

        if len(result) > 0:
            results = result.upper()
            results = str(results)
            return results

        else:
            messagebox.showErrorMessage(self)

    def clear_user_input_box(self):
        self.text_input_box.delete(0, END)

    def clear_values(self):
        self.company_name_label_text["text"] = ""
        self.company_sector_label_text["text"] = self.company_sector_default_text
        self.earnings_per_share_label_text["text"] = self.earnings_per_share_default_text
        self.pe_ratio_label_text["text"] = self.pe_ratio_default_text
        self.return_on_equity_label_text["text"] = self.return_on_equity_default_text
        self.current_stock_price_label_text["text"] = self.current_stock_price_default_text
        self.debt_to_equity_ratio_label_text["text"] = self.debt_to_equity_ratio_default_text
        self.profit_margin_label_text["text"] = self.profit_margin_default_text
        # self.companyDetailsValue["text"] = self.companyDetailsValue

        self.clear_user_input_box()
        # new method
        self.company_sector_value["text"] = self.company_sector_default_value
        self.earnings_per_share_value["text"] = self.earnings_per_share_default_value
        self.pe_ratio_value["text"] = self.pe_ratio_label_default_value
        self.return_on_equity_value["text"] = self.return_on_equity_default_value
        self.current_stock_price_value["text"] = self.current_stock_price_default_value
        self.debt_to_equity_ratio_value["text"] = self.debt_to_equity_ratio_default_value
        self.profit_margin_value["text"] = self.profit_margin_default_alue
        # self.companyDetailsValue["text"] = self.company_details_default_value
