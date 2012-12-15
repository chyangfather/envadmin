#!/usr/bin/python
#-*-coding:utf-8-*-
import  codecs
from xml.dom import minidom

__author__ = 'holbrook'


#try:
file = '/Users/holbrook/Documents/svnroot/dev/JGXT/src/trunk/JGXT/机构客户/cxGYWXTDYKHS_MX.xml'
f = codecs.open(file)
f.readline()
str = f.read().decode('gb2312')
f.close()
str = str.encode('utf-8')
      #print str
            #s = cStringIO.StringIO()
            #s.write(str)
            #s.seek(0)
   # xmlfile.encoding
xmldoc = minidom.parseString(str)
#except :
    #updatelogger.error( "Can't parse Xml File." )
#    sys.exit(0)

root = xmldoc.documentElement
print root.nodeName
print root.attributes['name'].value
describeNode = root.childNodes[1]
print describeNode.nodeName
print describeNode.firstChild.nodeValue

