from geopy.geocoders import GoogleV3
from geopy.exc import GeocoderTimedOut
import csv
import time

arrests = {}
f = open("arrests-cleaned.csv")

for row in csv.DictReader(f):
    
    #Clean up the address a little
    dirtyAddress = row["address"]
    cleanAddress = dirtyAddress.replace("/", " & ")
    
    incident = row["incident#"]
    date = row["date"]
    charges = row["charges"]

    #Actual geocoder from google
    geolocator = GoogleV3()
    location = geolocator.geocode(cleanAddress + ", Iowa City, IA", timeout=10)

    print ((location.latitude, location.longitude))
    arrests[incident] = {"incident":incident, "address":location, "date":date, "charges":charges, "latitude":location.latitude, "longitude":location.longitude}
    time.sleep(1)

with open("arrests-geocoded.csv", "wb") as outfile:
    attrNames = ["incident", "address", "date", "charges", "latitude", "longitude"]

    writer = csv.DictWriter(outfile, fieldnames = attrNames)

    writer.writeheader()
    for row in arrests:
        writer.writerow(arrests[row])
