import math

# https://projecteuler.net/

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Multiples of 3 or 5
def problem1(n):
    print(f"Sum of multiples of 3 or 5 below ", n)
    multiples = 0
    for i in range(1, n):
        if (i % 3 == 0) or (i % 5 == 0):
            multiples += i
    print(multiples)


problem1(10)
problem1(1000)


# Even Fibonacci Numbers

def problem2(n):
    print(f"Sum of the even-valued terms of Fibonacci sequence below ", n)
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

def problem3(n):
    print(f"Largest prime factor of the number ", n)
    # p = 2
    dividend = n
    sqrtn = math.sqrt(n)
    max_prime = divisor = 2
    while divisor < sqrtn and dividend > 1:
        if dividend % divisor == 0:
            num = int(dividend / divisor)
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
def problem4(n):
    print(n)