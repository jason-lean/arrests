from geopy.geocoders import GoogleV3
from geopy.exc import GeocoderTimedOut
import csv
import time

arrests = {}
f = open("arrests-cleaned.csv")

for row in csv.DictReader(f):
    incident = row["incident"]
    defendantDOB = row["defendantDOB"]
    arrestDate = row["arrestDate"]
    arrestType = row["arrestType"]
    arrestCharges = row["arrestCharges"]

    #Clean up the address a little
    dirtyAddress = row["arrestAddress"]
    cleanAddress = dirtyAddress.replace("/", " & ")
    #Actual geocoder from google
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
