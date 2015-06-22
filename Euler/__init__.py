import Euler.euler001
import Euler.euler002
import Euler.euler003

def main():
	for (i, problem) in enumerate([euler001, euler002, euler003], start=1):
		err = problem.check_given()
		# Should these be exceptions?
		if err:
			print(err)
		else:
			print("#{:0>3}: {}".format(i, problem.compute_answer()))
