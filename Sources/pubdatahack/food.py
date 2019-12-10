from matplotlib import pyplot as plt
import csv

URL = "https://data.cityofchicago.org/Health-Human-Services/Food-Inspections/4ijn-s7e5"
f = open("Food_Inspections.csv")
food_data = csv.DictReader(f)
Risk = {}
for row in food_data:
    Risk.setdefault(row['Risk'], 0)
    Risk[row['Risk']] += 1

Risk['None'] = Risk.pop('')
labels = tuple(Risk)
sizes = [Risk[risk] for risk in Risk]
fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()
