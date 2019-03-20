import argparse
import os
import sys
from alpha_vantage.timeseries import TimeSeries

# PVTL, CLGX, GOOG, AMZN, NFLX, APPL, IBM, GE, CAT, AA, FB, YHOO, HPE

parser = argparse.ArgumentParser(description="Generate various flavors of stock data")
parser.add_argument('-s', '--symbol', nargs='+', help="stock symbol", required=True) 
parser.add_argument('-i', '--interval', help="stock data interval", required=True) #intraday, weekly, weekly adjusted, monthly, monthly adjusted, batch stock
args = parser.parse_args()

symbol = args.symbol
interval = args.interval

ts = TimeSeries(key=os.environ['AV_API_KEY'], output_format='csv')

# data, _ = ts.get_intraday(
#    symbol=sys.argv[1], interval='5min', outputsize='full') #outputsize='compact' -- what's the diff? # intraday # daily #daily adjusted

# data, _ = ts.get_weekly(symbol=sys.argv[1]) # get_weekly_adjusted
# data, _ = ts.get_weekly_adjusted(symbol=sys.argv[1]) # get_weekly_adjusted
# data, _ = ts.get_monthly(symbol=sys.argv[1]) # get_monthly_adjusted
# data, _ = ts.get_monthly_adjusted(symbol=sys.argv[1]) # get_monthly_adjusted

if interval == 'get_batch_stock_quotes':
    #data, _ = ts.get_batch_stock_quotes(symbols=['PVTL', 'CLGX', 'GOOG', 'AMZN', 'NFLX',
    #                                         'APPL', 'IBM', 'GE', 'CAT', 'AA', 'FB', 'YHOO', 'HPE'])
    data, _ = ts.get_batch_stock_quotes(symbols=symbol)

# for everything except ts.get_batch_stock_quotes
# for i, v in enumerate(data):
#     if i == 0:
#         s = 'symbol'
#         v.insert(0, s)
#         v = ",".join(v)
#         print(v)
#     elif i > 0:
#         symbol = '"{}"'.format(sys.argv[1])
#         v[0] = '"{}"'.format(v[0])
#         v.insert(0, symbol)
#         v = ",".join(v)
#         print(v)

    for i, v in enumerate(data):
        print(i, v)
