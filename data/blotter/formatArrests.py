import csv

#Init the dict, and define the read file
arrests = {}
f = open("arrests.csv")

for row in csv.DictReader(f):
    
    #Use incident number as the key, it's unique. 
    key = row.pop("*Incident #*")
    if key == "*Incident #*":
        continue

    arrestAddress = row.pop("Arrest Location")

    dates = row.pop("*Offense Date*\nDate of Birth")
    perpDOB = dates.split("\n")[1].split(": ")[1]
    arrestDate = dates.split("*")[1]
    arrestCharges = row.pop("*Charge(s)*")
    arrestC = row.pop("*C/A*")
    #Comment out because splitting leades to a list of charges within the csv when writing
    #arrestCharges = arrestCharges.split("\n")

    print (perpDOB)

    arrests[key] = {"incident#":key, "address":arrestAddress, "date":arrestDate, "charges":arrestCharges}

with open("arrests-cleaned.csv", "wb") as outfile:
    attrNames = ["incident#", "address", "date", "charges"]

    writer = csv.DictWriter(outfile, fieldnames = attrNames)

    writer.writeheader()
    for row in arrests:
        writer.writerow(arrests[row])
