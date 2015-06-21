
problem_text = """
Fill me in with the text from the site, verbatim.
"""

def compute_answer():
	"""
	Computes the answer to the problem's main question. This function should handle all of the
	setup it might need to do and return a single number which can be put into the site's answer
	box.
	"""
	return someNumber

# TODO: Generalize this function.
def check_given():
	expected = 0
	actual = mainFunction(someNumber)
	if actual != expected:
		return "#xyz: mainFunction(someNumber) returned {}, but expected {}".format(
			actual, expected)
	return None
