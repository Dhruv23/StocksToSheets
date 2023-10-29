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
import smtplib
import datetime as dt
import discord


def toTxt(): 
    # Get user input for ticker symbol
    with open('data.txt', 'w') as f:
        f.write("\n")
    exitCase = "n"
    count = 0
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
        print(f"The current info for the stock {ticker} is: \n")
        print(f"Price: {price}\nTrailing PE: {trailingPE}\nForward PE: {forwardPE}\nHigh over one year: {oneYearHigh}\nLow over one year: {oneYearlow}\nOne Year Change: {oneYearChange}\n\n")
        dataset = [f"price: {price}", f"Trailing PE: {trailingPE}", f"Forward PE: {forwardPE}", f"One Year Change: {oneYearChange}", f"One Year Low: {oneYearlow}",f"One Year High: {oneYearHigh} \n"]
        with open('data.txt', 'a') as f:
            f.write(f"Data for ticker {ticker}: \n")
            for data in dataset:
                f.write(str(data))
                f.write('\n')
        continueInput = input("Type 'n' to exit, or anything else to continue: ")
        if(continueInput == 'n'):
            break
def toGoogleSheets():
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
def toSheetOnce(): 
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
def toEmail():

    with open('data.txt', 'w') as f:
        f.write("\n")

    with open('data.csv', 'w') as f:
        f.write("\n")
        f.write("ticker, price, trailingPE, forwardPE, oneYearChange, oneYearLow, oneYearHigh \n")
    tickerlist = ["GOOGL", "GOOG", "AMZN", "AAPL", "COST", "IBM", "MSFT", "MRNA", "PFE", "KO", "NKE", "AMD", "TSLA"]
    for ticker in tickerlist:
        tickerF = yf.Ticker(f'{ticker}').info
        price = '%.3f'%tickerF['currentPrice']
        trailingPE = '%.3f'%tickerF['trailingPE']
        forwardPE = '%.3f'%tickerF['forwardPE']
        oneYearChange = '%.3f'%tickerF['52WeekChange']
        oneYearHigh = '%.3f'%tickerF['fiftyTwoWeekHigh']
        oneYearlow = '%.3f'%tickerF['fiftyTwoWeekLow']
        dataset = [f"ticker: {ticker}", f"price: {price}", f"Trailing PE: {trailingPE}", f"Forward PE: {forwardPE}", f"One Year Change: {oneYearChange}", f"One Year Low: {oneYearlow}",f"One Year High: {oneYearHigh}"]
        with open('data.txt', 'a') as f:
            f.write(f"Data for ticker {ticker}: \n")
            for data in dataset:
                if data == dataset[6]: 
                    f.write(str(data))
                    f.write('\n')
                    f.write('\n')
                else: 
                    f.write(str(data))
                    f.write('\n')

        with open('data.csv', 'a') as f:
            for data in dataset:
                if(data == dataset[6]): 
                    f.write(str(data))
                    f.write('\n')
                else: 
                    f.write(str(data))
                    f.write(',')

        df = pandas.read_csv('data.csv')
        # print(df)

    my_email = "adhrinclips4@gmail.com"
    password = "fzfluixxechixsfx"

    # A list of who you want to send the email to
    to_emails = ["dipesh.ifpatel@gmail.com", "nirupa.d.patel@gmail.com", "bunciedp@gmail.com", "dhruvdp.2004@gmail.com"]

    now = dt.datetime.now()
    year = now.year
    month = now.month
    day_of_week = now.weekday()
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    day = days_of_week[day_of_week]
    print(day)


    messageF = df.to_html
    subject = f"Happy {day}!"
    message = f"{messageF}"
    with open("data.txt", "r") as f: 
        output = f.read()
    print(f"{output}")
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=to_emails,
            msg=f"Subject: {subject}\n\n Dear Fam, \n\n Attached is the daily stock info updates: \n {output}")       
