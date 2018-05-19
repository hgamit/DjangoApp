#
# H9-3:
#
#   hand.py
#

from card import Card
from deck import Deck

SUITS = ["Clubs", "Diamonds", "Hearts", "Spades"]
RANKS = ["", "Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King"]


class Hand():
	'''
	Collection of Cards dealt from Deck
	'''
	def __init__(self):
		'''
		Initialzes new Hand by adding empty _cards list
		'''
		self._hand = []

	def addCard(self,cardToAdd):
		'''
		Adds cardToAdd to this Hand
		:param cardToAdd:
		'''
		self._hand.append(cardToAdd)

	def __str__(self):
		'''
		Return string describing all cards in hand
		'''
		# "Ace of Spades" is string for self._rank==1, self._suit==3
		toreturn = ""

		for h in self._hand:
			toreturn += RANKS[h._rank] + " of " + SUITS[h._suit] + "\n"

		return toreturn


def main():
	'''
	Create new Deck, shuffle it, create new Hand,
		deal top 5 Cards of Deck into it,
		then print "stringified" Hand
	'''
	d = Deck()
	d.shuffle()
	hand =  Hand()

	for i in range(5):
		hand.addCard(d.dealCard())
	
	print(hand.__str__())


main()