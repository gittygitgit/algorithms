#!/usr/bin/python
import sys

strRaw=raw_input("Enter a list of numbers:\n")
#strRaw="4,2,6,4,7,5,99,1,3"
print "You entered {0}.".format(strRaw)

intList=[int(i) for i in strRaw.split(",")]

if len(intList) == 1:
  print "Can't sort a single element array."
  sys.exit(1)


def swap(lst, l, r):
  print "swap"
  tmp=lst[l]
  lst[l]=lst[r]
  lst[r]=tmp


firstTime=True
didSwap=False

# Keep bubbling until no swaps can be performed
while firstTime or didSwap:

  print "new bubble"

  firstTime=False
  didSwap=False 
  # start another bubble 
  l=0
  r=l+1

  # compare
  while l < len(intList) - 1:
    if intList[l] < intList[r]:
      l+=1 
      r+=1
    else:
     # Swap these
      swap(intList, l, r)  
      didSwap=True
      l+=1
      r+=1

    print intList
print intList

