from functools import reduce
import math
import operator

def product(nums):
	return reduce(operator.mul, nums, 1)

def primes_below(num):
	limit = num

	# Index `idx` in sieve represents the primality of `2*idx + 1`.
	# TODO: I wonder if this works when the largest prime factor >= sqrt(num).
	sieve = [True] * limit
	# 1 is not prime.
	sieve[0] = False

	primes = [2]

	for i in range(1, num):
		if sieve[i]:
			prime = 2*i + 1
			primes.append(prime)
			for j in range(i + prime, limit, prime):
				sieve[j] = False

	return primes

def prime_factors(num):
	count = 0
	while num % 2 == 0:
		num //= 2
		count += 1

	factors = [(2, count)]
	# While this isn't strickly prime, it will be if it enters the while loop,
	# because if it's not prime, it has a prime factor that's already gone through the loop.
	for prime in range(3, int(math.sqrt(num) + 1), 2):
		count = 0
		while num % prime == 0:
			num //= prime
			count += 1
		if count != 0:
			factors.append((prime, count))

	return factors


