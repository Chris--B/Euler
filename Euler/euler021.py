from Euler import utils
import math

problem_text = """
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""

def d(number, primes):
	""""
	Return the sum of proper divisors of n (numbers < n which divide n).
	"""
	total = 1

	# We make use of this algorithm:
	# http://mathschallenge.net/index.php?section=faq&ref=number/sum_of_divisors
	# Basically, the sum of divisors is also the product of co-prime divisors plus 1.
	#     e.g., for 72 = 2^3 * 3^2, the sum of all divisors = (2^3 + 1) * (3^2 + 1).
	#     Since we only want divisors less than `number`, we subtract it off at the end.
	for prime, power in utils.prime_factors_cached(number, primes):
		if power == 1:
			total *= prime + 1
		else:
			total *= (prime ** (power+1) - 1) // (prime - 1)

	# Remember, only the divisors < number. Not <=.
	return total - number

def amicable_numbers_below(below):
	"""
	Return a list of numbers < below which are in an amicable pair.
	"""
	pairs = []
	primes = utils.primes_below(below)

	for num in range(1, below):
		# Don't recalculate it if we don't have to.
		d_num = d(num, primes)

		# Only bother computing d(d_num) if num is the smaller in the pair. Then we never skip this
		# *first*.
		# This also rules out "perfect" numbers (where d_num == num).
		if d_num > num and d(d_num, primes) == num:
			pairs.append(num)
			pairs.append(d_num)

	return pairs

def compute_answer():
	return sum(amicable_numbers_below(10000))

given = [
	(504, sum(amicable_numbers_below(1000))),
]
