import matplotlib.pyplot as plt
import numpy as np
import urllib
import matplotlib.dates

def graph_data(stock):
    stock_price_url = 'https://pythonprogramming.net/yahoo_finance_replacement'
    source_code = urllib.request.urlopen(stock_price_url).read().decode()

    stock_data = []
