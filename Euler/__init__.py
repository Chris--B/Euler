import importlib
import time

def main():
	times = []

	wall_start = time.clock()
	for (i, problem) in solved_problems():
		# Should these be exceptions?
		err = problem.check_given()
		if err:
			print(err)
			continue

		start = time.clock()

		solution = problem.compute_answer()

		end = time.clock()
		times.append(end - start)

		print("#{:0>3}: {:<15} ({}) {}"
		      .format(i, solution, format_time(times[-1]), check_solution(i, solution)))

	wall_end = time.clock()
	print()
	print("Wall    ", format_time(wall_end - wall_start))
	print("Problems", format_time(sum(times)))

def solved_problems(problems=None):
	"""
	Import modules of the form Euler.euler###, where ### is a three digit number with zero padding.
	If it cannot find the module, it will silently skip it.

	Return a generator of tuples - the problem number and the module object.

	If `problems` is not None, then it is iterated over and only those problems are imported
	and yielded. Otherwise, it is as if range(1, 1000) was passed.

	For example, `list(solved_problems()) == [(2, <module object>), (27, <module object>)]`
	when only problems 2 and 27 have been solved.

	Or, `list(solved_problems([2, 27])) == [(2, <module object>), (27, <module object>)]`
	if at least problems 2 and 27 have been solved.
	"""

	if problems is None:
		# It will be a long while before Project Euler breaks 1000 problems.
		# e.g.:
		#   Project Euler launched in 2001,
		#   Problem 522 is due to be published on June 27th, 2015
		# Go backwards, so that the newest problem is displayed first.
		problems = range(999, 0, -1)

	for problem in problems:
		problem_str = "Euler.euler{:03d}".format(problem)
		try:
			yield (problem, importlib.import_module(problem_str))
		# We couldn't find the module, but maybe we just skipped this one? Keep going.
		except ImportError as e:
			# CPython and Pypy have *slightly* different error messages.
			# Other implementations might have different ones.
			# TODO: Investigate and maybe base this check on substrings.
			# e.g. check for "no module" and "Euler.euler[0-9]{3}".
			# Also, relying on error message syntax is likely not stable.
			if str(e).startswith("No module named 'Euler.euler") \
			   or str(e).startswith("No module named Euler.euler"):
				continue
			raise e

def format_time(time):
	"""
	Return a string "### unit", where ### is a space-padded 3-digit number (usually) and "unit" is one of:
	s, ms, us, ns, representing seconds, milliseconds, microseconds, and nanoseconds.

	If time is > 1, "s" is used and padding may be overwritten if time >= 1000.
	If time > 1e-3, then it is multiplied by 1e3 and rounded to the nearest integer.
	If time > 1e-6, likewise.
	Otherwise, it is multiplied by 1e9 and rounded. Sub-nanosecond labels don't make sense for our
	application (timing Python code), so they are not supported.
	"""

	if time > 1:
		return "{:>3} s".format(int(time + 0.5))
	elif time > 1e-3:
		return "{:>3} ms".format(int(time * 1e3 + 0.5))
	elif time > 1e-6:
		return "{:>3} us".format(int(time * 1e6 + 0.5))
	else:
		return "{:>3} ns".format(int(time * 1e9 + 0.5))

def check_solution(problem, answer):
	"""
	Verify whether or not `answer` is the correct solution to problem #`problem`.
	If it is, return an empty string.
	If it is not, return a string to print. e.g. "Expected ###", where ### is the actual solution.
	If no data for the problem can be found, return a string saying so.
	"""
	for (known_problem, solution) in known_solutions:
		if known_problem == problem:
			if answer != solution:
				return "Expected {}".format(solution)
			return ""
	return "(Unverified)"

# A list of known solutions, added to after the problem is solved but before the commit.
known_solutions = [
	(1, 233168),
	(2, 4613732),
	(3, 6857),
	(4, 906609),
	(5, 232792560),
	(6, 25164150),
	(7, 104743),
	(8, 23514624000),
	(9, 31875000),
	(10, 142913828922),
	(11, 70600674),
	(12, 76576500),
	(13, 5537376230),
	(14, 837799),
	(16, 1366),
	(15, 137846528820),
]
