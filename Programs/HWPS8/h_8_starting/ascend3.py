#
# HW 8-1: ascend3.py
#
#   Starting code for program that prints out all 3 digit ints
#		abc where a < b < c
#

for f in range(10):
    for s in range(10):
        for t in range(10):
            if(f<s and s<t):
                print (f, end="")
                print(s,end="")
                print(t, end=", ")
            elif(f==0 and s==0):
                print (f, end="")
                print(s,end="")
                print(t, end=", ")



