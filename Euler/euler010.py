from Euler import utils

problem_text = """
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

def compute_answer():
	return sum(utils.primes_below(int(2e6)))

given = [
	(17, sum(utils.primes_below(10))),
]
