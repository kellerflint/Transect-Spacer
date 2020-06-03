from bs4 import BeautifulSoup
import math


source = open("sampleData2.kml", "r")

soup = BeautifulSoup(source.read(), "lxml")

coordinateString = str(
    soup.find("linestring").coordinates.find_all(text=True, recursive=False))

coordinateString = coordinateString.replace('\\', '')
coordinateString = coordinateString.replace('t', '')
coordinateString = coordinateString.replace('n', '')
coordinateString = coordinateString.replace('[', '')
coordinateString = coordinateString.replace(']', '')
coordinateString = coordinateString.replace('\'', '')

cordsList = coordinateString.split(" ")

cordsList.pop()

points = []

for point in cordsList:
    points.append(point.split(","))

for i in range(len(points) - 1):
    x1 = float(points[i][0])
    x2 = float(points[i+1][0])
    y1 = float(points[i][1])
    y2 = float(points[i+1][1])

    length = math.sqrt(math.pow((x2 - x1), 2) + math.pow(y2 - y1, 2))

    points[i].append(length)
points[len(points) - 1].append(0)

lineDistance = 0
for point in points:
    lineDistance += point[3]

# get the length of the interval
interval = float(input("Enter Transect Interval (meters): "))
interval = interval / 111139


# print coordinates
for point in points:
    print(point)
