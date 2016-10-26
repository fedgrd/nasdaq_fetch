"""
Fetch last sale data from Nasdaq.
Author: Federico Giordani
"""
#import urllib2 to import stock data
import urllib2

#def function to find largest number in string
def findLargestNumber(text):
    ls = list()
    for w in text.split():
        try:
            ls.append(int(w))
        except:
            pass
    try:
        return max(ls)
    except:
        return None

#find page range function || reads only text
def page_range(ticker):

#read initial page range
    response = urllib2.urlopen('http://www.nasdaq.com/symbol/'+ str(ticker) + '/time-sales?time=1')
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
    print page_r

tick = str(raw_input('Please specify stock ticker (lowercase): '))
page_range(tick)
