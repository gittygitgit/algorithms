#!/usr/bin/python

strRaw=raw_input("Enter a list of numbers:\n")

print "You entered {0}.".format(strRaw)

# list comprehension
inPlace=[int(i) for i in strRaw.split(",")]


def countInversions(l):
  numInversions=0
  i=0
  while i < len(l):
    # for each item in the list compare with items to the right

    curVal=l[i]
    print curVal

    j=i+1
    while j < len(l):

      if curVal > l[j]:  
        numInversions += 1

      j+=1
    i+=1
  return numInversions  

numInversions = countInversions(inPlace)
print "There are {0} inversions.".format(numInversions)
