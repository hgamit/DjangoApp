#
# H9-5:
#
#   in_riffle.py
#
#   Note provided deck.py has outRiffle() as done in Lab 10
#		Modify this within Deck, adding new method inRiffle().
#

import random
import card

class Deck():
	"""
	Represents a deck of 52 standard playing cards,
		as a list of Card refs
	"""

	def __init__(self):
		'''
		Initialize deck: field _cards is list containing
			52 Card refs, initially
		'''

		self._cards = []
		for rank in range(1, 14):
			for suit in range(4):
				c = card.Card(rank, suit)
				self._cards.append(c)

	def __str__(self):
		'''
		"Stringified" deck: string of each Card,
		concatenated with '\n' for easier reading
		'''
		toreturn = ''

		# for index in range(len(self._cards)):
		#     self._cards[index]

		for c in self._cards:
			temp = str(c)  # temp is the stringified card
			toreturn = toreturn + temp + "\n"  # note \n at end

		return toreturn

	def shuffle(self):
		random.shuffle(self._cards)  # note random function to do this

	def dealCard(self):
		toreturn = self._cards.pop(0)  # get and remove top card from deck
		return toreturn

	## L10-1: add new method randomCard()

	def randomCard(self):
		rank = random.randint(1,13) # randrange(1,14)
		suit = random.randint(0,3) # randrange(0,4)

		c = card.Card(rank,suit)

		return c

	## L10-3: add new method dealHand()

	def dealHand(self):
		hand = []
		for count in range(5):
			try:
				c = self.dealCard()
			except IndexError:
				self.__init__()
				c = self.dealCard()

			hand.append(c)

		return hand

	## L10-4: add new method outRiffle()

	def outRiffle(self):
		top_half = []
		bottom_half = []

		# deal half of deck into top_half

		for count in range(len(self._cards)//2):
			c = self.dealCard()
		1	top_half.append(c)

		# deal remaining in self._cards into bottom_half

		for c in self._cards:
			bottom_half.append(c)

		# clear out current Deck's cards

		self._cards=[]

		for c in top_half:
			self._cards.append(c)
			bc = bottom_half.pop(0)
			self._cards.append(bc)

		for c in bottom_half:
			self._cards.append(c)

	# H9-4: add new method inRiffle()

	def inRiffle(self):
		b_half = []
		t_half = []

		# deal half of deck into b_half

		for count in range(len(self._cards)//2):
			c = self.dealCard()
			b_half.append(c)

		# deal remaining in self._cards into t_half

		for c in self._cards:
			t_half.append(c)

		# clear out current Deck's cards

		self._cards=[]

		for c in b_half:
			self._cards.append(c)
			bc = t_half.pop(0)
			self._cards.append(bc)

		for c in t_half:
			self._cards.append(c)

def main():
	'''
	Create, print then shuffle, print again
	Then deal first two cards and print, along with bottom card
	'''

    # create and print new Deck

	deck = Deck()
	print(str(deck))

    # shuffle and print Deck

	print("Now we shuffle:\n")

	deck.shuffle()
	print(str(deck))

    # deal two cards from Deck, and report them

	c = deck.dealCard()
	c2 = deck.dealCard()

	print("The first card dealt is", str(c), "and the second is", str(c2))
	print("Bottom of deck is", deck._cards[-1])  # can't hide the implementation!

if __name__ == "__main__":
	main()
