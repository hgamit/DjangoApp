#
# H8-2: count_alice3.py
#
#   Starting code H8-2
#

# start with your H8-2 count_alice2 and continue...

import re
import sys, os
    #print os.path.dirname(os.path.abspath(sys.argv[0]))

def main():
    dictcount = {}
    f=open(os.path.dirname(os.path.abspath(sys.argv[0]))+"\\alice.txt", "r")
    if f.mode == 'r':
        contents = f.read()
        contents = re.sub('[^A-Za-z0-9]+', ' ', contents)
        contents = contents.split(" ")
        #contents.sort()
        #contents = list(set(contents))
        for x in sorted(contents):
            if(x.isupper() or x.isdigit() or x==""):
                print("",end="")
            elif(not x.islower() and not x.isupper()):
                print("",end="")
            elif(x.islower() and (x in dictcount)):
                dictcount[x] = dictcount[x]+1
            else:
                dictcount[x] = 1

                #print (x)
        for key, value in dictcount.items():
            print(key, end="")
            print(":",end="")
            print(value, end=", ")


if __name__ == "__main__":
    main()



