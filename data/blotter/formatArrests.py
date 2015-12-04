import csv

#Init the dict, and define the read file
arrests = {}
f = open("arrests.csv")

for row in csv.DictReader(f):
    
    #Use incident number as the key, it's unique. 
    key = row.pop("*Incident #*")
    if key == "*Incident #*":
        continue

    dates = row.pop("*Offense Date*\nDate of Birth")
    defendantDOB = dates.split("\n")[1].split(": ")[1]
    arrestDate = dates.split("*")[1]

    arrestType = row.pop("*C/A*")
    arrestAddress = row.pop("Arrest Location")
    arrestCharges = row.pop("*Charge(s)*")
    #Comment out because splitting leades to a list of charges within the csv when writing
    #arrestCharges = arrestCharges.split("\n")

    arrests[key] = {"incident#":key, "defendantDOB":defendantDOB, "arrestAddress":arrestAddress, "arrestDate": arrestDate, "arrestType":arrestType, "arrestCharges":arrestCharges}
    print (arrests[key])

with open("arrests-cleaned.csv", "wb") as outfile:
    attrNames = ["incident#", "defendantDOB", "arrestAddress", "arrestDate", "arrestType", "arrestCharges"]
    writer = csv.DictWriter(outfile, fieldnames = attrNames)

    writer.writeheader()
    for row in arrests:
        writer.writerow(arrests[row])