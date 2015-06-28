from functools import reduce
import math
import operator

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

def prime_factors(num):
	factors = []

	# Hard code a check for 2, since it's the only even prime.
	count = 0
	while num % 2 == 0:
		num //= 2
		count += 1
	if count > 0:
		factors.append((2, count))

	# While this isn't strictly prime, it will be if it enters the while loop,
	# because if it's not prime, it has a prime factor that's already gone through the loop.
	for prime in range(3, num+1, 2):
		if num <= 1:
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

