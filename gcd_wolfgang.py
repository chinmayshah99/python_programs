# Calculate GCD as proposed by Wolfgang Schramm
# http://emis.impa.br/EMIS/journals/INTEGERS/papers/i50/i50.pdf

# MIT License 
# Copyright (c) 2019 Chinmay Shah

import numpy as np
from math import gcd

# Returns factors of given number
def get_factors(number):
	factors = []
	for i in range(1, number+1):
		if number % i == 0:
			factors.append(i)
	return factors

# calculate Ramanujan Sum
# https://en.wikipedia.org/wiki/Ramanujan%27s_sum

def Ramanujan_sum(q, n):
	sum_no = 0
	for a in range(1, q+1):
		if gcd(a, q) == 1:  # check if it's co-prime
			sum_no = sum_no + np.exp((2 * 1j * np.pi * a * n) / q)
	return sum_no

# 
def Wolfgang_Schramm(num1, num2):
	term = 0
	num1_factors = get_factors(num1)

	for k in range(1, num1 + 1):
		term1 = np.exp((2 * np.pi * 1j * k * num2) / num1)

		term2 = 0
		for d in num1_factors:  # to check d | num1
			term2 = term2 + Ramanujan_sum(d, k)/d

		term = term + (term1 * term2)
		print(term)
	return round(np.absolute(term))


# ensure num2 > num1 to minimze computation (line 31)
print(Wolfgang_Schramm(10023, 1222321))
