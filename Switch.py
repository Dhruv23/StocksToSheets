import StockFunctions
print("Welcome to the Stock Market Tool. \n\n")
print("Option 1: Enter Tickers and the data will be outputted into the terminal, and a txt file. \n")
print("Option 2: Enter Tickers and the data will be outputted into the terminal, and a Google Sheet. \n")
print("Option 3: Pre defined tickers are added to a google sheet. \n")
print("Option 4: Pre defined tickers are emailed to users. \n")
print("Option 5: Pre defined tickers are sent in a discord server by a bot. \n")
option = input("Pick an option (1-5)\n")
try: 
    option = int(option)
    if(option != "1" and option != 2 and option != 3 and option != 4 and option != 5): 
        print("Invalid option, try again \n ")
        exit()
except ValueError as ve: 
        print(f'You entered {option}, which is not a number.')


if(option == 1): 
    StockFunctions.toTxt()
    exit()
if(option == 2): 
    StockFunctions.toGoogleSheets()
    exit()
if(option == 3):
    StockFunctions.toSheetOnce()
    exit()
if(option == 4): 
    StockFunctions.toEmail()
    exit()
if(option == 5): 
    StockFunctions.toDiscord()
    exit()
else: 
    print("Invalid Input, Try again \n")
    exit()