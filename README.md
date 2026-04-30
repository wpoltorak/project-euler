# Project Euler Solutions

A collection of solutions to **Project Euler** problems in Python, demonstrating clean code practices, efficient algorithms, and mathematical problem-solving techniques.

## About Project Euler

[Project Euler](https://projecteuler.net/) is a series of challenging mathematical and computer programming problems designed to require more than just mathematical insight to solve. Problems are presented in increasing difficulty and cover topics such as number theory, combinatorics, computational geometry, and more.

## Implemented Problems

| Problem | Title | Difficulty |
|---------|-------|------------|
| 1 | [Multiples of 3 or 5](https://projecteuler.net/problem=1) | Easy |
| 2 | [Even Fibonacci Numbers](https://projecteuler.net/problem=2) | Easy |
| 3 | [Largest Prime Factor](https://projecteuler.net/problem=3) | Easy |
| 4 | [Largest Palindrome Product](https://projecteuler.net/problem=4) | Easy |
| 5 | [Smallest Multiple](https://projecteuler.net/problem=5) | Easy |
| 6 | [Sum Square Difference](https://projecteuler.net/problem=6) | Easy |
| 7 | [10001st Prime](https://projecteuler.net/problem=7) | Easy |
| 8 | [Largest Product in a Series](https://projecteuler.net/problem=8) | Easy |
| 9 | [Special Pythagorean Triplet](https://projecteuler.net/problem=9) | Easy |
| 10 | [Summation of Primes](https://projecteuler.net/problem=10) | Easy |
| 12 | [Highly Divisible Triangular Number](https://projecteuler.net/problem=12) | Medium |
| 13 | [Large Sum](https://projecteuler.net/problem=13) | Easy |
| 14 | [Longest Collatz Sequence](https://projecteuler.net/problem=14) | Medium |
| 16 | [Power Digit Sum](https://projecteuler.net/problem=16) | Easy |
| 17 | [Number Letter Counts](https://projecteuler.net/problem=17) | Easy |
| 20 | [Factorial Digit Sum](https://projecteuler.net/problem=20) | Easy |

## Quick Start

### Installation

Clone the repository:

```bash
git clone https://github.com/wpoltorak/project-euler.git
cd project-euler
```

### Running Solutions

Execute the main script to solve all problems:

```bash
python main.py
```

To solve a specific problem programmatically:

```python
from main import problem1, problem2, problem3

print(problem1(1000))      # Sum of multiples of 3 or 5 below 1000
print(problem2(4000000))   # Sum of even Fibonacci numbers below 4,000,000
print(problem3(600851475143))  # Largest prime factor
```

## Testing

Run the comprehensive unit test suite:

```bash
pytest tests/test_problems.py -v
```

Tests use small input values for quick validation:

- **Problem 1**: Tested with range 10 (answer: 23)
- **Problem 3**: Tested with 13195 (answer: 29)
- **Problem 5**: Tested with LCM of 1-10 (answer: 2520)
- **Problem 14**: Tested with limit 14 (answer: 9)
- And more...

Run a specific problem's tests:

```bash
pytest tests/test_problems.py::TestProblem1 -v
```

## Key Algorithms

### Problem 1: Sum of Multiples
Simple range iteration with modulo filtering.

### Problem 3: Largest Prime Factor
Trial division optimization using square root bound.

### Problem 7: nth Prime
Prime generation using trial division with optimized candidate checking.

### Problem 10: Summation of Primes
[Sieve of Eratosthenes](https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes) - efficient algorithm for generating all primes below a limit.

### Problem 14: Longest Collatz Sequence
Dynamic sequence generation with functional programming (`max()` with key parameter).

### Problem 17: Number Letter Counts
Recursive number-to-words conversion counting letters in English representation.

## Code Quality

✅ **Type Hints**: All functions include complete type annotations  
✅ **Docstrings**: Every function has clear documentation  
✅ **Clean Code**: Readable variable names and structure  
✅ **Pythonic**: Leverages comprehensions, generators, and built-in functions  
✅ **Tested**: Comprehensive unit tests with both quick and full dataset validation  

## Performance Notes

- **Problem 14** (Collatz sequence to 1M): ~10-15 seconds
- **Problem 10** (Primes below 2M): ~2-3 seconds  
- **Problem 12** (500+ divisors): ~1-2 seconds
- All other problems complete in < 1 second

## Running Official Challenges

To solve the actual Project Euler problems with their official parameters:

```python
from main import *

# Official parameters (may take longer)
problem1(1000)              # Expected: 233168
problem10(2000000)          # Expected: 142072321
problem14(1000000)          # Expected: 837799
problem17(1000)             # Expected: 21124
problem20(100)              # Expected: 648
```

## References

- [Project Euler](https://projecteuler.net/) - Official site
- [Sieve of Eratosthenes](https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes)
- [Pythagorean Triplet](https://en.wikipedia.org/wiki/Pythagorean_triple)
- [Collatz Conjecture](https://en.wikipedia.org/wiki/Collatz_conjecture)

## License

This project is provided as-is for educational purposes.
