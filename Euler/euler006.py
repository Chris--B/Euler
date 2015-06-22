
problem_text = """
The sum of the squares of the first ten natural numbers is,

1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)^2 = 55^2 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""

def compute_answer():
	return sum_square_diff(100)

def check_given():
	expected = 2640
	actual = sum_square_diff(10)
	if actual != expected:
		return "#006: f(10) returned {}, but expected {}".format(actual, expected)
	return None

def sum_square_diff(limit):
	sum_squares = sum(num*num for num in range(limit+1))
	square_sum = sum(range(limit+1)) ** 2
	return square_sum - sum_squares
