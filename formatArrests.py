import csv

arrests = {}

f = open("arrests.csv")
for row in csv.DictReader(f):
    key = row.pop("*Incident #*")
    
    if key in arrests:
        #duplicate handling
        pass

    arrestAddress = row.pop("Arrest Location")
    arrestDate = row.pop("*Offense Date*\nDate of Birth")
    arrestDate = arrestDate.split("*")[1]
    arrestCharges = row.pop("*Charge(s)*")
    #Comment out because splitting leades to a list of charges within the csv when writing
    #arrestCharges = arrestCharges.split("\n")

    arrests[key] = {"address":arrestAddress, "date":arrestDate, "charges":arrestCharges}
print (arrests)
