import yfinance as yf
import csv
import pandas
import os
import glob
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import json
import oauth2client 
import time 
scopes = [
'https://www.googleapis.com/auth/spreadsheets',
'https://www.googleapis.com/auth/drive'
]

credentials = ServiceAccountCredentials.from_json_keyfile_name("PtoG.json", scopes) #access the json key you downloaded earlier 
file = gspread.authorize(credentials) # authenticate the JSON key with gspread
sheet = file.open("OutputSheet") #open sheet
# sheet = sheet.OutputSheet #replace sheet_name with the name that corresponds to yours, e.g, it can be sheet1
# Get user input for ticker symbol
count = 2
temp = count
while(temp < 15):
    sheet.values_update(
        f'Sheet1!A{temp}:G{temp+1}',
        params={
            'valueInputOption': 'USER_ENTERED'
        },
        body={
            'values': [["", "", "", "", "", "", ""]]
        }
    )
    temp = temp + 1
tickerlist = ["GOOGL", "GOOG", "AMZN", "AAPL", "COST", "IBM", "MSFT", "MRNA", "PFE", "KO", "NKE", "AMD", "TSLA"]
for ticker in tickerlist:
    tickerF = yf.Ticker(f'{ticker}').info
    price = tickerF['currentPrice']
    trailingPE = tickerF['trailingPE']
    forwardPE = tickerF['forwardPE']
    oneYearChange = tickerF['52WeekChange']
    oneYearHigh = tickerF['fiftyTwoWeekHigh']
    oneYearlow = tickerF['fiftyTwoWeekLow']
    dataset = [ticker, price, trailingPE, forwardPE, oneYearChange, oneYearlow, oneYearHigh]
    sheet.values_update(
        f'Sheet1!A{count}:G{count+1}',
        params={
            'valueInputOption': 'USER_ENTERED'
        },
        body={
            'values': [[ticker, price, trailingPE, forwardPE, oneYearChange, oneYearlow, oneYearHigh]]
        }
    )
    count = count+1
print("Updated, Starting timer. \n")
