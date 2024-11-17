# Fraction Class

## Overview

The `fraction` class represents a mathematical fraction with a numerator and a denominator. It provides various methods for arithmetic operations, comparisons, simplification, and conversion to other representations.

## Attributes

- **numerator (int)**: The numerator of the fraction.
- **denominator (int)**: The denominator of the fraction. Must not be zero.

## Methods

### `__init__(numerator, denominator)`

Initializes a new instance of the `fraction` class.

- **Parameters**:
  - `numerator`: The numerator of the fraction.
  - `denominator`: The denominator of the fraction (must not be zero).

### `__str__()`

Returns the string representation of the fraction in the form `numerator/denominator`.

### `add(k_x)`

Adds another fraction to this fraction and returns the result.

- **Parameters**:
  - `k_x`: Another instance of the `fraction` class.
- **Returns**: A new `fraction` instance representing the sum.

### `subtract(k_x)`

Subtracts another fraction from this fraction and returns the result.

- **Parameters**:
  - `k_x`: Another instance of the `fraction` class.
- **Returns**: A new `fraction` instance representing the difference.

### `multiply(k_x)`

Multiplies this fraction by another fraction and returns the result.

- **Parameters**:
  - `k_x`: Another instance of the `fraction` class.
- **Returns**: A new `fraction` instance representing the product.

### `divide(k_x)`

Divides this fraction by another fraction and returns the result.

- **Parameters**:
  - `k_x`: Another instance of the `fraction` class.
- **Returns**: A new `fraction` instance representing the quotient.
- **Raises**: ValueError if attempting to divide by zero.

### `root(r_x=2)`

Returns the nth root of the fraction.

- **Parameters**:
  - `r_x`: The root to calculate (default is 2).
- **Returns**: A new `fraction` instance representing the root.
- **Raises**: ValueError if r_x is not a positive integer.

### `power(k_x)`

Raises the fraction to the power of k_x.

- **Parameters**:
  - `k_x`: The exponent to raise the fraction.
- **Returns**: A new `fraction` instance representing the result.

### Comparison Methods

- **`is_greater_than(fraction_x)`**: Checks if this fraction is greater than another fraction.
- **`is_lesser_than(fraction_x)`**: Checks if this fraction is less than another fraction.
- **`is_equal_to(fraction_x)`**: Checks if this fraction is equal to another fraction.

### `simplify()`

Simplifies the fraction to its lowest terms.

### `to_float()`

Converts the fraction to a float representation.

### `to_mixed_fraction()`

Converts the fraction to a mixed number representation if applicable.

## Examples

```python
# Creating fractions
f1 = fraction(1, 2)
f2 = fraction(3, 4)

# Adding fractions
result_add = f1.add(f2)
print(result_add)  # Output: 10/8 or simplified version

# Subtracting fractions
result_subtract = f1.subtract(f2)
print(result_subtract)  # Output: -2/8 or simplified version

# Multiplying fractions
result_multiply = f1.multiply(f2)
print(result_multiply)  # Output: 3/8

# Dividing fractions
result_divide = f1.divide(f2)
print(result_divide)  # Output: 4/6 or simplified version

# Checking equality
is_equal = f1.is_equal_to(fraction(2, 4))
print(is_equal)  # Output: True

# Simplifying a fraction
f3 = fraction(8, -12)
f3.simplify()
print(f3)  # Output: -2/3

# Converting to float
float_value = f1.to_float()
print(float_value)  # Output: 0.5

# Converting to mixed number
f4 = fraction(10,3)
mixed_fraction = f4.to_mixed_fraction()
print(mixed_fraction)  # Output: 3 1/3


