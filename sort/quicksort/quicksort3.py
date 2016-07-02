#!/usr/bin/python
'''
Uses median el as pivot.
'''
with open("entries.txt") as f:
  entries=f.readlines()

print len(entries)

# list comprehension
inPlace=[int(i) for i in entries]
print len(inPlace)

#def swap(a, i, j):

#inPlace=[9,6,7,8,5,2,1,4,3]  
numCompares=0

def choosePivot(a):
  med=(len(a)/2)-1 if len(a)%2 == 0 else (len(a)-1)/2

  idx=-1;
  if a[0] <= a[med] <= a[-1] or a[-1] <= a[med] <= a[0] :
    idx = med
  elif a[med] <= a[0] <= a[-1] or a[-1] <= a[0] <= a[med]:
    idx = 0
  else:
    idx = -1 

  return idx

def partition(a, p):
  print "Partition [a={0}, pivot={1}]".format(a, str(p))

  # i is the index between el's less than the pivot and greater than the pivot
  i=1

  # j is the index between el's that have been iterated over and those that haven't
  j=1

  # while there's more el's to iterate over
  while j < len(a):
    
    val = a[j]
    if val < p:
      if j > 1:
        a[j] = a[i]
        a[i] = val
      i += 1 
    j+=1

  # swap in pivot
  a[0]=a[i-1]
  a[i-1] = p
  return i
  
def quicksort(a, level):
  level  += 1
  idx=choosePivot(a)
 
  print "pivotIdx={0}".format(idx)
  pivot = a[idx]
  global numCompares

  # Swap pivot w/ first element just before the partition subroutine is called
  a[idx] = a[0]
  a[0] = pivot

  numCompares += (len(a) - 1)
  print "Quicksort [level={0}, len(a)={1}, pivot={2}]".format(level, str(len(a)), str(pivot))
  if len(a) == 1:
    print "basecase"
    return a
 
  pivotIdx=partition(a, pivot)

  print "Partitioned={0}, pivotIdx={1}".format(a, pivotIdx)
  # recursively sort subarrays

  l = [] if pivotIdx == 0 else a[0:pivotIdx-1]
  
  r=[] if pivotIdx == len(a) else a[pivotIdx:len(a)]

  print "Recursively invoking quicksort [l={0}, r={1}]".format(l, r)

  if (len(l) > 0):
    l=quicksort(l, level)
  if (len(r) > 0):
    r=quicksort(r, level)
  
  
  l.append(pivot)
  result = l + r
  print "sorted={0}".format(result)
  return result

print "Starting [unsorted={0}".format(inPlace)
result = quicksort(inPlace, 0)
print len(result)
print result
print numCompares
