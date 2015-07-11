
from .__main__ import main, check_solution
__all__ = ["utils", "main", "check_solution"]

def __load_euler_modules():
	"""
	Loads the euler modules of form euler###, where ### are any three digits,
	and appends them on to __all__.

	Any exceptions encountered when importing are passed up to the caller,
	except ones which which resulted from a particular euler module not being
	found. Those are ignored.
	"""
	import importlib
	# Export any euler### modules it can find within Euler.
	for problem in range(1, 1000):
		module_name = "Euler.euler{:03d}".format(problem)
		try:
			vars()[module_name] = importlib.import_module(module_name)
			__all__.append(module_name)
		except ImportError as e:
			if str(e).startswith("No module named 'Euler.euler") \
			   or str(e).startswith("No module named Euler.euler"):
				continue
			raise e

__load_euler_modules()
