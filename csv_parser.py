# importing csv module
import csv

# csv file name
filename = "schedule.csv"

# initializing the titles and rows list
weekly= {}
fields = []
rows = []
day = []

# reading csv file
with open(filename, 'r') as csvfile:
    # creating a csv reader object
    csvreader = csv.reader(csvfile)

    # fields = next(csvreader)[1:]
    
    for row in csvreader:
        rows.append(row)
for i in range(1,8):
    for row in rows:
        day.append(row[i])

    date= day.pop(0)
    d= dict(s1= day.pop(0), s2= day.pop(0), s3= day.pop(0))
    weekly[date] = d

print(weekly)