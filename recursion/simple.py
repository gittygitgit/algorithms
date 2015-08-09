#!/usr/bin/python

'''
Use recursion to sum an arbitrary list of numbers
'''

numList=[1,2,3,4,5]

def dumbSum(numbers):
  print "foo"
  return sum(numbers)

def anotherDumSum(numbers):
  result=0
  for i in numbers:
    result += i
  return result

def recursiveSort(numberList):
  if len(numberList) > 2:
    return numberList[0] + recursiveSort(numberList[1:])
  else:
    return numberList[0] + numberList[1]

 
print dumbSum(numList)
print anotherDumSum(numList)
print recursiveSort(numList)



