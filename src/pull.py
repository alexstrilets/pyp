#!/usr/bin/env python
import urllib2
import time
import datetime
import os.path


stocksToPull = "AAPL", "GOOG"

def getLastPullDate(stock):
    return 0

def pullData(stock):
    print "Pulling stock " + stock
    print str(datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'))
    urlToPull = 'http://chartapi.finance.yahoo.com/instrument/1.0/'+stock+'/chartdata;type=quote;range=1y/csv'
    saveFileName = stock+'.txt'
    saveFile=open(saveFileName, 'a')
    htmlPage=urllib2.urlopen(urlToPull).read()
    splitHtml=htmlPage.split('\n')
    lastDateOnFile=getLastPullDate(stock)

    for eachLine in splitHtml:
        if 'values' not in eachLine:
            splitLine=eachLine.split(',')
            if len(splitLine) == 6:
                if int(splitLine[0]) > lastDateOnFile:
                    lineToWrite=eachLine+'\n'
                    saveFile.write(lineToWrite)
    saveFile.close()
    print "Pulled stock " + stock
    time.sleep(1)

for stock in stocksToPull:
    pullData(stock)


