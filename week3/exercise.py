#!/usr/bin/env python

# Week 3 Exercises: Functions

# EXERCISE 1:

# Implement FizzBuzz using function(s) with Clean Code standards

# -----FIZZBUZZ CODE HERE-----
def FIZZBUZZ(num):
    if (num % 3 == 0) & (num % 5 == 0):
        result = 'Fizz Buzz'
    elif num % 3 == 0:
        result = 'Fizz'
    elif num % 5 == 0:
        result = 'Buzz'
    else:
        result = num
    return result

# test code for FIZZBUZZ
for num in range(1, 17):
    result = FIZZBUZZ(num)
    print result

# -----END FIZBUZZ CODE-----

# EXERCISE 2:

# Review the payroll.java code in Listing 3-4 in the book

# Re-implement it as clean Python code. See Listing 3-5 for guidance.

# -----PAYROLL CODE HERE-----


# -----END PAYROLL CODE-----
