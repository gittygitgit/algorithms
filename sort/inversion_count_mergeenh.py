#!/usr/bin/python
import math

with open("entries.txt") as f:
  entries=f.readlines()

print len(entries)

# list comprehension
inPlace=[int(i) for i in entries]

numInversions=0

def countInversions(l, r):
  global numInversions
  for i in l:
    for j in r:
      if i > j:
        numInversions += 1
      


def merge(l,r):
  #print "Merging [l=" + str(l) + ", r=" + str(r) + "]"
  merged=[]

  while len(l) > 0 and len(r) > 0:

    if l[0] <= r[0]:
      merged.append(l.pop(0))
    else:
      merged.append(r.pop(0))

  while len(l) > 0:
    merged.append(l.pop(0))

  while len(r) > 0:
    merged.append(r.pop(0))

  return merged

def sort(arr):
  # keep dividing until each subarray contains only a single el

  # An array of length 1 is sorted
  if len(arr) == 1:
    return arr

  # divide
  l=len(arr)
  mid=int(math.floor(l / 2))

  arrl=arr[0:mid]
  arrr=arr[mid:l]

  sortedl=sort(arrl)
  sortedr=sort(arrr)

  countInversions(sortedl, sortedr)
  return merge(sortedl,sortedr)

sorted=sort(inPlace)
print numInversions
