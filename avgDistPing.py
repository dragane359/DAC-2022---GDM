import csv
import math
from math import atan2, radians, cos, sin, asin, sqrt

def read_csv(csvfilename):
    rows = []
    with open(csvfilename) as csvfile:
        file_reader = csv.reader(csvfile)
        for row in file_reader:
            rows.append(row)
    return rows


def find_distances(fname, route):
    data = read_csv(fname)[1:]
    data = list(filter(lambda row: row[1] == route, data))
    data.sort(key = lambda x: x[3])
    print(len(data))
    dists = []
    for i in range(len(data) - 1):
        R = 6373.0
        lat1 = radians(float(data[i][4]))
        lon1 = radians(float(data[i][5]))
        lat2 = radians(float(data[i+1][4]))
        lon2 = radians(float(data[i+1][5]))

        dlon = lon2 - lon1
        dlat = lat2 - lat1

        a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))

        d = R * c
        dists += [d,]
    return dists

def trj_unique(fname):
    data = read_csv(fname)[1:]
    names = []
    for i in data:
        if i[1] not in names:
            names.append(i[1])
    return names

def average_pings(fname):
    data = read_csv(fname)[1:]
    averages = {}
    count = 0
    for i in trj_unique(fname):
        count += 1;
        if count != 30:
            x = find_distances(fname, i)
            averages[i] = sum(x)/len(x)
        if count == 30:
            break;
    return averages

