
from page_range_ns import page_range
import urllib2

#remove spacing
def normalize_space(s):
    # This should be a str method
    return ' '.join(s.split())

#fetch data
def f_data(ticker, time, n):
    resp = urllib2.urlopen('http://www.nasdaq.com/symbol/'+str(ticker)+'/time-sales?time='+str(time)+'&pageno='+str(n))
    data = resp.read()
    with open("data"+str(n)+str(time), "w") as f:
        f.write(data)
#clean data
def c_data(t, n):
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
    #clean lists
    time = [i.replace('<td>', '') for i in time]
    time = [i.replace('</td>', '') for i in time]
    time = [normalize_space(i) for i in time]
    price = [i.replace('<td>', '') for i in price]
    price = [i.replace('</td>', '') for i in price]
    price = [normalize_space(i) for i in price]
    price = [i.replace('$&nbsp;', '') for i in price]
    price = [i.replace('&nbsp;', '') for i in price]
    volume = [i.replace('<td>', '') for i in volume]
    volume = [i.replace('</td>', '') for i in volume]
    volume = [normalize_space(i) for i in volume]
    #add time price and volume to single list
    tpv = []
    for t in time:
        for p in price:
            for v in volume:
                tpv_temp = "%s %s %s" %(t, p, v)
                tpv.append(tpv_temp)
    tpv.reverse()
    return tpv
