#!/usr/bin/python
print "hello"

strRaw=raw_input("Enter a list of numbers:\n")
print "You entered {0}.".format(strRaw)


intList=[int(i) for i in strRaw.split(",")]
maxVal=max(intList)
sorted=[0] * maxVal
print sorted

for i in intList:
  print i
  sorted[i-1]+=1

print sorted
i=0
while i < len(sorted):
  j=0
  if sorted[i] > 0:
    while j < sorted[i]:
      print i+1
      j+=1  
  i+=1


