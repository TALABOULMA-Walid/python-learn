from geopy.distance import geodesic
from urllib import request
import xml.etree.ElementTree as Et
import time
import webbrowser
import pathlib


MAPS_URL = "https://www.google.com/maps/search/?api=1&query={latitude},{longitude}"
MAPS_URL_DIR = "https://www.google.com/maps/dir/?api=1" \
               "&origin={david_lat},{david_long}" \
               "&destination={bus_lat},{bus_long}" \
               "&travelmode=walking"


def load_bus_route():
    import os
    bus_url = "http://ctabustracker.com/bustime/map/getBusesForRoute.jsp?route=22"
    script_directory = pathlib.Path(__file__).parent
    route22_path = script_directory.joinpath("rt22.xml")
    file_empty = (os.stat(str(route22_path)).st_size == 0)
    now_time = time.time()
    file_time = route22_path.stat().st_mtime
    if (now_time - file_time > 5) or file_empty:
        data = request.urlopen(bus_url).read().decode("UTF-8")
        route22_file = route22_path.open("w+")
        route22_file.write(data)
        route22_file.close()


def route_xml():
    load_bus_route()
    string_xml = open("rt22.xml", "r").read()
    xml_tree = Et.fromstring(string_xml)
    return xml_tree


def main():
    david_coordinate = (41.979471, -87.668254)
    bus_lat, bus_long = 0, 0
    bus_coordinate = (bus_lat, bus_long)
    while 1:
        route_tree = route_xml()
        for child in route_tree.findall('bus'):
            if child.find('dd').text == 'Northbound':
                bus_lat = float(child.find('lat').text)
                bus_long = float(child.find('lon').text)
                bus_coordinate = (bus_lat, bus_long)
            if geodesic(bus_coordinate, david_coordinate).meters < 400:
                display_url = MAPS_URL_DIR.format(david_lat=david_coordinate[0],
                                                  david_long=david_coordinate[1],
                                                  bus_lat=bus_lat,
                                                  bus_long=bus_long)
                webbrowser.open_new_tab(display_url)
                return True
        time.sleep(10)


if __name__ == "__main__":
    main()
