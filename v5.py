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