import yfinance as yf 
import datetime

print('yfinance version is ' + yf.__version__)


def yfinancetut(tickersymbol):
    if type(tickersymbol) not in [str]:
        raise TypeError("The stock symbol must be a string of characters")

    if len(tickersymbol) > 5:
        raise ValueError("The stock symbol must be 3 characters or less")
    tickerdata = yf.Ticker(tickersymbol)
    tickerinfo = tickerdata.info
    #gets company name
    investment = tickerinfo['shortName']
    print('Investment ' + investment)
    
    #gets the date for today
    today = datetime.datetime.today().isoformat()

    #gets the history of the stock depending on the start and end params for the date
    tickerDF = tickerdata.history(period = '1d', start = '2020-1-1', end = today[:10])

    #gets the most recent price of the stock 
    priceLast = tickerDF['Close'].iloc[-1]

    #gets the price from the day before
    priceYest = tickerDF['Close'].iloc[-2]

    change = priceLast - priceYest

    #print(investment + ' price last = ' + str(priceLast))

    #print("price change = " + str(change))

    #prints the whole table of price values for the stock
    #print(tickerDF)

    print(tickersymbol)
    print(priceLast)



yfinancetut('GSAT')
