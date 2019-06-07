#!/usr/bin/python3

import csv
import collections
import pspEntries

entries = pspEntries.getEntries()
f = open('types.csv', 'w')

with f:
    fnames = ['ID', 'Name', 'ProposedName', 'Comment']
    writer = csv.DictWriter(f, fnames)
    writer.writeheader()
    
    ordered = collections.OrderedDict(sorted(entries.items()))
    for key, value in ordered.items():
        id = "{0:#0{1}x}".format(key,5)
        name = value['Name']
        pname = value['PName']
        comment = value['Comment']
        writer.writerow({'ID': id, 'Name' : name, 'ProposedName' : pname, 'Comment': comment})
