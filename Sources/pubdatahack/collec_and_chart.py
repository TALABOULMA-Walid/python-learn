from collections import Counter
from matplotlib import pyplot as plt

sentence = "yes but no but yes"
words = sentence.split()
word_counts = Counter(words)
print(word_counts['yes'])
print(word_counts.most_common())
# Pie Chart
labels = ('Frogs', 'Hogs', 'Dogs', 'Logs')
sizes = [15, 30, 45, 10]
explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')
fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()

