import matplotlib.pyplot as plt
import numpy as np
import urllib
import matplotlib.dates

def graph_data(stock):
    stock_price_url = 'https://pythonprogramming.net/yahoo_finance_replacement'
    source_code = urllib.request.urlopen(stock_price_url).read().decode()

    stock_data = []

    split_source = source_code.split('\n')

    for(line in split_source):
        split_line = line.split(',')
        if(len(split_line) == 6):
            if('values' not in line):
                stock_data.append(line)

    date, closep, highp, lowp, openp, volume = np.loadtxt(stock_data,
                                                          delimiter=',',
                                                          unpack=True,
                                                          # %Y = full year 2018
                                                          # %y = partial year 18
                                                          # %m = number of month
                                                          # %d = number of days
                                                          # %H = hours
                                                          # %M = minutes
                                                          # %S = seconds
                                                          converters={0: bytespdate2num('')})

    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('stock grph')
    plt.legend()

    plt.show()

graph_data('TSLA')
