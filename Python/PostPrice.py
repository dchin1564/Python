###Code used to place a stock onto dynamoDB table 
###only functions for one stock and I wasn't sure how to fix that with this version of code

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
    