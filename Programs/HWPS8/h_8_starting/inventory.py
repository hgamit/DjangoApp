#
# HW 8-5: inventory.py
#
#   Starting code for a simple inventory tracking program using
#       dictionaries.
#

def getCommand():
    command = input("Enter command: ")
    return command

def addToInventory(dict):
    while True:
        try:
            itemName = str(input("Enter item: "))
            itemNum = int(input("Enter item count: "))
            dict[itemName] = itemNum
            return dict
    
        except ValueError:
            print("Oops!  That was no valid Input, use string for name and number for count.  Try again...")
    
    #return dict


def viewInventory(dict):
    #if(bool(dict)):
    #    print("No item in Inventory.")
    #else:
    print("items in Inventory:")
    for key, value in dict.items(): 
        print(key, end="")
        print(":",end="")
        print(value)

def main():

    print ("Welcome to StuffMaster, v.0.47")

    inventory = {} # empty dictionary

    while True: # get command, process command; quit when selected below
        try:
            cmd = getCommand()
            if(cmd == 'A'):
                inventory=addToInventory(inventory)
            elif(cmd== 'V'):
                viewInventory(inventory)
            elif(cmd== 'Q'):
                break
            else:
                raise ValueError
        except ValueError:
            print("Oops!  That was no valid input: A to ADD, V to View and Q to print inventory and Exit.  Try again...")

        # Get the command,
        #
        # Call the appropriate function based on command
        #
        # If unknown command, complain and prompt for reentry

    # here, we're quitting

    print ("Quitting. Final version of inventory is:")

    # print out final version of inventory
    viewInventory(inventory)
    print ("Exiting...")

main()
