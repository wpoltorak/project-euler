"""
Unit tests for Project Euler solutions.

Tests use smaller input values to run quickly while validating the correctness
of the algorithms. Expected results are verified against known Project Euler
answers or mathematical calculations.
"""

import pytest
from main import (
    problem1, problem2, problem3, problem4, problem5, problem6, problem7,
    problem8, problem9, problem10, problem12, problem13, problem14, problem16,
    problem17, problem20
)


class TestProblem1:
    """Problem 1: Multiples of 3 or 5"""

    def test_small_range(self):
        """Test with range 10 (answer: 3+5+6+9 = 23)"""
        assert problem1(10) == 23

    def test_single_multiple(self):
        """Test with range 5"""
        assert problem1(5) == 3  # Only 3

    def test_official(self):
        """Test with Project Euler parameter"""
        assert problem1(1000) == 233168


class TestProblem2:
    """Problem 2: Even Fibonacci Numbers"""

    def test_small_limit(self):
        """Test with limit 10"""
        # Fibonacci: 1, 2, 3, 5, 8, 13...
        # Even: 2, 8
        assert problem2(10) == 10

    def test_larger_limit(self):
        """Test with limit 100"""
        # Even Fibonacci numbers below 100: 2, 8, 34
        assert problem2(100) == 44

    def test_official(self):
        """Test with Project Euler parameter"""
        assert problem2(4000000) == 4613732


class TestProblem3:
    """Problem 3: Largest Prime Factor"""

    def test_example_from_problem(self):
        """Test with 13195 (answer: 29)"""
        assert problem3(13195) == 29

    def test_prime_number(self):
        """Test with prime (answer: itself)"""
        assert problem3(17) == 17

    def test_official(self):
        """Test with Project Euler parameter"""
        assert problem3(600851475143) == 6857


class TestProblem4:
    """Problem 4: Largest Palindrome Product"""

    def test_1_digit_numbers(self):
        """Test with 1-digit numbers (1-9)"""
        # Largest palindrome: 9 * 9 = 81 (not palindrome), 7*1=7, etc.
        assert problem4(1) > 0

    def test_2_digit_numbers(self):
        """Test with 2-digit numbers (10-99)"""
        # Largest palindrome: 9009 = 91 * 99
        assert problem4(2) == 9009

    def test_official(self):
        """Test with Project Euler parameter (3-digit numbers)"""
        assert problem4(3) == 906609


class TestProblem5:
    """Problem 5: Smallest Multiple"""

    def test_small_range(self):
        """Test finding LCM of 1-10 (answer: 2520)"""
        assert problem5(10) == 2520

    def test_smaller(self):
        """Test finding LCM of 1-5 (answer: 60)"""
        assert problem5(5) == 60

    def test_official(self):
        """Test with Project Euler parameter"""
        assert problem5(20) == 232792560


class TestProblem6:
    """Problem 6: Sum Square Difference"""

    def test_small_range(self):
        """Test with first 10 natural numbers"""
        # Sum of squares: 385
        # Square of sum: 3025
        # Difference: 2640
        assert problem6(10) == 2640

    def test_first_three(self):
        """Test with first 3 numbers"""
        # Sum of squares: 14, Square of sum: 36, Difference: 22
        assert problem6(3) == 22

    def test_official(self):
        """Test with Project Euler parameter"""
        assert problem6(100) == 25164150


class TestProblem7:
    """Problem 7: 10001st Prime"""

    def test_6th_prime(self):
        """Test 6th prime (answer: 13)"""
        assert problem7(6) == 13

    def test_10th_prime(self):
        """Test 10th prime (answer: 29)"""
        assert problem7(10) == 29

    def test_official(self):
        """Test with Project Euler parameter"""
        assert problem7(10001) == 104743


class TestProblem8:
    """Problem 8: Largest Product in a Series"""

    def test_4_adjacent_digits(self):
        """Test with 4 adjacent digits"""
        assert problem8(4) == 5832

    def test_official(self):
        """Test with Project Euler parameter (13 adjacent digits)"""
        assert problem8(13) == 23514624000


class TestProblem9:
    """Problem 9: Special Pythagorean Triplet"""

    def test_small_sum(self):
        """Test with sum 12 (triplet: 3, 4, 5)"""
        # 3^2 + 4^2 = 5^2 and 3 + 4 + 5 = 12
        assert problem9(12) == 60

    def test_official(self):
        """Test with Project Euler parameter"""
        assert problem9(1000) == 31875000


class TestProblem10:
    """Problem 10: Summation of Primes"""

    def test_small_limit(self):
        """Test primes below 10 (2+3+5+7 = 17)"""
        assert problem10(10) == 17

    def test_limit_100(self):
        """Test sum of primes below 100"""
        assert problem10(100) == 1060

    def test_official(self):
        """Test with Project Euler parameter"""
        assert problem10(2000000) == 142072321


class TestProblem12:
    """Problem 12: Highly Divisible Triangular Number"""

    def test_5_divisors(self):
        """Test first triangle number with 5+ divisors"""
        # 28 = 1+2+3+4+5+6+7 has divisors: 1,2,4,7,14,28 (6 divisors)
        assert problem12(5) == 28

    def test_official(self):
        """Test with Project Euler parameter (500+ divisors)"""
        assert problem12(500) == 76576500


class TestProblem13:
    """Problem 13: Large Sum"""

    def test_first_10_digits(self):
        """Test extracting first 10 digits of sum"""
        result = problem13(10)
        assert 5537376230 == result


class TestProblem14:
    """Problem 14: Longest Collatz Sequence"""

    def test_small_limit(self):
        """Test with limit 14 (answer: 9, chain length 20)"""
        assert problem14(14) == 9

    def test_limit_1000(self):
        """Test with limit 1000"""
        result = problem14(1000)
        assert result > 0
        assert result < 1000

    def test_official(self):
        """Test with Project Euler parameter (may take ~10-15 seconds)"""
        assert problem14(1000000) == 837799


class TestProblem16:
    """Problem 16: Power Digit Sum"""

    def test_power_15(self):
        """Test 2^15 = 32768, digit sum = 3+2+7+6+8 = 26"""
        assert problem16(15) == 26

    def test_power_100(self):
        """Test 2^100"""
        assert problem16(100) == 115

    def test_official(self):
        """Test with Project Euler parameter"""
        assert problem16(1000) == 1366


class TestProblem17:
    """Problem 17: Number Letter Counts"""

    def test_small_range(self):
        """Test with numbers 1-5"""
        # one(3) + two(3) + three(5) + four(4) + five(4) = 19
        assert problem17(5) == 19

    def test_range_to_1000(self):
        """Test with numbers 1-1000"""
        # This is the official Project Euler answer
        result = problem17(1000)
        assert result == 21124


class TestProblem20:
    """Problem 20: Factorial Digit Sum"""

    def test_small_factorial(self):
        """Test 10! = 3628800, digit sum = 27"""
        assert problem20(10) == 27

    def test_factorial_5(self):
        """Test 5! = 120, digit sum = 3"""
        assert problem20(5) == 3

    def test_official(self):
        """Test with Project Euler parameter"""
        assert problem20(100) == 648
