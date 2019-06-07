#!python3

# importing csv module
import csv
import os
from pathlib import PurePath, Path

# csv file nam
p = PurePath(__file__)
filename = os.path.join(p.parent, "types.csv")


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
