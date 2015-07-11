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

def longest_collatz_length_below(below):
	cache = defaultdict(lambda: None)
	cache[1] = 0

	# The number with the longest chain seed so far.
	longest_chain = 1

	# Skip evens. They all have a corresponding odd somewhere, except for things
	#  with high powers
	# of two. But those aren't going to have long chains anyway.
	for number in range(3, below, 2):
		if cache[number] is None:
			calc_collatz_length(number, cache)
		if cache[number] > cache[longest_chain]:
			longest_chain = number

	return longest_chain

def calc_collatz_length(number, cache):
	num = number
	path = []
	while cache[num] is None:
		path.append(num)
		if num % 2 == 0:
			num = num // 2
		else:
			num = 3*num + 1
	base_length = cache[num]
	for (offset, path_num) in enumerate(reversed(path), start=1):
		cache[path_num] = base_length + offset