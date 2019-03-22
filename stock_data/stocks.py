import argparse
import os
import sys
from alpha_vantage.timeseries import TimeSeries

# PVTL CLGX, GOOG AMZN NFLX APPL IBM GE CAT AA FB YHOO HPE

parser = argparse.ArgumentParser(description="Generate various flavors of stock data")
parser.add_argument('-s', '--symbol', nargs='+', help="stock symbol", required=True) 
parser.add_argument('-t', '--type', choices=['batch', 'intraday', 'weekly', 'weekly_adjusted',
                                            'monthly', 'monthly_adjusted'], help="stock data type", required=True)
args = parser.parse_args()

symbol = args.symbol
stock_type = args.type

ts = TimeSeries(key=os.environ['AV_API_KEY'], output_format='csv')

def batch(symbol):
    data, _ = ts.get_batch_stock_quotes(symbols=symbol)

    for v in (data):
        print(v)

def intraday(symbol):
    data, _ = ts.get_intraday(
    symbol=symbol, interval='1min', outputsize='compact') #outputsize='compact' and full 

    for i, v in enumerate(data):
        if i == 0:
            s = 'symbol'
            v.insert(0, s)
            v = ",".join(v)
            print(v)
        elif i > 0:
            s = ''.join(symbol) 
            symbol = '{}'.format(s)
            v[0] = '"{}"'.format(v[0])
            v[0] = '{}'.format(v[0])
            v.insert(0, symbol)
            v = ",".join(v)
            print(v)

def weekly(symbol):
    data, _ = ts.get_weekly(symbol=symbol) 

    for i, v in enumerate(data):
        if i == 0:
            s = 'symbol'
            v.insert(0, s)
            v = ",".join(v)
            print(v)
        elif i > 0:
            s = ''.join(symbol) 
            symbol = '{}'.format(s)
            v[0] = '"{}"'.format(v[0])
            v[0] = '{}'.format(v[0])
            v.insert(0, symbol)
            v = ",".join(v)
            print(v)

def weekly_adjusted(symbol):
    data, _ = ts.get_weekly_adjusted(symbol=symbol) 

    for i, v in enumerate(data):
        if i == 0:
            s = 'symbol'
            v.insert(0, s)
            v = ",".join(v)
            print(v)
        elif i > 0:
            s = ''.join(symbol) 
            symbol = '{}'.format(s)
            v[0] = '"{}"'.format(v[0])
            v[0] = '{}'.format(v[0])
            v.insert(0, symbol)
            v = ",".join(v)
            print(v)

def monthly(symbol):
    data, _ = ts.get_monthly(symbol=symbol) 

    for i, v in enumerate(data):
        if i == 0:
            s = 'symbol'
            v.insert(0, s)
            v = ",".join(v)
            print(v)
        elif i > 0:
            s = ''.join(symbol) 
            symbol = '{}'.format(s)
            v[0] = '"{}"'.format(v[0])
            v[0] = '{}'.format(v[0])
            v.insert(0, symbol)
            v = ",".join(v)
            print(v)

def monthly_adjusted(symbol):
    data, _ = ts.get_monthly_adjusted(symbol=symbol) 

    for i, v in enumerate(data):
        if i == 0:
            s = 'symbol'
            v.insert(0, s)
            v = ",".join(v)
            print(v)
        elif i > 0:
            s = ''.join(symbol) 
            symbol = '{}'.format(s)
            v[0] = '"{}"'.format(v[0])
            v[0] = '{}'.format(v[0])
            v.insert(0, symbol)
            v = ",".join(v)
            print(v)

if __name__ == "__main__":
    if stock_type == 'batch':
        batch(symbol)
    elif stock_type == 'intraday':
        intraday(symbol)
    elif stock_type == 'weekly':
        weekly(symbol)
    elif stock_type == 'weekly_adjusted':
        weekly_adjusted(symbol)
    elif stock_type == 'monthly':
        monthly(symbol)
    elif stock_type == 'monthly_adjusted':
        monthly_adjusted(symbol)