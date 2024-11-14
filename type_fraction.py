import math

class fraction:
    
    """
    A class to represent a mathematical fraction.

    Attributes:
        numerator (int): The numerator of the fraction.
        denominator (int): The denominator of the fraction. Must not be zero.

    Methods:
        __str__(): Returns the string representation of the fraction.
        add(k_x): Adds another fraction to this fraction and returns the result.
        subtract(k_x): Subtracts another fraction from this fraction and returns the result.
        multiply(k_x): Multiplies this fraction by another fraction and returns the result.
        divide(k_x): Divides this fraction by another fraction and returns the result.
        root(r_x=2): Returns the nth root of the fraction.
        power(k_x): Raises the fraction to the power of k_x.
        is_greater_than(fraction_x): Checks if this fraction is greater than another fraction.
        is_lesser_than(fraction_x): Checks if this fraction is less than another fraction.
        is_equal_to(fraction_x): Checks if this fraction is equal to another fraction.
        simplify(): Simplifies the fraction to its lowest terms.
        to_float(): Converts the fraction to a float representation.
        to_mixed_fraction(): Converts the fraction to a mixed number representation if applicable.
    """

    def __init__(self, numerator, denominator):
        if denominator == 0:
            raise ValueError('Cannot have 0 as the denominator')
        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):
        return f'{self.numerator}/{self.denominator}'

    def add(self, k_x):
        if k_x.denominator == self.denominator:
            nenum = self.numerator + k_x.numerator
            return fraction(nenum, self.denominator)
        else:
            nenum = (self.numerator * k_x.denominator) + (k_x.numerator * self.denominator)
            nedenom = self.denominator * k_x.denominator
            return fraction(nenum, nedenom)

    def subtract(self, k_x):
        if k_x.denominator == self.denominator:
            nenum = self.numerator - k_x.numerator
            return fraction(nenum, self.denominator)
        else:
            nenum = (self.numerator * k_x.denominator) - (k_x.numerator * self.denominator)
            nedenom = self.denominator * k_x.denominator
            return fraction(nenum, nedenom)

    def multiply(self, k_x):
        nenum = self.numerator * k_x.numerator
        nedenom = self.denominator * k_x.denominator
        return fraction(nenum, nedenom)

    def divide(self, k_x):
        if k_x.numerator == 0:
            raise ValueError("Cannot divide by zero.")
        nenum = self.numerator * k_x.denominator
        nedenom = self.denominator * k_x.numerator
        return fraction(nenum, nedenom)
    
    def root(self, r_x=2):
        if r_x <= 0:
            raise ValueError("Root must be a positive integer.")
        numerator_root = self.numerator ** (1/r_x)
        denominator_root = self.denominator ** (1/r_x)
        return fraction(numerator_root, denominator_root)

    def power(self, k_x):
        nenum = self.numerator ** k_x
        nedenom = self.denominator ** k_x
        return fraction(nenum, nedenom)

    def is_greater_than(self,fraction_x):
        return self.to_float() > fraction_x.to_float()

    def is_lesser_than(self,fraction_x):
        return self.to_float() < fraction_x.to_float()

    def is_equal_to(self,fraction_x):
        return self.to_float() == fraction_x.to_float()

    def simplify(self):
        if self.denominator < 0:
            self.numerator = -self.numerator
            self.denominator = -self.denominator
            
        gcd_value = math.gcd(abs(self.numerator), abs(self.denominator))
        self.numerator //= gcd_value
        self.denominator //= gcd_value

    def to_float(self):
        return self.numerator / self.denominator

    def to_mixed_fraction(self):
        if abs(self.numerator) >= self.denominator:
            whole_part = self.numerator // self.denominator
            remainder = abs(self.numerator) % self.denominator
            if remainder == 0:
                return str(whole_part)
            return f'{whole_part} {remainder}/{self.denominator}'
        return f'{self.numerator}/{self.denominator}'


###TEST###
from test_fraction import test_fraction_class
test_fraction_class()