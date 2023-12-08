#!/usr/bin/env python
# @author geeksforgeeks.com
# part of the code edited by self
# importing csv module
import csv
import sys
 
# csv file name
filename = sys.argv[1]
 
# initializing the titles and rows list
# fields = []
# rows = []
name = sys.argv[2]
 
# reading csv file
with open(filename) as csvfile:
    # creating a csv reader object
    csvreader = csv.reader(csvfile)
     
    # extracting field names through first row
    fields = next(csvreader)
 
    # extracting each data row one by one
 
    for row in csvreader:
        for i in range(len(row)):
            if(name == row[i].strip().upper()):
                print(row[0])

                match(i):
                    case 1:
                        print("Monday\n")
                    case 2:
                        print("Tuesday\n")
                    case 3:
                        print("Wednesday\n")
                    case 4:
                        print("Thursday\n")
                    case 5:
                        print("Friday\n")
                    case 6:
                        print("Saturday\n")
                    case 7:
                        print("Sunday\n")
                    case _:
                        print("Go HOME!!\n")