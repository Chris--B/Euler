from collections import defaultdict
from Euler import utils

problem_text = """

"""

def compute_answer():
	return longest_collatz_length_below(int(1e6))

def check_given():
	expected = 9
	actual = longest_collatz_length_below(10)
	if actual != expected:
		return "#014: f(5) returned {}, but expected {}".format(actual, expected)
	return None

def longest_collatz_length_below(num):
	cache = dict()
	cache[1] = 0

	# Skip evens. They all have a corresponding odd somewhere.
	for number in range(3, num, 2):
		calc_collatz_length(number, cache)

	# Some intermediate numbers will jump way above the limit we have.
	# Make sure we don't count them.
	eligible = ((number, length) for (number, length) in cache.items() if number <= num)

	# We want the chain with the longest length.
	return max(eligible, key=lambda item: item[1])[0]

def calc_collatz_length(num, cache):
	"""
	Calculate the collatz length of `num`, storing it in `cache`. `cache` is expected to map numbers
	to collatz lengths, and is used to reduce repeated computation.
	"""

	history = []
	# We're going to need the value of `num` later.
	xx = num

	while xx not in cache.keys():
		history.append(xx)
		if xx % 2 == 0:
			xx //= 2
		else:
			xx = 3*xx + 1

	# `xx` is either 1 or a number we've already computed.
	# Either way, it returns 0.
	length = cache[xx]
	# The length of the last item acts as a base length for the rest, which are linear
	# with their position in the history... from the back.
	for (offset, number) in enumerate(reversed(history)):
		cache[number] = length + offset

	return cache[num]
