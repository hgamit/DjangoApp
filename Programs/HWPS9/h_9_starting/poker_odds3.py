#
# H9-4:
#
#   poker_odds3.py
#

import random

SUITS = ["Clubs", "Diamonds", "Hearts", "Spades"]
RANKS = ["", "Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King"]

class Card():
    """
    Represents a single playing card,
        whose rank internally is int _rank: 1..13 => "Ace".."King"
        and whose suit internally is int _suit 0..3 => "Clubs".."Spades"
    """

    def __init__(self,rank=1,suit=3):
        '''
        Initialize card with given int suit and int rank
        :param rank:
        :param suit:
        :return:
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

#CARD CLASS ENDS HERE

class Deck():
    """
    Represents a deck of 52 standard playing cards,
        as a list of Card refs
    """
    def __init__(self):
        '''
        Initialize deck: field _cards is list containing
            52 Card refs, initially
        :return: nothing
        '''

        self._cards = []
        for rank in range(1,14):
            for suit in range(4):

                c = Card(rank,suit)
                self._cards.append(c)

    def __str__(self):
        '''
        "Stringified" deck: string of Card named,
        with \n for easier reading
        :return:
        '''
        toreturn = ''

        # for index in range(len(self._cards)):
        #     self._cards[index]

        for c in self._cards:
            temp = str(c) # temp is the stringified card
            toreturn = toreturn + temp + "\n" # note \n at end

        return toreturn

    def shuffle(self):
        random.shuffle(self._cards) # note random function to do this

    def dealCard(self):
        toreturn = self._cards.pop(0) # get and remove top card from deck
        return toreturn

#DECK CLASS ENDS HERE

class Hand2():
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
    
	def buildDict(self,hand):
	    dict = {}
	    for h in hand:
	        dict[h.__str__()] = h._rank
    
	    return dict
    
	def hasOnePair(self):
    
    # Check for EXACTLY one value of 2 in dict
    # Note there might be 2 pairs; hence the counting of pairs
    
	    dict = self.buildDict(self._hand)
	    twocount=0
	    values = []
	    values=list(dict.values())
	    values.sort()
	    i=0
	    while i<len(values):
	        if values.count(values[i])==2:
	            twocount += 1
	            i = i+1
	        i=i+1
    
	    if twocount == 1:
	        return True
	    else: 
	        return False
    
	def hasTwoPairs(self):
	    ''' Complete this! :param dict: dictionary with card ranks to check'''
	    dict = self.buildDict(self._hand)
	    twocount=0
	    values = []
	    values=list(dict.values())
	    values.sort()
	    i=0
	    while i<len(values):
	        if values.count(values[i])==2:
	            twocount += 1
	            i = i+1
	        i=i+1
        
	    if twocount == 2:
	        return True
	    else: 
	        return False

	def hasThreeOfAKind(self):
	    '''
        Complete this!
        :param dict: dictionary with card ranks to check
        '''
	    dict = self.buildDict(self._hand)
	    threecount=0
	    values = []
	    values=list(dict.values())
	    values.sort()
	    i=0
	    while i<len(values):
	        if values.count(values[i])==3:
	            threecount += 1
	            i = i+2
	        i=i+1
        
	    if threecount == 1:
	        return True
	    else: 
	        return False

	def hasFullHouse(self):
	    '''
        Complete this!
        :param dict: dictionary with card ranks to check
        '''
	    dict = self.buildDict(self._hand)
	    twocount=0
	    threecount=0
	    values = []
	    values=list(dict.values())
	    values.sort()
	    i=0
	    while i<len(values):
	        if values.count(values[i])==2:
	            twocount += 1
	            i = i+1
	        elif values.count(values[i])==3:
	            threecount += 1
	            i = i+2
	        i=i+1
        
	    if twocount == 1 and threecount==1:
	        return True
	    else: 
	        return False

	def hasFourOfAKind(self):
	    '''
        Complete this!
        :param dict: dictionary with card ranks to check
        '''
	    dict = self.buildDict(self._hand)
	    fourcount=0
	    values = []
	    values=list(dict.values())
	    values.sort()
	    i=0
	    while i<len(values):
	        if values.count(values[i])==4:
	            fourcount += 1
	            i = i+4
	        i=i+1
        
	    if fourcount == 1:
	        return True
	    else: 
	        return False

	def hasStraight(self):
	    '''
        Complete this!
        :param dict: dictionary with card ranks to check
        '''
	    dict = self.buildDict(self._hand)
	    straight=0
	    values = []
	    values=list(dict.values())
	    values.sort()
	    for i in range(0,len(values)-1):
	        if values[i]<values[i+1]:
	            straight = 1
	        else:
	            straight = 0
	            break
        
	    if straight == 1:
	        return True
	    else: 
	        return False

	def hasFlush(self):
	    ''' 
        Complete this!
        :param dict: dictionary with card ranks to check
        '''
	    dict = self.buildDict(self._hand)
	    flush=0
	    keys = []
	    keys=list(dict.keys())
	    keys.sort()
        #[suit for suit in SUITS if(suit in keys)]
	    for i in range(0,len(keys)-1):
	        for suit in SUITS:
	            if suit in keys[i] and suit in keys[i+1]:
	                flush = 1
	            else:
	                flush = 0
	                break
        
	    if flush == 1:
	        return True
	    else: 
	        return False

	def hasStraightFlush(self):
	    '''
        Complete this!
        :param dict: dictionary with card ranks to check
        '''
	    dict = self.buildDict(self._hand)
	    if Hand2.hasStraight(dict) and Hand2.hasFlush(dict):
	        return True
	    else: 
	        return False

	def hasRoyalFlush(self, dict):
	    '''
        Complete this!
        :param dict: dictionary with card ranks to check
        '''
        #straight=0
	    dict = self.buildDict(self._hand)
	    values = []
	    values=list(dict.values())
	    values.sort()

	    if values[0]==10 and Hand2.hasStraight(dict) and Hand2.hasFlush(dict):
	        return True
	    else: 
	        return False

    #Hand2 ENDS Here

def main():

# finish this...

    TRIALS = 10000 # int(input ("Input number of hands to test: "))

    hand = [] # list of Card in hand

# accumulators for different counts

    onepairCount = 0
    twopairCount = 0
    threeCount = 0
    fourCount = 0
    fullHouseCount = 0

    # more if you wish...

    for num in range(TRIALS):

        d = Deck()
        d.shuffle()
        hand = []

        for count in range(5):
            hand.append(d.dealCard())

        dict = buildDict(hand)

        if hasOnePair(dict):
            onepairCount += 1
##        elif hasTwoPairs(dict):
##            twopairCount += 1
##        elif hasThreeOfAKind(dict):
##            threeCount += 1
##        elif hasFourOfAKind(dict):
##            fourCount += 1
##        elif hasFullHouse(dict):
##            fourCount += 1

        # add more if you wish...

    # print out results...

    print ("Number of one pair hands is: ", onepairCount)

    print ("% of hands: ", 100.0 * onepairCount / TRIALS)
1
def test():
    ''' hardcoded hand, allowing test of hasXXX() methods
    '''

    testhand = [Card(2,3),Card(1,2),Card(1,1),Card(13,2), Card(2,0)]

    dict = buildDict(testhand)

    print ("Does handtest contain exactly one pair? %s" % hasOnePair(dict))

def testCard():

    card1 = Card(1,3)
    card2 = Card(12,2)

    card1._newfield = 47
    #print(card1)
    #print (card1.__str__()) # long-winded form
    print (card1._newfield)
    print(card1)
    print (str(card2))

def testDeck():
    '''
    Test Deck: create, print then shuffle, print again
    Then deal first two cards and print, along with bottom card
    '''
    deck = Deck()
    print (str(deck))

    print ("Now we shuffle:\n")

    deck.shuffle()
    print (str(deck))

    c = deck.dealCard()

    c2 = deck.dealCard()

    print ("The first card dealt is",str(c), "and the second is",str(c2))
    print ("Bottom of deck is", deck._cards[-1]) # can't hide the implementation!

if __name__ == "__main__":

    #testCard() # uncomment to test creating & calling Card methods

    test() # uncomment to test hand (list of 5 Card obj) for one pair

    # main() # uncomment to run general poker odds calculations

    #testDeck()  # uncomment to test Deck: create, print, shuffle, print



