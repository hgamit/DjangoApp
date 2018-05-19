#
# H8-4: readint.py
#
#   Starting code H8-4
#

def read_int():
	while True:
		try:
			x = int(input("Please enter an integer: "))
			print(x)
			break
		except ValueError:
			print("Oops!  That was no valid Integer.  Try again...")

	'''
	read int from user and return;
	handle exceptions to defend against invalid ints
	:return:
	'''

read_int()





