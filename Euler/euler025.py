from itertools import takewhile

problem_text = """
The Fibonacci sequence is defined by the recurrence relation:

    Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.

Hence the first 12 terms will be:

    F1 = 1
    F2 = 1
    F3 = 2
    F4 = 3
    F5 = 5
    F6 = 8
    F7 = 13
    F8 = 21
    F9 = 34
    F10 = 55
    F11 = 89
    F12 = 144

The 12th term, F12, is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
"""

def compute_answer():
	return first_fib_above(10 ** 999) # First 1000-digit number.

def check_given():
	expected = 12
	actual = first_fib_above(10 ** 2) # First 3-digit number.
	if actual != expected:
		return "#025: Found {}, but expected {}".format(
			actual, expected)
	return None

def first_fib_above(above):
	fib_gen = fibonacci()

	idx, fib = 0, 0
	while fib <= above:
		idx, fib = next(fib_gen)

	return idx

def fibonacci(limit=None):
	a, b, = 1, 0

	# Hard code the first value.
	yield (0, 0)
	idx = 1

	while True:
		a, b = a + b, a
		idx += 1
		yield (idx, a)

given = [
	# 10 ** 2 is the first 3-digit number, 10 ** 3 - 1 the last.
	(12, first_fib_above(10 ** 2)),
]
