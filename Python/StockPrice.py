#This code originally used for posting to a table, but I could not run it on AWS Lambda 
#which is PostPrice.py is made to post to a table 
#This code is used to get the last price of a stock given any stock symbol 
#errors in AWS lambda showed that I did not have a numpy dependency even though I uploaded a zip folder with numpy 
#StockPrice_test.py is the unittest for this file
import json
import boto3
import datetime as dt 
import pandas_datareader.data as web 


def getPrice(tickerSymbol):
    #checks the input that is given to getPrice function
    if type(tickerSymbol) not in [str]:
        raise TypeError("The stock symbol must be a string of characters")

    if len(tickerSymbol) > 5 or len(tickerSymbol) < 3:
        raise ValueError("The stock symbol must be 3 characters or less")
    
    start = dt.datetime(2021,1,25)
    end = dt.datetime(2021,1,27)

    df = web.DataReader(tickerSymbol,'yahoo',start,end)
    #returns last row of data from dataframe 
    dr = df.tail(1)

    return [tickerSymbol,dr.loc['2021-01-27','Close']]



"""
def lambda_handler(event, context):
    # TODO implement
    
    information = getPrice('GSAT')
    name = information[0]
    price = information[1]
    
    table.put_item(
        Item = {
            'StockSymbol': name,
            'StockPrice': price
        }
    )
    
    response = {
        'message' :'Item added'
    }
    return {
        'statusCode': 200,
        'body': response
    }

"""




###Code used to place a stock onto dynamoDB table 
###only functions for one stock and I wasn't sure how to fix that with this version of code
'''
from urllib.request import urlopen
from contextlib import closing
import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('StockPrice')
 
def lambda_handler(event, context):
    with closing(urlopen("https://financialmodelingprep.com/api/v3/quote-short/AAPL?apikey=demo")) as responseData:
        jsonData = responseData.read()
        object = json.loads(jsonData)
        price = int(object[0]['price'])
        symbol = object[0]['symbol']
        table.put_item(
        Item = {
            'StockSymbol': symbol,
            'StockPrice': price
        }
    )
    
    response = {
        'message' :'Item added'
    }
    return {
        'statusCode': 200,
        'body': response
    }
'''    
    

