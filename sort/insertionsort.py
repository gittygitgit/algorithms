#!/usr/bin/python
"""
Algorithm class: sorting
Algorithm name:  insertion sort
Description:     https://en.wikipedia.org/wiki/Insertion_sort

                 Given a list of n items.

		 Track an index into the array such that elements before the index are considered sorted, after unsorted

		 For each index position starting at 0 up till n-1

		 Take the number at the index and insert it into the sorted portion of the array. 

Notes:           Typically done in-place.  Simple.  Fine for small datasets.  More efficient than selection sort since only needs to perform partial scan for each iteration.
Time complexity: n-squared
                 Iteration => N
                 Scan => N
                 Insertion => 1
 

"""
strRaw=raw_input("Enter a list of numbers:\n")
#strRaw="5,2,8,5,10"

print "You entered {0}.".format(strRaw)

# list comprehension
inPlace=[int(i) for i in strRaw.split(",")]

idx=1
"""
Inserts the value at srcIdx into tgtIdx, shifting items to right.
"""
def doInsert(array, srcIdx, tgtIdx):
  print "doInsert [array={0}, val={1}, srcIdx={2}, tgtIdx={3}".format(array, array[srcIdx], srcIdx, tgtIdx)
  val=array[srcIdx]

  limit=srcIdx
  i=limit

  # shift
  while i > tgtIdx:
    array[i] = array[i-1]
    i -= 1
  
  array[tgtIdx] = val
    

def doNext(array, idx):
  sorted=array[0:idx]
  elToInsert=array[idx]
  print "Processing array [idx={0}, sorted={1}, unsorted={2}, elToInsert={3}".format(idx, sorted, array[idx:len(array)], elToInsert)


  for i, el in enumerate(sorted):
    print "Scanning for insertion point [index={0}, val={1}]".format(i, el)
    if el > elToInsert:
      print "Inserting {0} at index {1}".format(elToInsert, i)
      doInsert(array, idx, i)
      break

print "Starting..."      
while idx < len(inPlace):
  doNext(inPlace, idx)
  idx+=1

print "Sorted array ({0})".format(inPlace)
