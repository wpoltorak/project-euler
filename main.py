import math


# https://projecteuler.net/

# Multiples of 3 or 5
# https://projecteuler.net/problem=1
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
# The sum of these multiples is 23. Find the sum of all the multiples of 3 or 5 below 1000.
def problem1(n):
    print(f"Sum of multiples of 3 or 5 below", n)
    multiples = 0
    for i in range(1, n):
        if (i % 3 == 0) or (i % 5 == 0):
            multiples += i
    print(multiples)


problem1(10)
problem1(1000)


# Even Fibonacci Numbers
# https://projecteuler.net/problem=2
# Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2,
# the first 10 terms will be:1, 2, 3, 5, 8, 13, 21, 34, 55, 89. By considering the terms in the Fibonacci sequence whose
# values do not exceed four million, find the sum of the even-valued terms.
def problem2(n):
    print(f"Sum of the even-valued terms of Fibonacci sequence below", n)
    sum_of_even = 0
    f1 = 0
    f = 0
    f2 = 1
    while f < n:
        f = f1 + f2
        f1, f2 = f2, f
        if f % 2 == 0:
            sum_of_even += f

    print(sum_of_even)


problem2(10)
problem2(4000000)


# Largest Prime Factor
# https://projecteuler.net/problem=3
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143?
def problem3(n):
    print(f"Largest prime factor of the number", n)
    dividend = n
    sqrtn = math.sqrt(n)
    max_prime = divisor = 2
    while divisor < sqrtn and dividend > 1:
        if dividend % divisor == 0:
            dividend = int(dividend / divisor)
            max_prime = max(divisor, max_prime)
            divisor = 2
        else:
            divisor += 1
    print(max_prime)

    # while p < sqrtn:
    #     if primes[p]:
    #         for i in range(p * p, n + 1, p):
    #             primes[i] = False
    #     p += 1
    #
    # i = n
    #
    # while not primes[i] or n % i != 0:
    #     i -= 1

    # print(i)


problem3(13195)
problem3(600851475143)


# Largest Palindrome Product
# https://projecteuler.net/problem=4
# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two -digit numbers is 9009.
# Find the largest palindrome made from the product of two 3-digit numbers.

def problem4(n):
    print(f"largest palindrome made from the product of two {n}-digit numbers.")
    max_pal = 0
    min_num = int("1" + "".join(["0"] * (n - 1)))
    max_num = int("1" + "".join(["0"] * n))
    for i in range(min_num, max_num):
        for j in range(min_num, max_num):
            prd = i * j
            str_prd = str(prd)
            if str_prd == str_prd[::-1]:
                max_pal = max(max_pal, prd)
    print(max_pal)


problem4(2)
problem4(3)


# Smallest multiple
# https://projecteuler.net/problem=5
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

def problem5(n):
    print(f"smallest positive number that is evenly divisible by all of the numbers from 1 to", n)
    dividable = 0
    num = 0
    while dividable == 0:
        num += 10
        dividable = num
        for i in range(1, n+1):
            if num % i != 0:
                dividable = 0
                break
    print(dividable)


problem5(10)
problem5(20)

# Sum Square Difference
# https://projecteuler.net/problem=6
# The sum of the squares of the first ten natural numbers is, 1^2 + 2^2 + ... + 10^2 = 385.
# The square of the sum of the first ten natural numbers is, (1 + 2 + ... + 10)^2 = 55^2 = 3025.
#
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is
# 3025 - 385 = 2640. Find the difference between the sum of the squares of the first one hundred natural numbers and
# the square of the sum.

def problem6(n):
    print(f"the difference between the sum of the squares of the first {n} natural numbers and the square of the sum", n)
    lst = range(1, n+1)
    sum_of_squares = sum(i*i for i in lst)
    square_of_sums = pow(sum(i for i in lst), 2)
    print(square_of_sums - sum_of_squares)


problem6(10)
problem6(100)