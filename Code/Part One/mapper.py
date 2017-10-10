#!/usr/bin/python

# Format of each line is:
# date\ttime\tstore name\titem description\tcost\tmethod of payment
#
# We want elements 2 (store name) and 4 (cost)
# We need to write them out to standard output, separated by a tab
import sys

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) == 6:
       date, time, store, item, cost, payment = data 
       # mapper code for Quiz: Sales per Category
       #print "{0}\t{1}".format(item, cost)
       
       # mapper code for Quiz: Highest Sale 
       #print "{0}\t{1}".format(store, cost)

       # mapper code for Quiz: Total Sale
       print "{0}\t{1}".format(store, cost)
