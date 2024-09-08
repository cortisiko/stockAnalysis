
# Stock Analysis 📈

The **Stock Analysis** application is a Python-based tool that leverages the `yahooquery` package to fetch real-time stock data. The frontend is built using `Tkinter`, allowing users to analyze financial ratios and view visual representations of key financial statement line items through bar and trend charts.

### Purpose
This application provides users with ratio analysis and visualize data from financial statements in a user-friendly manner. The ratios focused on in this application includes: PE, Return on Equity and Debt to equity ratios. Furthermore, the Profit margin, EPS are also displayed. 
The application helps you visualize the financial health of a company by displaying charts in the following areas:
- Free Cash Flow (from the Cash Flow statement)
- Cash to Earnings (from the Cash Flow statement)
- Long Term Debt (from the Balance Sheet)
- Net Income (from the Income Statement)
- Total Revenue

Additionally, it provides a trend analysis comparing Cash from Operations and Net Income, supporting [cash-based earnings quality analysis](https://www.investopedia.com/terms/q/qualityofearnings.asp).

**Note:** This application does not constitute investment advice or recommendations for any particular stock or investment strategy.

---

## Demo

When a user enters a stock symbol, multiple [financial ratios](https://www.investopedia.com/financial-ratios-4689817) are displayed:
![StockAnalysisHomePage](assets/home-page.png)

The bar graphs show:
- **Free Cash Flow** (from the Cash Flow statement)
- **Cash to Earnings** (from the Cash Flow statement)
- **Long Term Debt** (from the Balance Sheet)
- **Net Income** (from the Income Statement)
- **Total Revenue**

Each graph allows the user to toggle between quarterly and yearly views for better comparison.
![Charts](assets/cash-flow.png)

---

## Installation and Usage

### Prerequisites
- Python 3.x
- `pipenv` for package management

### Installation Steps
1. Install `pipenv` if you don't already have it:
   ```bash
   pip install pipenv
   ```

2. Install the required dependencies:
   ```bash
   pipenv sync
   ```
   If you're in a development environment, use:
   ```bash
   pipenv sync --dev
   ```

3. Run the application:
   ```bash
   python userInterface.py
   ```

### Optional
If `Tkinter` is not installed on your machine, you can install it by running:
```bash
sudo apt-get install python3-tk
```

---
