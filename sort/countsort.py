#!/usr/bin/python

strRaw=raw_input("Enter a list of numbers:\n")
print "You entered {0}.".format(strRaw)


intList=[int(i) for i in strRaw.split(",")]
maxVal=max(intList)
count=[0] * (maxVal + 1)
sorted=[0] * (maxVal + 1)

print count

for i in intList:
  count[i]+=1

print count

counted2=[0] * (maxVal + 1)

for idx, cal in enumerate(count):
  if idx == 0:
    counted2[idx] = count[idx]
  else:
    counted2[idx] = counted2[idx-1] + count[idx]

print counted2   


for i in intList:
  print i
  idx=counted2[i]
  print "index=%d, val=%d" % (idx, i)
  counted2[i] -= 1
  sorted[idx]=i

print sorted
