
from page_range_ns import page_range
import urllib2

#clean data
def fetch_data(ticker, time, n):
    resp = urllib2.urlopen('http://www.nasdaq.com/symbol/'+str(ticker)+'/time-sales?time='+str(time)+'&pageno='+str(n))
    data = resp.read()
    with open("data"+str(n)+str(time), "w") as f:
        f.write(data)

def clean_data(t, n):
    time = []
    price = []
    volume = []
    searchfile = open("data"+str(n)+str(t), "r")
    for line in searchfile:
        if "<td>" in line and "</td>" in line and "<tr>" not in line:
            if ";" in line:
                price.append(line)
            elif ":" in line:
                time.append(line)
            else:
                volume.append(line)
    searchfile.close
    
fetch_data('goog', 1, 1)
clean_data(1, 1)
