#!python3

# importing csv module 
import csv 
  
# csv file name 
filename = "types.csv"


f = open(filename, 'r')

DIRECTORY_ENTRY_TYPES = {}

with f:
    
    reader = csv.DictReader(f)
    
    for row in reader:
        id = row['ID']
        name = row['Name']
        pName = row['ProposedName']
        comment = row['Comment']
        DIRECTORY_ENTRY_TYPES[int(id, 0)] = {}
        DIRECTORY_ENTRY_TYPES[int(id, 0)]['Name'] = name
        DIRECTORY_ENTRY_TYPES[int(id, 0)]['PName'] = pName
        DIRECTORY_ENTRY_TYPES[int(id, 0)]['Comment'] = comment
