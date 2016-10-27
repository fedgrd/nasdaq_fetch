"""
Fetch last sale data from Nasdaq.
Author: Federico Giordani page_range(tick, tm)
"""

from page_range_ns import page_range
from fetch_data import f_data
from fetch_data import c_data
#prompt user for ticker choice
tick = str(raw_input('Please specify stock ticker: ').lower())


#fetch data, saves it in file
output = []
for t in range(1,14):
    for n in reversed(range(1, page_range(tick, t)+1)):
        f_data(tick, t, n)
        for i in c_data(t, n):
            output.append(i)
with open("output.txt", "w") as f:
   for i in output:
        f.write("%s\n" % i)
