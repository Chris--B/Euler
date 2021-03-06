from Euler import utils

problem_text = """
215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 21000?
"""

def paths_over_square_lattice(size):
	return nCr(2*size, size)

def nCr(n, r):
	r = min(r, n-r)

	if r == 0:
		return 1

	numerator = utils.product(range(n, n-r, -1))
	denominator = utils.product(range(1, r+1))

	return numerator // denominator

def compute_answer():
	return paths_over_square_lattice(20)

given = [
	(6, paths_over_square_lattice(2)),
]
