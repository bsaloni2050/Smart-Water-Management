import matplotlib.pyplot as plt
import numpy as np
import xlrd
import urllib
import matplotlib.dates as mdates


def graph_data(stock)

    price_url ='http://chartapi.finance.yahoo.com/instrument/1.0/'+stock+'/chartdata;type=quote;range=1m/csv'
    Source_code = urllib.request.urlopen
    plt.plot([1, 3, 4, 8 ], [1, 3, 4 , 9], label ='line')

    plt.xlabel('TIme Series')
    plt.ylabel('Raw BioCon Values')
    plt.title('Raw Data in Time Series')
    plt.legend()
    plt.show()

