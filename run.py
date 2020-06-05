from bs4 import BeautifulSoup
import math
import csv

userInput = input("Enter file path: ")

source = open(userInput, "r")

soup = BeautifulSoup(source.read(), "lxml")

# placemarks to CSV file


def flagsToCSV():
    placemarks = []
    for placemark in soup.find_all("placemark"):
        placemarkList = []
        placemarkList.append(str(placemark.find("name").string))
        placemarkList.append(str(placemark.lookat.longitude.string))
        placemarkList.append(str(placemark.lookat.latitude.string))
        placemarks.append(placemarkList)
    with open(userInput + '_output.csv', 'w', newline='') as csvfile:
        write = csv.writer(csvfile, delimiter=',',
                           quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for place in placemarks:
            write.writerow(place)


flagsToCSV()


# transect caluctions that ended up not being used for now
def parseCoordinates():
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

    # get the length of the interval
    interval = float(input("Enter Transect Interval (meters): "))
    interval = interval / 111139

    distance = (interval * 10) / 2

    # print coordinates
    for point in points:
        print(point)
