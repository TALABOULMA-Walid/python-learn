from urllib import request
import xml.etree.ElementTree as ET
import sys
import os

urlbus="http://ctabustracker.com/bustime/map/getBusesForRoute.jsp?route=22"
route22file="rt22.xml"

def main():
    u = request.urlopen(urlbus)
    data = u.read()
    f = open(route22file,'wb+')
    f.write(data)
    f.flush()
    f.close()

    tree = ET.parse("rt22.xml")
    root = tree.getroot()
    childs = (child for child in root if child.tag == 'bus')
    for child in childs:
        print(child)


if __name__ == "__main__":
    main()
