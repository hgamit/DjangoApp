import string

def remove_all(substr,theStr):
    return theStr.replace(substr,"")

if __name__ == '__main__':
    s = input("Please enter a string: ")
    sub = input("Please enter a substring to remove from string: ")
    print(remove_all(sub,s))