from functools import reduce
import itertools
import math
import operator

def memoize(func):
	"""
	Memoization decorator for a function taking a single argument. For arguments taking more,
	consider rewriting them to take a tuple instead for performance reasons.

	See: http://code.activestate.com/recipes/578231-probably-the-fastest-memoization-decorator-in-the-/
	"""
	class memodict(dict):
		def __missing__(self, key):
			ret = self[key] = func(key)
			return ret
	return memodict().__getitem__

def product(nums):
	return reduce(operator.mul, nums, 1)

def primes_below(num):
	# Make sure num is odd. Our code expects anything in the sieve to be odd, and we want the end
	# of the sieve to represent num.
	if num % 2 == 0:
		num += 1
	limit = (num - 1) // 2

	# Index `idx` in sieve represents the primality of `2*idx + 1`.
	# TODO: I wonder if this works when the largest prime factor >= sqrt(num).
	sieve = [True] * limit
	# 1 is not prime.
	sieve[0] = False

	primes = [2]

	# Cross off multiples of primes.
	for i in range(1, limit):
		if sieve[i]:
			# Anytime we find a square that hasn't been marked off, it's prime.
			prime = 2*i + 1
			primes.append(prime)

			# Now we need to mark the multiples of the prime we just found as composite.
			multiples_count = len(sieve[i+prime:limit:prime])
			sieve[i+prime:limit:prime] = [False]*multiples_count

	return primes

@memoize
def prime_factors(num):
	divisors = itertools.chain([2], range(3, num+1, 2))
	return prime_factors_cached(num, divisors)

def prime_factors_cached(num, divisors):
	if 0 < num < 2:
		return []

	factors = []

	for prime in divisors:
		if num < 2 or prime > num:
			break

		count = 0
		while num % prime == 0:
			num //= prime
			count += 1
		if count > 0:
			factors.append((prime, count))
	return factors

def sum_digits(num):
	return sum(int(digit) for digit in str(num))
