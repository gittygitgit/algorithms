#!/usr/bin/python

'''
This algorithm is simple and Big-O of n-squared.
'''
with open("entries.txt") as f:
  entries=f.readlines()

print len(entries)

# list comprehension
inPlace=[int(i) for i in entries]


def countInversions(l):
  numInversions=0
  i=0
  while i < len(l):
    # for each item in the list compare with items to the right

    curVal=l[i]

    j=i+1
    print "" + str(i) + "|" + str(numInversions)
    while j < len(l):

      if curVal > l[j]:  
        numInversions += 1

      j+=1
    i+=1
  return numInversions  

numInversions = countInversions(inPlace)
print "There are {0} inversions.".format(numInversions)
