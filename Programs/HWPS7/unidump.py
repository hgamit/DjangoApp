#
# unidump.py:
#
#   Starting code H7-2
#

N = int(input("Enter integer N: "))

if N>32:
    for n in range(32,N):
        if(n%32 == 0):
            print("\n",n,": ", chr(n), end='')
        else:
            print(chr(n) , end='')

else:
    print("Please provide number greater than 32")