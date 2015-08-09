#!/usr/bin/python

strRaw=raw_input("Enter a list of numbers:\n")
#strRaw="5,2,8,5,10"

print "You entered {0}.".format(strRaw)

intList=[int(i) for i in strRaw.split(",")]

sorted=[]

sorted=intList

idx=0

'''
algorithm definition

given an unsorted array of length n

track an index into the array such that elements before the index are considered sorted, after unsorted

for each index position starting at 0 up till n-1

take the number at the index and insert it into the sorted portion of the array 
'''

def foo(array, idx):
  sorted=array[0:idx]
  elToInsert=array[idx]
  print "Processing array [idx={0}, sorted={1}, unsorted={2}, elToInsert={3}".format(idx, sorted, array[idx:len(array)], elToInsert)


  for i, el in enumerate(sorted):
    print "Enumerating [index={0}, val={1}]".format(i, el)
    if el > elToInsert:
      print "Swapping in {0} at index {1}".format(elToInsert, i)
      temp=el
      array[i]=elToInsert
      array[idx]=temp
      break
      
while idx < len(intList):
  foo(intList, idx)
  idx+=1

print "Sorted array ({0})".format(intList)
