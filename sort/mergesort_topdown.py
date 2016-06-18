#!/usr/bin/python

import math

strRaw=raw_input("Enter a list of numbers:\n")

print "You entered {0}.".format(strRaw)

# list comprehension
inPlace=[int(i) for i in strRaw.split(",")]

def merge(l,r):
  print "Merging [l=" + str(l) + ", r=" + str(r) + "]"
  merged=[]

  while len(l) > 0 and len(r) > 0:
      
    if l[0] <= r[0]:
      merged.append(l.pop(0))
      print merged
    else:
      merged.append(r.pop(0))
      print merged

  while len(l) > 0:
    merged.append(l.pop(0))

  while len(r) > 0:
    merged.append(r.pop(0))

  print "Merged: " + str(merged)
  return merged


def sort(arr):
  # keep dividing until each subarray contains only a single el

  print "Sorting [arr=" + str(arr) + "]"  
  # An array of length 1 is sorted
  if len(arr) == 1:
    return arr

  # divide
  l=len(arr)
  mid=int(math.floor(l / 2))

  arrl=arr[0:mid]
  arrr=arr[mid:l]

  print arrl
  print arrr
  sortedl=sort(arrl)
  sortedr=sort(arrr)

  return merge(sortedl,sortedr)


sorted = sort(inPlace)
print sorted
