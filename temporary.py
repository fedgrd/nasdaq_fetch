"""
Fetch data from Nasdaq for stock.
Author: Federico
"""
#import urllib2 to import Nasdaq data
import urllib2
nasdaq_w_list = []
#define the range of pages to search in
for n in range(2, 3):
    nasdaq_w_list.append('http://www.nasdaq.com/symbol/goog/time-sales?time=1&pageno='+str(n))
    for i in nasdaq_w_list:
        response = urllib2.urlopen(str(i))
        html = response.read()
        with open('page'+str(n)+'.txt', 'w') as f:
            f.write(html)
print nasdaq_w_list
#clean up data and keep only time, price, volume

for m in range(1, 2):
    alpha = []
    searchfile = open('page'+str(m)+'.txt', 'r')
    for line in searchfile:
            if '<td>' in line:
                alpha.append(line)
print alpha
