#!/usr/bin/python
import sys

#strRaw=raw_input("Enter a list of numbers:\n")
strRaw="4,2,6,4,7,5,99,1,3"
print "You entered {0}.".format(strRaw)

intList=[int(i) for i in strRaw.split(",")]

if len(intList) == 1:
  print "Can't sort a single element array."
  sys.exit(1)

i=0
j=i+1

def swap(l,r):
  intList[i]=r
  intList[j]=l

if intList[i] < intList[j]:
  pass
else:
 # Swap these
  swap(intList[i], intList[j])  
  
print intList

