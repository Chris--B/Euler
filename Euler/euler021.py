from Euler import utils
import math

problem_text = """
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""

def compute_answer():
	return sum(amicable_numbers_below(10000))

def check_given():
	expected = 504
	actual = sum(amicable_numbers_below(1000))
	if actual != expected:
		return "#021: f(10) returned {}, but expected {}".format(
			actual, expected)
	return None

@utils.memoize
def d(number):
	""""
	Return the sum of proper divisors of n (numbers < n which divide n).
	"""
	res = 0
	for num in range(1, number):
		if number % num == 0:
			res += num
	return res

def amicable_numbers_below(below):
	"""
	Return a list of numbers < below which are in an amicable pair.
	"""
	pairs = []

	for num in range(1, below):
		# Don't recalculate it if we don't have to.
		d_num = d(num)

		# Numbers which are their own pair are surprisingly common. 6, 28, and 496 below 1000. Wow!
		if d(d_num) == num and d_num != num:
			pairs.append(num)

	return pairs
