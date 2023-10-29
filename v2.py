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


scopes = [
'https://www.googleapis.com/auth/spreadsheets',
'https://www.googleapis.com/auth/drive'
]

credentials = ServiceAccountCredentials.from_json_keyfile_name("PtoG.json", scopes) #access the json key you downloaded earlier 
file = gspread.authorize(credentials) # authenticate the JSON key with gspread
sheet = file.open("OutputSheet") #open sheet
# sheet = sheet.OutputSheet #replace sheet_name with the name that corresponds to yours, e.g, it can be sheet1
# Get user input for ticker symbol

with open('data.csv', 'w') as f:
    f.write("\n")
    f.write("ticker, price, trailingPE, forwardPE, oneYearChange, oneYearLow, oneYearHigh \n")
exitCase = "n"
count = 2
temp = count
while(temp <10):
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

print("Welcome to the Stock Market Tool. \n This script allows you to view and save data such as price, PE, and One Year Highs and lows of a stock \n")
continueInput = input("Would you like to enter the Stock Market tool? (y/n) ")
while(continueInput != exitCase):
    ticker = input("Enter the ticker symbol: ").upper()
    tickerF = yf.Ticker(f'{ticker}').info
    price = tickerF['currentPrice']
    trailingPE = tickerF['trailingPE']
    forwardPE = tickerF['forwardPE']
    oneYearChange = tickerF['52WeekChange']*100
    oneYearHigh = tickerF['fiftyTwoWeekHigh']
    oneYearlow = tickerF['fiftyTwoWeekLow']
    dataset = [ticker, price, trailingPE, forwardPE, oneYearChange, oneYearlow, oneYearHigh]
    with open('data.csv', 'a') as f:
        for data in dataset:
            if(data == dataset[6]): 
                f.write(str(data))
                f.write('\n')
            else: 
                f.write(str(data))
                f.write(',')

    df = pandas.read_csv('data.csv')
    print(df)
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
    continueInput = input("Type 'n' to exit, or anything else to continue: ")
    if(continueInput == 'n'):
        break
# command to look at all available outputs
# print(ticker.keys())
