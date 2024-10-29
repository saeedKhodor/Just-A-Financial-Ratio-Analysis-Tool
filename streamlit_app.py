import streamlit as st
import yfinance as yf
import pandas as pd

# Page Title
st.title("Financial Ratio Analysis Tool")

# Ticker Input
ticker = st.text_input("Enter Stock Ticker (e.g., AAPL)", "AAPL")

# Fetch Data Button
if st.button("Analyze Ratios"):
    # Download data
    stock = yf.Ticker(ticker)
    financials = stock.financials
    balance_sheet = stock.balance_sheet
    cash_flow = stock.cashflow

    # Display fetched data (optional)
    st.subheader("Financial Statements")
    st.write("Income Statement", financials)
    st.write("Balance Sheet", balance_sheet)
    st.write("Cash Flow Statement", cash_flow)

    # Calculate Ratios
    try:
        # Profitability Ratios
        gross_margin = financials.loc["Gross Profit"][0] / financials.loc["Total Revenue"][0]
        net_profit_margin = financials.loc["Net Income"][0] / financials.loc["Total Revenue"][0]
        return_on_assets = financials.loc["Net Income"][0] / balance_sheet.loc["Total Assets"][0]

        # Liquidity Ratios
        current_ratio = balance_sheet.loc["Current Assets"][0] / balance_sheet.loc["Current Liabilities"][0]
        quick_ratio = (balance_sheet.loc["Current Assets"][0] - balance_sheet.loc["Inventory"][0]) / balance_sheet.loc["Current Liabilities"][0]

        # Leverage Ratios
        debt_to_equity = balance_sheet.loc["Total Liab"][0] / balance_sheet.loc["Stockholder Equity"][0]
        interest_coverage = financials.loc["EBIT"][0] / financials.loc["Interest Expense"][0]

        # Efficiency Ratios
        inventory_turnover = financials.loc["Cost Of Revenue"][0] / balance_sheet.loc["Inventory"][0]
        asset_turnover = financials.loc["Total Revenue"][0] / balance_sheet.loc["Total Assets"][0]

        # Display Ratios
        st.subheader("Profitability Ratios")
        st.write(f"Gross Margin: {gross_margin:.2%}")
        st.write(f"Net Profit Margin: {net_profit_margin:.2%}")
        st.write(f"Return on Assets: {return_on_assets:.2%}")

        st.subheader("Liquidity Ratios")
        st.write(f"Current Ratio: {current_ratio:.2f}")
        st.write(f"Quick Ratio: {quick_ratio:.2f}")

        st.subheader("Leverage Ratios")
        st.write(f"Debt to Equity Ratio: {debt_to_equity:.2f}")
        st.write(f"Interest Coverage Ratio: {interest_coverage:.2f}")

        st.subheader("Efficiency Ratios")
        st.write(f"Inventory Turnover: {inventory_turnover:.2f}")
        st.write(f"Asset Turnover: {asset_turnover:.2f}")

    except Exception as e:
        st.write("Error in calculating ratios:", e)
