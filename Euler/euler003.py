import math

problem_text = """
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

def compute_answer():
	return largest_prime_factor(600851475143)

def check_given():
	expected = 29
	actual = largest_prime_factor(13195)
	if actual != expected:
		return "#003: prime_factors(13195) returned {}, but expected {}.".format(actual, expected)
	return None

def calc_primes(below):
	limit = int(math.sqrt(below)) + 1

	# Index `idx` in sieve represents the primality of `2*idx + 1`.
	# TODO: I wonder if this works when the largest prime factor >= sqrt(below).
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

def prime_factors(num):
	primes = calc_primes(num)
	return [prime for prime in primes if num % prime == 0]

def largest_prime_factor(num):
	return prime_factors(num)[-1]
