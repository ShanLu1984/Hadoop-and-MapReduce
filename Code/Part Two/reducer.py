#!/usr/bin/python

import sys

########################## Code for Quiz: Hits to Page #########################

 #########################
#hitCount = 0
#oldKey = None
#
#for line in sys.stdin:
#   data_mapped = line.strip().split("\t")
#   if len(data_mapped) != 1:
#      # there is something wrong, continue
#      continue
#   
#   thisKey = data_mapped
#
#   if oldKey and oldKey != thisKey:
#      print oldKey, "\t", hitCount
#      hitCount = 0
#   
#   oldKey = thisKey
#   hitCount += 1
#
#if oldKey != None:
#   oldKey, "\t", hitCount


########################## Code for Quiz: Hits from IP #########################

# the same as Quiz: Hits to Page


########################## Code for Quiz: Most Popular #########################
hitCount = 0
maxHit = 0
oldKey = None
maxKey = None

for line in sys.stdin:
   data_mapped = line.strip().split("\t")
   if len(data_mapped) != 1:
      # there is something wrong, continue
      continue
   
   thisKey = data_mapped

   if oldKey and oldKey != thisKey:
      if hitCount > maxHit:
         maxHit = hitCount
         maxKey = oldKey
      hitCount = 0
   
   oldKey = thisKey
   hitCount += 1

if oldKey != None and hitCount > maxHit:
   maxHit = hitCount
   maxKey = oldKey
print maxKey, "\t", maxHit
