import math

class MixedFraction:
    def __init__(self, numerator, denominator, whole_part):
        self.numerator = numerator
        self.denominator = denominator
        self.whole_part = whole_part

    def __str__(self):
        # String representation of the mixed fraction.
        return f'{self.whole_part} {self.numerator}/{self.denominator}' if self.whole_part else f'{self.numerator}/{self.denominator}'

    def __add__(self, other):
        pass

    def __sub__(self, other):
        pass

    def __mul__(self, other):
        pass

    def __truediv__(self, other):
        pass
    
    def __floordiv__(self, other):
        pass

    def __pow__(self, k_x):
        pass

    def __iadd__(self, other):
        pass

    def __isub__(self, other):
        pass

    def __imul__(self, other):
        pass

    def __itruediv__(self, other):
        pass

    def __ifloordiv__(self, other):
        pass

    def __ipow__(self, k_x):
        pass

    def root(self, r_x=2):
        pass

    def __gt__(self, other):
        # Check if this mixed fraction is greater than another mixed fraction.
        return self.to_float() > other.to_float()

    def __lt__(self, other):
        # Check if this mixed fraction is less than another mixed fraction.
        return self.to_float() < other.to_float()

    def __eq__(self, other):
        # Check if this mixed fraction is equal to another mixed fraction.
        return self.to_float() == other.to_float()

    def __ge__(self, other):
        # Check if this mixed fraction is greater than or equal to another mixed fraction.
        return self.to_float() >= other.to_float()

    def __le__(self, other):
        # Check if this mixed fraction is less than or equal to another mixed fraction.
        return self.to_float() <= other.to_float()

    def __ne__(self, other):
        # Check if this mixed fraction is not equal to another mixed fraction.
        return self.to_float() != other.to_float()

    def simplify(self):
        pass

    def to_float(self):
        # Convert the fraction to a floating-point number.
        return int(whole_part) + self.numerator / self.denominator

    def to_fraction(self):
        # Convert this mixed fraction to a fully fractional representation.
        pass

    @classmethod
    def float_to_fraction(cls, fl_x):
        # Convert a floating-point number to a MixedFraction instance.
        pass

###########################################################################


class Fraction:
    def __init__(self, numerator, denominator):
        # Initialize the fraction with a numerator and denominator.
        # Raise an error if the denominator is zero.
        if denominator == 0:
            raise ValueError('Cannot have 0 as the denominator')
        
        # Normalize the sign so that the denominator is always positive.
        if denominator < 0:
            numerator = -numerator
            denominator = -denominator
            
        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):
        # Return a string representation of the fraction in the form "numerator/denominator".
        return f'{self.numerator}/{self.denominator}'

    def __add__(self, other):
        # Add two fractions.
        # Calculate a new numerator and denominator for the result.
        nenum = (self.numerator * other.denominator) + (other.numerator * self.denominator)
        nedenom = self.denominator * other.denominator
        return Fraction(nenum, nedenom)

    def __sub__(self, other):
        # Subtract one fraction from another.
        # Calculate a new numerator and denominator for the result.
        nenum = (self.numerator * other.denominator) - (other.numerator * self.denominator)
        nedenom = self.denominator * other.denominator
        return Fraction(nenum, nedenom)

    def __mul__(self, other):
        # Multiply two fractions.
        # The new numerator is the product of the numerators,
        # and the new denominator is the product of the denominators.
        nenum = self.numerator * other.numerator
        nedenom = self.denominator * other.denominator
        return Fraction(nenum, nedenom)

    def __truediv__(self, other):
        # Divide this fraction by another fraction.
        # Raises an error if attempting to divide by zero.
        if other.numerator == 0:
            raise ValueError("Cannot divide by zero.")
        
        # The new numerator is this fraction's numerator multiplied by the other fraction's denominator,
        # and the new denominator is this fraction's denominator multiplied by the other fraction's numerator.
        nenum = self.numerator * other.denominator
        nedenom = self.denominator * other.numerator
        return Fraction(nenum, nedenom)
    
    def __floordiv__(self, other):
        # Perform floor division between two fractions.
        if other.numerator == 0:
            raise ValueError("Cannot divide by zero.")
        
        # Calculate the result of floor division
        result = (self.numerator * other.denominator) // (self.denominator * other.numerator)
        
        # Return the result as a Fraction
        return Fraction(result, 1)

    def __pow__(self, k_x):
        # Raise this fraction to the power of k_x.
        nenum = self.numerator ** k_x
        nedenom = self.denominator ** k_x
        return Fraction(nenum, nedenom)

    def __iadd__(self, other):
        # In-place addition of two fractions.
        self.numerator = (self.numerator * other.denominator) + (other.numerator * self.denominator)
        self.denominator *= other.denominator
        return self

    def __isub__(self, other):
        # In-place subtraction of one fraction from another.
        self.numerator = (self.numerator * other.denominator) - (other.numerator * self.denominator)
        self.denominator *= other.denominator
        return self

    def __imul__(self, other):
        # In-place multiplication of two fractions.
        self.numerator *= other.numerator
        self.denominator *= other.denominator
        return self 

    def __itruediv__(self, other):
        # In-place division of this fraction by another fraction.
        if other.numerator == 0:
            raise ValueError("Cannot divide by zero.")
        
        self.numerator *= other.denominator
        self.denominator *= other.numerator
        return self

    def __ifloordiv__(self, other):
        # Perform in-place floor division between two fractions.
        if other.numerator == 0:
            raise ValueError("Cannot divide by zero.")
        
        result = (self.numerator / self.denominator) // (other.numerator / other.denominator)
        
        # Update this fraction to represent the result as an improper fraction.
        self.numerator = int(result)
        self.denominator = 1
        return self  # Return the updated instance

    def __ipow__(self, k_x):
        # Raise this fraction to the power of k_x in place.
        self.numerator **= k_x
        self.denominator **= k_x
        return self

    def root(self, r_x=2):
        # Calculate the r-th root of this fraction.
        # Raises an error if r_x is not a positive integer.
        if r_x <= 0:
            raise ValueError("Root must be a positive integer.")
        
        numerator_root = self.numerator ** (1/r_x)
        denominator_root = self.denominator ** (1/r_x)
        return Fraction(numerator_root, denominator_root)

    def __gt__(self, other):
        # Check if this fraction is greater than another fraction.
        return self.to_float() > other.to_float()

    def __lt__(self, other):
        # Check if this fraction is less than another fraction.
        return self.to_float() < other.to_float()

    def __eq__(self, other):
        # Check if this fraction is equal to another fraction.
        return self.to_float() == other.to_float()

    def __ge__(self, other):
        # Check if this fraction is greater than or equal to another fraction.
        return self.to_float() >= other.to_float()

    def __le__(self, other):
        # Check if this fraction is less than or equal to another fraction.
        return self.to_float() <= other.to_float()

    def __ne__(self, other):
        # Check if this fraction is not equal to another fraction.
        return self.to_float() != other.to_float()

    def simplify(self):
        # Simplify the fraction to its lowest terms.
        
        # Calculate the greatest common divisor (GCD) of numerator and denominator.
        gcd_value = math.gcd(abs(self.numerator), abs(self.denominator))
        
        # Divide both numerator and denominator by their GCD to simplify.
        simplified_numer = self.numerator // gcd_value
        simplified_denom = self.denominator // gcd_value
        
        return Fraction(simplified_numer, simplified_denom)

    def to_float(self):
        # Convert the fraction to a floating-point number.
        return self.numerator / self.denominator

    def to_mixed_fraction(self):
        # Convert this fraction to a mixed number representation.
        
        whole_part = 0
        remainder = abs(self.numerator)

        if remainder >= self.denominator:
            whole_part = remainder // self.denominator  # Get whole number part.
            remainder %= self.denominator  # Get remainder for fractional part.

        return MixedFraction(remainder, self.denominator, whole_part)

    @classmethod
    def float_to_fraction(cls, fl_x):
        # Convert a floating-point number to a Fraction instance.
        
        whole_part = int(fl_x)
        fractional_part = fl_x - whole_part
        
        # Arbitrarily large denominator for precision.
        denominator = 10000
        
        numerator = int(fractional_part * denominator)
        
        # Simplify the fraction part if necessary.
        gcd_value = math.gcd(numerator, denominator)
        
        return cls(numerator // gcd_value + whole_part*denominator//gcd_value , denominator//gcd_value )



