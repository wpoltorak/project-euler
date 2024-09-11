# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import math


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')


# See PyCharm help at https://www.jetbrains.com/help/pycharm/

# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
# See PyCharm help at https://www.jetbrains.com/help/pycharm/


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
    primes = [True for i in range(n + 1)]
    p = 2

    while p * p < n:
        if primes[p]:
            for i in range(p * p, n + 1, p):
                primes[i] = False
        p += 1
    i = n
    while not primes[i]:
        i -= 1
    print(i)


problem3(13195)
