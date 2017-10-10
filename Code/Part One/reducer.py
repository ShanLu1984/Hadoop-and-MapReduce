#!/usr/bin/python

import sys

####################### Code for Quiz: Sales per Category #####################

salesTotal = 0.0
oldKey = None

# Loop around the data
# It will be in the format key\tval
# Where key is the store name, val is the sale amount
#
# All the sales for a particular store will be presented,
# then the key will change and we'll be dealing with the next store

#for line in sys.stdin:
#    data_mapped = line.strip().split("\t")
#    if len(data_mapped) != 2:
#        # Something has gone wrong. Skip this line.
#        continue
#
#    thisKey, thisSale = data_mapped
#    
#    if oldKey and oldKey != thisKey:
#        print oldKey, "\t", salesTotal
#        salesTotal = 0
#
#    oldKey = thisKey
#    salesTotal += float(thisSale)
#
#if oldKey != None:
#    print oldKey, "\t", salesTotal
    

##############################################################################


########################## Code for Quiz: Highest Sale #######################

#salesMax = 0.0
#oldKey = None

# Loop around the data
# It will be in the format key\tval
# Where key is the store name, val is the sale amount
#
# All the sales for a particular store will be presented,
# then the key will change and we'll be dealing with the next store

#for line in sys.stdin:
#    data_mapped = line.strip().split("\t")
#    if len(data_mapped) != 2:
#        # Something has gone wrong. Skip this line.
#        continue
#
#    thisKey, thisSale = data_mapped
#    
#    if oldKey and oldKey != thisKey:
#        print oldKey, "\t", salesMax
#        salesMax = 0.0
#
#    oldKey = thisKey
#    if float(thisSale) > salesMax:
#      salesMax = float(thisSale)
#
#if oldKey != None:
#    print oldKey, "\t", salesMax



##############################################################################


    
########################### Code for Quiz: Total Sale ########################


SalesTotal = 0.0
count = 0
oldKey = None

# Loop around the data
# It will be in the format key\tval
# Where key is the store name, val is the sale amount
#
# All the sales for a particular store will be presented,
# then the key will change and we'll be dealing with the next store

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisSale = data_mapped
    
    oldKey = thisKey
    count += 1
    salesTotal += float(thisSale)

if oldKey != None:
    print "{0}\t{1}".format(count, salesTotal)
