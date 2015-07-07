
from .__main__ import main, check_solution
__all__ = ["utils"]

def __load_euler_modules():
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
