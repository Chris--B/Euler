
problem_text = """
Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
"""

def compute_answer():
	return sum_even_fibonacci(4e6)

def check_given():
	# This wasn't given to us verbatim, but it should suffice nonetheless.
	expected = sum(num for num in [1, 2, 3, 5, 8, 13, 21, 34, 55, 89] if num % 2 == 0)
	actual = sum_even_fibonacci(90)

	if actual != expected:
		return "#002: sum_even_fibonacci(90) expected {expected}, but returned {actual}".format(
			**vars())

	return None

def sum_even_fibonacci(below):
	total = 0

	for num in fibonacci(below):
		if num % 2 == 0:
			total += num

	return total

def fibonacci(below):
	yield 0

	if below <= 1:
		return

	a, b = 1, 0
	while a < below:
		a, b = a + b, a
		yield b
