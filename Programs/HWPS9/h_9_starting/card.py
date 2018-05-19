'''
Represents a single standard playing card,
with _rank from 1 (Ace) to 13 (King),
suit from 0 (Clubs) to 3 (Spades)
'''

#
# card.py:
#
# 	Starting code for L10
#

SUITS = ["Clubs", "Diamonds", "Hearts", "Spades"]
RANKS = ["", "Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King"]

class Card():
	"""
	Represents a single playing card,
		whose rank internally is int _rank: 1..13 => "Ace".."King"
		and whose suit internally is int _suit 0..3 => "Clubs".."Spades"
	"""

	def __init__(self, rank=1, suit=3):
		'''
		Initialize card with given int suit and int rank
		'''
		self._rank = rank
		self._suit = suit

	def __str__(self):
		'''
		Return the string name of this card:
		"Ace of Spades": translates int fields to strings
		:return:
		'''

		# "Ace of Spades" is string for self._rank==1, self._suit==3

		toreturn = RANKS[self._rank] + " of " + SUITS[self._suit]

		return toreturn

def main():
	'''Create several Cards and print
	Also demonstrate adding new field dynamically...
	'''

    # create first Card

	card1 = Card() # same as Card(1, 3), initializing to the Ace of Spades

	print(card1) # print() adds str(..) automagically
	print(str(card1)) # equivalent to above
	print(card1.__str__())  # long-winded form, but same as the two above

    # create second Card

	card2 = Card(12, 2) # Queen of Hearts

	print(str(card2))

    # add dynamic field to card1

	card1._newfield = 47
	print(card1._newfield)

if __name__ == "__main__":
	main()