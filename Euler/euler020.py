from Euler import utils
import math

problem_text = """
n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
"""

def compute_answer():
	return utils.sum_digits(math.factorial(100))

# TODO: Generalize this function.
def check_given():
	expected = 27
	actual = utils.sum_digits(math.factorial(10))
	if actual != expected:
		return "#020: f(10) returned {}, but expected {}".format(actual, expected)
	return None
