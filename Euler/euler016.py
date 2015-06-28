from Euler import utils

problem_text = """
215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 21000?
"""

def compute_answer():
	return utils.sum_digits(2 ** 1000)

def check_given():
	expected = 26
	actual = utils.sum_digits(2 ** 15)
	if actual != expected:
		return "#016: f(2 ** 15) returned {}, but expected {}.".format(actual, expected)
	return None
