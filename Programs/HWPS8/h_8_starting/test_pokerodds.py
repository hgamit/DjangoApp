'''
test_pokerodds.py:

py.test unit test to check for one pair
'''
import pokerodds as p

def test_one_pair():

	testhand = [p.Card(2, 3), p.Card(1, 2), \
				p.Card(3, 1), p.Card(13, 2), \
				p.Card(2, 0)]

	dict = p.buildDict(testhand)

	assert p.hasOnePair(dict)

def test_two_pair():

	testhand = [p.Card(2, 3), p.Card(1, 2), \
				p.Card(1, 1), p.Card(13, 2), \
				p.Card(2, 0)]

	dict = p.buildDict(testhand)

	assert p.hasTwoPairs(dict)

def test_threeofAkind():

	testhand = [p.Card(2, 3), p.Card(1, 2), \
				p.Card(2, 1), p.Card(13, 2), \
				p.Card(2, 0)]

	dict = p.buildDict(testhand)

	assert p.hasThreeOfAKind(dict)

def test_fullHouse():

	testhand = [p.Card(2, 3), p.Card(1, 2), \
				p.Card(2, 1), p.Card(1, 0), \
				p.Card(2, 0)]

	dict = p.buildDict(testhand)

	assert p.hasFullHouse(dict)

if __name__ == '__main__':
	print("Prints error only if assertion fails")
	test_one_pair()
	test_two_pair()
	test_threeofAkind()
	test_fullHouse()
