
problem_text = """
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

def sum_mults_3_or_5(below):
	total = 0
	for num in range(below):
		if num % 3 == 0 or num % 5 == 0:
			total += num
	return total

def compute_answer():
	return sum_mults_3_or_5(1000)

given = [
	(23, sum_mults_3_or_5(10)),
]
