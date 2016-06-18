#!/usr/bin/python
"""
Algorithm class: sorting
Algorithm name:  selection sort
Description:     https://en.wikipedia.org/wiki/Selection_sort
                 
                 Given a list of unsorted items.

                 Maintains index demarcating sorted / unsorted portion of the list. 
                  
                 Compares item at current index with min val of unsorted items, swapping if necessary.   
Notes:           Old.  Simple.  In-place.
Efficiency:      Iterate over list => (N-1)
                 For each iteration, 
                 - determine minimum value of unsorted items (worst case N-1)
                 - compare
                 - swap if necessary

"""
strRaw=raw_input("Enter a list of numbers:\n")
print "You entered {0}.".format(strRaw)

listRaw=[int(i) for i in strRaw.split(",")]

sorted=[]

size=len(listRaw)

i=0

while i <= size-2:
  slice=listRaw[i:size]
  # print listRaw[i:size]
  minVal=min(slice)
  print minVal
  print listRaw[i]
  print "Comparing [left={0}, right={1}]".format(listRaw[i], minVal)

  if listRaw[i] > minVal:
    print "swapping..."
    temp=listRaw[i]
    idx=slice.index(minVal)
    listRaw[i]=minVal
    listRaw[idx+i]=temp
    print listRaw
  i+=1

print listRaw


     
     
