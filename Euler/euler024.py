from itertools import permutations

problem_text = """
A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
"""

def compute_answer():
	return nth_lexico_perm(1000000, "0123456789")

def check_given():
	expected = 210
	actual = nth_lexico_perm(6, "012")
	if actual != expected:
		return "#024: Found {}, but expected {}".format(actual, expected)
	return None

def nth_lexico_perm(num, things):
	perms = permutations(things)
	for _ in range(num):
		res = next(perms)
	return int(''.join(res))
