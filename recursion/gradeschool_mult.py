#!/usr/bin/python
import math
'''
Input: two n-digit numbers X and Y
Output: Product X * Y

Setup:
  Create a multi-dimentional array to hold temp output
Method:
  For each digit in Y working from least to most significant digit (right to left):
    Multiply by each digit in X working right to left.

    
'''
import sys
operands=raw_input("Enter two positive numbers:\n")

opList=operands.split(",")

def usage():
  print "bad"


if len(opList) != 2:
  usage()
  sys.exit()
print "You entered {0}.".format(operands)

# Make larger number X
isSwap=len(opList[1]) > len(opList[0])

X=opList[1] if isSwap else opList[0]
Y=opList[0] if isSwap else opList[1]

# Setup temp output storage
output=[[0]*(len(X) + len(Y) + 1) for _ in range(len(Y))]
print(len(output))

level=0
shift=level

for i in reversed(Y):
 
  print "XXX" + str(level) 
  levelIdx=1 + level
  curOutput=output[level]

  carry=0
  for idx, j in enumerate(reversed(X)):
    isLast=(len(X) == idx + 1)
    r=int(i)*int(j)
    rpc=r+carry
    print "multiplying {0} by {1}, add carry {2} = {3}".format(i, j, carry, rpc)
    print idx
    print len(X)
    if not isLast:
      curOutput[-levelIdx]=rpc%10 
    else:
      if rpc < 10:
        curOutput[-levelIdx]=rpc
      else:
        curOutput[-levelIdx]=rpc%10 
        levelIdx+=1
        curOutput[-levelIdx]=int(math.floor(rpc/10))
        continue

    carry=int(math.floor(rpc/10)) 
    print "raw={0}, carry={1}".format(r,carry)
    print curOutput
    levelIdx +=1
       
  level += 1      

# finally add subtotals
for o in output:
  print o
 
result=0
for o in output:
  result += int(''.join(map(str, o)))

print result 
