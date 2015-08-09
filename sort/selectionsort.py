#!/usr/bin/python

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


     
     
