#!/usr/bin/env python
import urllib2
import time
import datetime
import os.path


stocksToPull = "AAPL","GOOG",'MSFT','CMG','AMZN','EBAY','TSLA'

def getLastPullDate(fname):
    if not os.path.isfile(fname):
        return 0
    else:
        fPtr=open(fname, 'r')
        existingData=fPtr.read().split('\n')
        lastLine = existingData[-2]
        fPtr.close()
        return int(lastLine.split(',')[0])

def pullData(stock):
    print "-------- Pulling stock " + stock
    print str(datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'))
    urlToPull = 'http://chartapi.finance.yahoo.com/instrument/1.0/'+stock+'/chartdata;type=quote;range=1y/csv'
    saveFileName = stock+'.txt'
    lastDateOnFile=getLastPullDate(saveFileName)
    saveFile=open(saveFileName, 'a')
    htmlPage=urllib2.urlopen(urlToPull).read()
    splitHtml=htmlPage.split('\n')

    for eachLine in splitHtml:
        if 'values' not in eachLine:
            splitLine=eachLine.split(',')
            if len(splitLine) == 6:
                if int(splitLine[0]) > lastDateOnFile:
                    lineToWrite=eachLine+'\n'
                    saveFile.write(lineToWrite)
    saveFile.close()
    print "------- Done ------- "
    time.sleep(1)

for stock in stocksToPull:
    pullData(stock)


