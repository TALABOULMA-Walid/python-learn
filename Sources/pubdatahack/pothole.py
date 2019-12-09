import csv
import re

Streets = {}
max_potholes = 0
with open("potholes.csv") as f:
    for row in csv.DictReader(f):
        potholes = row['NUMBER OF POTHOLES FILLED ON BLOCK']
        street_address = re.split('^[0-9]* ', row['STREET ADDRESS'])[-1]
        Streets.setdefault(street_address, 0)
        try:
            Streets[street_address] += float(potholes)
            if Streets[street_address] > max_potholes:
                max_potholes = Streets[street_address]
                worst_street = street_address
        except ValueError:
            pass

print(worst_street, max_potholes)
