from urllib import request
import xml.etree.ElementTree as Et


BUS_URL = "http://ctabustracker.com/bustime/map/getBusesForRoute.jsp?route=22"
route22file = "rt22.xml"


def main():
    u = request.urlopen(BUS_URL)
    data = u.read()
    f = open(route22file, 'wb+')
    f.write(data)
    f.flush()
    f.close()

    tree = Et.parse("rt22.xml")
    root = tree.getroot()
    children = (child for child in root if child.tag == 'bus')
    for child in children:
        print(child)


if __name__ == "__main__":
    main()
