from Euler import utils

problem_text = """
The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:

 1: 1
 3: 1,3
 6: 1,2,3,6
10: 1,2,5,10
15: 1,3,5,15
21: 1,3,7,21
28: 1,2,4,7,14,28
We can see that 28 is the first triangle number to have over five divisors.

What is the value of the first triangle number to have over five hundred divisors?
"""

def compute_answer():
	return first_triangle_with_divisors(500)

def check_given():
	expected = 28
	actual = first_triangle_with_divisors(5)
	if actual != expected:
		return "#012: f(5) returned {}, but expected {}".format(actual, expected)
	return None

def first_triangle_with_divisors(count):
	num = 1
	tri_num = 1
	while True:
		if count_factors(tri_num) >= count:
			return tri_num
		num += 1
		tri_num += num


def count_factors(num):
	pfactors = utils.prime_factors(num)
	return utils.product(power+1 for (_, power) in pfactors)

