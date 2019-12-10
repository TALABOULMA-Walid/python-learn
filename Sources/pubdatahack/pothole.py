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
            Streets[street_address] += 1  # float(potholes)
            if Streets[street_address] > max_potholes:
                max_potholes = Streets[street_address]
                worst_street = street_address
        except ValueError:
            pass

print(worst_street, max_potholes)

# worst 10 streets
street_list = []
for key, value in Streets.items():
    street_list.append((key, value))
street_list.sort(key=lambda x: x[1])  # or sorted(street_list, ...)
for st in street_list[-1:-10:-1]:
    print(st)

# interesting:
# sorted(street_list[800:810], key=lambda x:(random.randint(1,10),x[1]), reverse=True)
