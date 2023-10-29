import yfinance as yf

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

# command to look at all available outputs
# print(ticker.keys())
