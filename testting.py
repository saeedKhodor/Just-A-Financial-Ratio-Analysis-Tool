import streamlit as st
import yfinance as yf
import pandas as pd    

stock = yf.Ticker('AAPL')
financials = stock.financials
balance_sheet = stock.balance_sheet
cash_flow = stock.cashflow

print(balance_sheet.index)


#['Treasury Shares Number', 'Ordinary Shares Number', 'Share Issued', 'Net Debt', 'Total Debt', 'Tangible Book Value', 'Invested Capital', 'Working Capital', 'Net Tangible Assets', 'Capital Lease Obligations', 'Common Stock Equity', 'Total Capitalization', 'Total Equity Gross Minority Interest', 'Stockholders Equity', 'Gains Losses Not Affecting Retained Earnings', 'Other Equity Adjustments', 'Retained Earnings', 'Capital Stock', 'Common Stock', 'Total Liabilities Net Minority Interest', 'Total Non Current Liabilities Net Minority Interest', 'Other Non Current Liabilities', 'Tradeand Other Payables Non Current', 'Long Term Debt And Capital Lease Obligation', 'Long Term Capital Lease Obligation', 'Long Term Debt', 'Current Liabilities', 'Other Current Liabilities', 'Current Deferred Liabilities', 'Current Deferred Revenue', 'Current Debt And Capital Lease Obligation', 'Current Capital Lease Obligation', 'Current Debt', 'Other Current Borrowings', 'Commercial Paper', 'Payables And Accrued Expenses', 'Payables', 'Total Tax Payable', 'Income Tax Payable', 'Accounts Payable', 'Total Assets', 'Total Non Current Assets', 'Other Non Current Assets', 'Non Current Deferred Assets', 'Non Current Deferred Taxes Assets', 'Investments And Advances', 'Other Investments', 'Investmentin Financial Assets', 'Available For Sale Securities', 'Net PPE', 'Accumulated Depreciation', 'Gross PPE', 'Leases', 'Other Properties', 'Machinery Furniture Equipment', 'Land And Improvements', 'Properties', 'Current Assets', 'Other Current Assets', ...]