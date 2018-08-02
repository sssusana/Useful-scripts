import csv, sys
import requests
import urllib2
import os
import datetime
from time import strftime


filename = 'raw_data_urls.csv'
with open(filename, 'rb') as f:
    reader = csv.reader(f)
    try:
        for row in reader:
            if 'http' in row[0]:
                print row
                rev  = row[0][::-1]
                i  = rev.index('/')
                tmp = rev[0:i]
                print strftime("%H:%M:%S"), "The file:", tmp[::-1], "is being downloaded.........."
                rq = urllib2.Request(row[0])
                res = urllib2.urlopen(rq)
                if not os.path.exists("./"+tmp[::-1]):
                    pdf = open("./" + tmp[::-1], 'wb')
                    pdf.write(res.read())
                    pdf.close()
                    print strftime("%H:%M:%S"), "SUCCESS! The file:", tmp[::-1], "download is completed"
                    print "\n"
                else:
                    print strftime("%H:%M:%S"), "ERROR! The file: ", tmp[::-1], "already exists, won't be downloaded"
                    print "\n"
    except csv.Error as e:
        sys.exit('file %s, line %d: %s' % (filename, reader.line_num, e))
