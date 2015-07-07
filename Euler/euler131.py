from bisect import bisect_left
from Euler import utils
import math

problem_text = """
There are some prime values, p, for which there exists a positive integer, n,
such that the expression n^3 + n^2 * p is a perfect cube.

For example, when p = 19, 8^3 + 8^2×19 = 12^3.

What is perhaps most surprising is that for each prime with this property the
value of n is unique, and there are only four such primes below one-hundred.

How many primes below one million have this remarkable property?
"""

def compute_answer():
	return len(prime_cubes_below(1000000))

def check_given():
	expected = 4
	actual = len(prime_cubes_below(100))
	if actual != expected:
		return "#131: Found {}, but expected {}".format(
			actual, expected)
	return None

def prime_cubes_below(below):
	primes = utils.primes_below(below)
	res = []

	for m in range(1, int(math.sqrt(below)) + 1):
		k = m ** 2
		n = k * m # m ** 3
		p = k**3 / n**2 + 3*k**2 / n + 3*k
		p_idx = bisect_left(primes, p)
		if 0 < p_idx < len(primes) and primes[p_idx] == p:
			res.append((n, int(p), k))
		# sqrt(below) is an upper bound on the upper bound. Bail out when we
		# hit it exactly.
		if p >= below:
			break

	return res
