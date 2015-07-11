from collections import defaultdict
from Euler import utils

problem_text = """
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains
10 terms. Although it has not been proved yet (Collatz Problem), it is thought
that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
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

	# The number with the longest chain seed so far.
	longest_chain = 1

	# Skip evens. They all have a corresponding odd somewhere, except for things
	#  with high powers
	# of two. But those aren't going to have long chains anyway.
	for number in range(3, num, 2):
		length = calc_collatz_length(number, cache)
		if length > cache[longest_chain] and number < num:
			longest_chain = number

	return longest_chain

def calc_collatz_length(num, cache):
	"""
	Calculate the collatz length of `num`, storing it in `cache`. `cache` is
	expected to map numbers to collatz lengths, and is used to reduce repeated
	computation.
	"""

	history = []
	# We're going to need the value of `num` later, so best we don't modify it.
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
	# The length of the last item acts as a base length for the rest, which are
	# linear with their position in the history... from the back.
	for (offset, number) in enumerate(reversed(history)):
		cache[number] = length + offset

	return cache[num]
