from Euler import utils

problem_text = """
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

def compute_answer():
	return largest_prime_factor(600851475143)

def check_given():
	expected = 29
	actual = largest_prime_factor(13195)
	if actual != expected:
		return "#003: prime_factors(13195) returned {}, but expected {}.".format(actual, expected)
	return None

def largest_prime_factor(num):
	prime, power = utils.prime_factors(num)[-1]
	return prime
