from Euler import utils

problem_text = """
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

def largest_prime_factor(num):
	prime, power = utils.prime_factors(num)[-1]
	return prime

def compute_answer():
	return largest_prime_factor(600851475143)

given = [
	(29, largest_prime_factor(13195)),
]
