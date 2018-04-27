#
# strip_comments.py:
#
#   Starting code H7-4
#

# read string fname from user

# open Python source file named fname.py for reading

# create new file 'strip_' + fname.py for writing

# for each line in fname file:

# read line remove comments: starting at # and going to end of line

# write modified line to output file

# close both files

import os, sys

def main():
    fname = input("Enter Python FIle Name(include .py): ")
    f = open(fname).read().splitlines()
    f_w= open('strip_'+fname,"w+")
    for x in f:
        if(not x.startswith('#')):
            f_w.write("%s\r\n" % x)
    
    #f.close()
    f_w.close()

if __name__ == "__main__":
    main()
