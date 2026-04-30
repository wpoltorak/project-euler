# Project Euler Solutions

A collection of solutions to **Project Euler** problems in Python, demonstrating clean code practices, efficient algorithms, and mathematical problem-solving techniques.

## About Project Euler

[Project Euler](https://projecteuler.net/) is a series of challenging mathematical and computer programming problems designed to require more than just mathematical insight to solve. Problems are presented in increasing difficulty and cover topics such as number theory, combinatorics, computational geometry, and more.


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

Run a specific problem's tests:

```bash
pytest tests/test_problems.py::TestProblem1 -v
```

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
