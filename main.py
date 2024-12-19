import time
import os
from stock import Stocks
from yahoo_fin import stock_info
import yfinance as yf
import warnings
warnings.filterwarnings("ignore")

portfolio = []

def addStock(name, ticker, sector, numOfShares):
    price = round(float(stock_info.get_live_price(ticker)),2)
    newStock = Stocks(name,ticker,sector,price,numOfShares)
    portfolio.append(newStock)

def updatePrice():
    for stock in portfolio:
        price = stock_info.get_live_price(stock.ticker)
        stock.currentPrice = round(float(price),2)
            
def viewPortfolio():
    print("{0:20s}{1:10s}{2:35s}{3:15s}{4:14s}{5:10s}".format("Name of Stock", "Ticker", "Industry", "Price", "QTY", "GAIN/LOSS"))
    count = 1
    for stock in portfolio:
        updatePrice()
        gain = round((stock.originalPrice - stock.currentPrice)* numOfShares, 2)
        print(f"{count}. {stock.name:{17}}{stock.ticker:{10}}{stock.sector:{35}}${stock.currentPrice:{8}}{stock.numOfShares:{8}}               ${gain:{1}}")
        count += 1

def search_by_sector():
    sector_portfolio = []
    user_industry = input("What sector are you looking for: ").lower()
    for stock in portfolio:
        if stock.sector.lower() == user_industry:
            sector_portfolio.append(stock)
    print("{0:20s}{1:10s}{2:35s}{3:15s}{4:14s}{5:10s}".format("Name of Stock", "Ticker", "Industry", "Price", "QTY", "GAIN/LOSS"))
    sector_count = 1
    for stock in sector_portfolio:
        gain = round((stock.originalPrice - stock.currentPrice)* numOfShares, 2)
        print(f"{sector_count}. {stock.name:{17}}{stock.ticker:{10}}{stock.sector:{35}}${stock.currentPrice:{8}}{stock.numOfShares:{8}}               ${gain:{1}}")
        sector_count += 1
    sector_portfolio = []
    input("\nPRESS ENTER TO CONTINUE ")

def mainMenu():
    start_menu = """
    ____________________________________
    |            MAIN MENU             |
    |                                  |
    |1. Add a new stock to portfolio   |
    |2. Update stock price             |
    |3. Search by sector               |
    |4. View portfolio                 |
    |5. Exit program                   |
    |                                  |
    |__________________________________|
    """
    print(start_menu)
    print("")
    choice = input()
    time.sleep(0.5)
    os.system('clear')
    return choice

print("WELCOME TO MY STOCK PORTFOLIO")

status = True

while status:
    os.system('clear')
    choice = mainMenu()
    if choice == '1':
        name = input("Enter the name of the stock: ")
        ticker = input("Enter the stock ticker name: ")
        tick = yf.Ticker(ticker).info
        sector = tick['industry']
        numOfShares = int(input("Enter the numer of stock shares to buy: "))
        addStock(name, ticker, sector, numOfShares)
    elif choice == "2":
        updatePrice()
        viewPortfolio()
    elif choice == '3':
        search_by_sector()
    elif choice == '4':
        viewPortfolio()
        input("\nPRESS ENTER TO CONTINUE ")
    elif choice == '5':
        status = False
        print("Thanks for using my stock portfolio. GOODBYE!")
        os.system('clear')
    else:
        print("\nINVALID OPTION")
        input("PRESS ENTER TO CONTINUE ")
    os.system('clear')
