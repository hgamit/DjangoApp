#
# count_alice2.py:
#
#   Starting code H7-1
#

# start with your Lab 7 count_alice and continue...
import re
import sys, os
    #print os.path.dirname(os.path.abspath(sys.argv[0]))

def main():
    f=open(os.path.dirname(os.path.abspath(sys.argv[0]))+"\\alice.txt", "r")
    if f.mode == 'r':
        contents = f.read()
        contents = re.sub('[^A-Za-z0-9]+', ' ', contents)
        contents = contents.split(" ")
        #contents.sort()
        contents = list(set(contents))
        for x in sorted(contents):
            if(not x.isupper()):
                print (x)


if __name__ == "__main__":
    main()


