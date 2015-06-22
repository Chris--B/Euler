
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
	largest = 10 ** digits - 1
	def palindromes():
		# Larger factors usually means larger number. Start the search at 99...9 and go down.
		for a in range(largest, 0, -1):
			for b in range(largest, 0, -1):
				string = str(a*b)
				if string == string[::-1]:
					yield a*b

	return max(palindromes())

