from Euler import utils

problem_text = """
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

def largest_power_bounded(base, bound):
	num = 1
	power = 0
	while num < bound:
		power += 1
		num *= base
	return power-1

def smallest_evenly_divided(limit):
	# Assume we have all the primes <= limit.
	# So... pretend limit <= 23.
	assert(limit <= 23)
	primes = [2, 3, 5, 7, 11, 13, 17, 19, 23]
	return utils.product(prime ** largest_power_bounded(prime, limit) for prime in primes)

def compute_answer():
	return smallest_evenly_divided(20)


given = [
	(2520, smallest_evenly_divided(10)),
]