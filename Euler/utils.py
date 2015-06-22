import math

def primes_below(num):
	limit = int(math.sqrt(num)) + 1

	# Index `idx` in sieve represents the primality of `2*idx + 1`.
	# TODO: I wonder if this works when the largest prime factor >= sqrt(num).
	sieve = [True] * limit
	# 1 is not prime.
	sieve[0] = False

	primes = []

	for i in range(1, limit):
		if sieve[i]:
			prime = 2*i + 1
			primes.append(prime)
			for j in range(i + prime, limit, prime):
				sieve[j] = False

	return primes
