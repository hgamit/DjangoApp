import re, sys

#724-21-8121

if re.match(r"^(?!000|666)[0-8][0-9]{2}-(?!00)[0-9]{2}-(?!0000)[0-9]{4}$", sys.argv[1]):
    print ("SSN is valid")
else:
    print ("SSN is invalid")