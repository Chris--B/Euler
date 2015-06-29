from Euler import utils
import math
import os

problem_text = """
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
"""

NAMES_FILE = os.path.join(os.path.dirname(__file__), "resources/p022_names.txt")

def compute_answer():
	names = load_names_file(NAMES_FILE)

	return sum(calc_name_score(idx, name) for (idx, name) in enumerate(names))

def check_given():
	# These are given in the project description. index is an INDEX, not the position.
	name_idx = 937
	name = "COLIN"

	names = load_names_file(NAMES_FILE)
	if names[name_idx] != name:
		print("Expected {}, but found {} at index {}".format(
			name, names[name_idx], name_idx))

	expected = 49714
	actual = calc_name_score(name_idx, names[name_idx])

	if actual != expected:
		return "#022: Found {}, but expected {}".format(actual, expected)
	return None

def calc_name_score(idx, name):
	# The position is 1 indexed, but arrays in Python are 0-indexed.
	return (idx+1) * sum(ord(letter) - ord("A") + 1 for letter in name)

def load_names_file(filename):
	with open(filename) as fi:
		names = fi.read().split(",")
		# Strip out the quotes.
		names = [name[1:-1] for name in names]
	names.sort()
	return names
