import math
from Euler import utils

problem_text = """
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""

def nth_prime(num):
	# This follows from the Prime Number Theorem.
	# https://en.wikipedia.org/wiki/Prime_number_theorem
	high_guess = int(num * (math.log(num) + math.log(math.log(num))))

	# The "first" prime is at index 0, the "second" at 1, etc.
	return utils.primes_below(high_guess)[num - 1]

def compute_answer():
	return nth_prime(10001)

given = [
	(13, nth_prime(6)),
]
