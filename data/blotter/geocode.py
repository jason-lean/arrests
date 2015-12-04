from geopy.geocoders import GoogleV3
from geopy.exc import GeocoderTimedOut
import csv
import time

arrests = {}
f = open("arrests-cleaned.csv")

for row in csv.DictReader(f):
    incident = row["incident#"]
    defendantDOB = row["defendantDOB"]
    arrestDate = row["arrestDate"]
    arrestType = row["arrestType"]
    arrestCharges = row["arrestCharges"]


    dirtyAddress = row["arrestAddress"]
    if "-" in dirtyAddress:
        #add rule to check if surrounded. EX: K-Mart
        dirtyAddress = dirtyAddress.split("-")[1]
    marks = ["&", "@", "/"]
    for i in marks:
        if i in dirtyAddress:
            dirtyAddress = dirtyAddress.replace(i, " and ")
    cleanAddress = " ".join(dirtyAddress.split()) #This cleans up any extra whitespaces
    cleanAddress = cleanAddress.title() #And this (kinda) smarty capitalizes the address for Google
    print (cleanAddress)

    """#Actual geocoder from google
    geolocator = GoogleV3()
    location = geolocator.geocode(cleanAddress + ", Iowa City, IA", timeout=10)
    print ((location.latitude, location.longitude))

    arrests[incident] = {"incident":key, "defendantDOB":defendantDOB, "arrestAddress":arrestAddress, "arrestDate": arrestDate, "arrestType":arrestType, "arrestCharges":arrestCharges, "latitude":location.latitude, "longitude":location.longitude}
    time.sleep(10)

with open("arrests-geocoded.csv", "wb") as outfile:
    attrNames = ["incident", "defendantDOB", "arrestAddress", "arrestDate", "arrestType", "arrestCharges", "latitude", "longitude"]
    writer = csv.DictWriter(outfile, fieldnames = attrNames)

    writer.writeheader()
    for row in arrests:
        writer.writerow(arrests[row])
"""