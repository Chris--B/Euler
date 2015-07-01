from Euler import utils
from bisect import bisect_left
from fractions import gcd, Fraction

problem_text = """
Let S(n) = a+b+c over all triples (a,b,c) such that:

    a, b, and c are prime numbers.
    a < b < c < n.
    a+1, b+1, and c+1 form a geometric sequence.

For example, S(100) = 1035 with the following triples:

(2, 5, 11), (2, 11, 47), (5, 11, 23), (5, 17, 53), (7, 11, 17), (7, 23, 71),
(11, 23, 47), (17, 23, 31), (17, 41, 97), (31, 47, 71), (71, 83, 97)

Find S(10^8).
"""

def compute_answer():
	return s(1000)

#	return s(10 ** 5)

def check_given():
	expected = 1035
	actual = s(100)
	if actual != expected:
		return "#518: Found {}, but expected {}".format(actual, expected)
	return None

def s(num):
	def triples():
		print("Finding primes <", num)
		primes = utils.primes_below(num)
		print("    ...found", len(primes))
		count = 0
		for c_idx, c in enumerate(primes):
			for b_idx, b in enumerate(primes[:c_idx]):
				count += 1
				ratio = (c + 1) / (b + 1)
				a = (b + 1) / ratio - 1
				a_idx = bisect_left(primes[:b_idx], a)
				if primes[a_idx] == a:
					a = int(a)
					assert(a < b < c < num)
					if num == 100:
						f = utils.prime_factors
						print(
							"""
=================================================
({}, {}, {})
pf(a+1): {}
pf(b+1): {}
pf(c+1): {}
ratio  : {}
gcd(a+1, b+1, c+1): {}
=================================================
							""".format(
								a, b, c,
								f(a+1), f(b+1), f(c+1),
								Fraction(c+1, b+1),
								f(gcd(a+1, gcd(b+1, c+1)))))
					yield a, b, c
		print(count)

	return sum(a + b + c for (a, b, c) in triples())
