import pandas as pd
import numpy as np
import matplotlib as mpl
from matplotlib import pyplot
from indexes import ColumnKey

filePath = './Statistics.xlsx'

ColumnKey.insert(3, [])
excel = pd.read_excel('./Statistics.xlsx')
excel = np.asarray(excel)
excel = np.delete(excel, [15, 16, 158], axis=0)

keys = [0, 4, 5]

for v in excel:
    for i in range(0, len(keys)):
        v[keys[i]] = ColumnKey[keys[i]].index(str(v[keys[i]]))

print(excel)

lookup = [
    [4],
    ['M', 'F'],
    ['NEW', 'nan'],
    [26],
    [53]
]

key = [0, 3, 4]
for i in range(0, len(key)):
    for j in range(1, lookup[key[i]][0] + 1):
        lookup[key[i]].append(j)
    lookup[key[i]][0] = 0

print(lookup)

categories = [
    np.delete(excel, [1, 2, 3, 4, 5], axis=1),
    np.delete(excel, [0, 1, 3, 4, 5], axis=1),
    np.delete(excel, [0, 2, 3, 4, 5], axis=1),
    np.delete(excel, [0, 1, 2, 3, 5], axis=1),
    np.delete(excel, [0, 1, 2, 3, 4], axis=1),
]

for i in range(0, len(categories[2])):
    categories[2][i][0] = str(categories[2][i][0])

new = [
    np.zeros(5),
    np.zeros(2),
    np.zeros(2),
    np.zeros(27),
    np.zeros(54),
]

for i in range(0, len(lookup)):
    for j in range(0, len(categories[i])):
        for k in range(0, len(lookup[i])):
            if categories[i][j][0] == lookup[i][k]:
                new[i][k] = int(new[i][k]  + 1)

chartinfo = [
    {
        'size': (11, 8),
        'labels': ['Male Students', 'Female Students'],
        'data': new[1],
        'type': 'barh',
        'title': 'Amount of Students Based on Gender',
    },
    {
        'size': (4, 4),
        'labels': ['New students', 'Old students'],
        'data': new[2],
        'type': 'pie',
        'title': 'Percentage of New Students',
    },
    {
        'size': (6, 5),
        'labels': ColumnKey[0],
        'data': new[0],
        'type': 'pie',
        'title': 'Which Leaning Style Students Use',
    },
    {
        'size': (10, 7),
        'labels': ColumnKey[4],
        'data': new[3],
        'type': 'barh',
        'title': 'Which Cities Students Reside In',
    }
]

for i in range(0, len(chartinfo)):
    pyplot.figure(figsize=chartinfo[i]['size'])
    pyplot.title(chartinfo[i]['title'])
    if chartinfo[i]['type'] == 'pie':
        pyplot.pie(chartinfo[i]['data'], labels=chartinfo[i]['labels'])
    else:
        pyplot.barh(chartinfo[i]['labels'], chartinfo[i]['data'])
    pyplot.show()
