import time

import Euler.euler001
import Euler.euler002
import Euler.euler003
import Euler.euler004

def main():
	times = []

	for (i, problem) in enumerate([euler001, euler002, euler003, euler004], start=1):
		start = time.clock()
		err = problem.check_given()
		end = time.clock()
		times.append(end - start)
		# Should these be exceptions?
		if err:
			print(err)
		else:
			print(
				"#{:0>3}: {:<10} ({})".format(i, problem.compute_answer(), format_time(times[-1])))

	print()
	print("Total", format_time(sum(times)))
	print("Ave  ", format_time(sum(times) / i))

def format_time(time):
	if time > 1:
		return "{:>3} s".format(int(time + 0.5))
	elif time > 1e-3:
		return "{:>3} ms".format(int(time * 1e3 + 0.5))
	elif time > 1e-6:
		return "{:>3} us".format(int(time * 1e6 + 0.5))
	# This kind of resolution in a language like Python is hardly meaningful.
	elif time > 1e-8:
		return "{:>3} ns".format(int(time * 1e9 + 0.5))
	else:
		return "Barely any time at all."
