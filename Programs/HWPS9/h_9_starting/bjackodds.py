#
# H9-2:
#
#   bjackodds.py
#

import random
from card import Card
from deck import Deck

TRIALS = 10000

def main():
	'''
	Repeat the following of TRIALS
	'''
	# finish this...
	#hand = [] # list of Card in hand
	#deck = Deck()
	blackJackCount = 0

	for num in range(TRIALS):
		#print ("Now we shuffle:\n")
		deck = Deck()
		deck.shuffle()
		#print (str(deck))
		c = deck.dealCard()
		c2 = deck.dealCard()
		if (c._rank==1 or c2._rank == 1) and (c._rank in [10,11,12,13] or c2._rank in [10,11,12,13]):
			blackJackCount += 1


	#print ("The first card dealt is",str(c), "and the second is",str(c2))
	#print ("Bottom of deck is", deck._cards[-1]) # can't hide the implementation!

    # print out results...
	p= 100.0 * blackJackCount / TRIALS

	print ("Number of Black Jack hands is: ", blackJackCount)

	print ("% of Black Jack hands: ", )

	print("General Probability of getting Black Jack is around 2% comapare to our trial ",end="")
	print(p,end="")
	print("%")

if __name__ == '__main__':
	print("Black Trials Running...")
	main()