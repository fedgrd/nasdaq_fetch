
from largest_number import findLargestNumber
#import urllib2 to import stock data
import urllib2

#find page range function || reads only text
def page_range(ticker, time):

#read initial page range
    response = urllib2.urlopen('http://www.nasdaq.com/symbol/'+ str(ticker) + '/time-sales?time='+str(time))
    page = response.read()
    with open("page_test.txt", "w") as f:
        f.write(page)

#searchfile for number of pages in current timeframe
    searchfile = open("page_test.txt", "r")
    clean_line = ""
    for line in searchfile:
        if "quotes_content_left_lb_FirstPage" in line:
            clean_line += line
    clean_line = clean_line.replace('<', ' ')
    clean_line = clean_line.replace('>', ' ')

#call largest number function on open text file
    page_r = findLargestNumber(clean_line)
    return page_r
    
