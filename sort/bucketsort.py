#!/usr/bin/python
print "hello"

strRaw=raw_input("Enter a list of numbers:\n")
print "You entered {0}.".format(strRaw)


intList=[int(i) for i in strRaw.split(",")]
maxVal=max(intList)
i=0
sorted=[]
while i <= maxVal:
  sorted.append(0)
  i+=1

for i in intList:
  sorted[i]+=1

print sorted

i=0
while i < len(sorted):
  j=0
  if sorted[i] > 0:
    while j < sorted[i]:
      print i
      j+=1  
  i+=1


