from Euler import utils

problem_text = """
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

def compute_answer():
	return sum_primes_below(int(2e6))

def check_given():
	# We weren't given an example of finding a specific sum for this problem, so we reworked the
	# example they did give us.
	expected = 17
	actual = sum_primes_below(10)
	if actual != expected:
		return"#010: f(10) gave {}, but expected {}".format(actual, expected)
	return None

def sum_primes_below(num):
	primes = utils.primes_below(num)
	return sum(primes)
