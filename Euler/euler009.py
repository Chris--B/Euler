from Euler import utils

problem_text = """
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

def compute_answer():
	return pathagorean_triplet_product(1000)

def check_given():
	# We weren't given an example of finding a specific sum for this problem, so we reworked the
	# example they did give us.
	expected = 3*4*5
	actual = pathagorean_triplet_product(3+4+5)
	if actual != expected:
		return"#009: f(3+4+5) gave {}, but expected {}".format(actual, expected)
	return None

def pathagorean_triplet_product(sum_to):
	# We only want the first one.
	a, b, c = next(pathagorean_triplets(sum_to))
	return a * b * c

def pathagorean_triplets(sum_to):
	limit = sum_to
	for a in range(1, limit):
		for b in range(a+1, limit):
			c = sum_to - a - b
			if a ** 2 + b ** 2 == c ** 2:
				yield(a, b, c)
