import math

problem_text = """
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

def compute_answer():
	return largest_palindrome_from_n_digit_product(3)

def check_given():
	expected = 9009
	actual = largest_palindrome_from_n_digit_product(2)
	if actual != expected:
		return "#004: largest_palindrome_from_n_digit_product(2) returned {}, but expected {}".format(
			actual, expected)
	return None

def largest_palindrome_from_n_digit_product(digits):
	limit = 10 ** digits - 1

	largest = 0

	# Larger factors usually means larger number. Start the search at 99...9 and go down.
	# The lower bound doesn't matter, because we'll break out of it before hitting it.
	# TODO: Test that claim.
	for a in range(limit, limit // 10, -1):
		for b in range(limit, a, -1):
			# No point in making `b` smaller: it's already too small, so just skip the rest of
			# the `b`s for this `a`.
			if a*b < largest:
				break

			string = str(a*b)
			if string == string[::-1]:
				largest = max(largest, a*b)

	return largest

