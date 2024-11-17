import math

class MixedFraction:
    def __init__(self, whole_part, numerator, denominator):
        """Initialize a mixed fraction with whole part, numerator, and denominator."""
        self.numerator = numerator
        self.denominator = denominator
        self.whole_part = whole_part

    def __str__(self):
        """Return a string representation of the mixed fraction."""
        return f'{self.whole_part} {self.numerator}/{self.denominator}' if self.whole_part else f'{self.numerator}/{self.denominator}'

    def __add__(self, other):
        """Add two mixed fractions."""
        newhole = self.whole_part + other.whole_part
        nenum = (self.numerator * other.denominator) + (other.numerator * self.denominator)
        nedenom = self.denominator * other.denominator
        return MixedFraction(newhole, nenum, nedenom)

    def __sub__(self, other):
        """Subtract another mixed fraction from this one."""
        newhole = self.whole_part - other.whole_part
        nenum = (self.numerator * other.denominator) - (other.numerator * self.denominator)
        nedenom = self.denominator * other.denominator
        return MixedFraction(newhole, nenum, nedenom)

    def __mul__(self, other):
        """Multiply this mixed fraction by another."""
        f1 = self.to_fraction()
        f2 = other.to_fraction()
        f_final = f1 * f2
        return f_final.to_mixed_fraction()

    def __truediv__(self, other):
        """Divide this mixed fraction by another."""
        f1 = self.to_fraction()
        f2 = other.to_fraction()
        f_final = f1 / f2
        return f_final.to_mixed_fraction()

    def __floordiv__(self, other):
        """Floor divide this mixed fraction by another."""
        f1 = self.to_fraction()
        f2 = other.to_fraction()
        f_final = f1 // f2
        return f_final.to_mixed_fraction()

    def __pow__(self, k_x):
        """Raise this mixed fraction to the power of k_x."""
        f1 = self.to_fraction()
        f_final = f1 ** k_x
        return f_final.to_mixed_fraction()

    def __iadd__(self, other):
        """In-place addition of another mixed fraction."""
        f1 = self.to_fraction()
        f2 = other.to_fraction()
        f1 += f2
        return f1.to_mixed_fraction()

    def __isub__(self, other):
        """In-place subtraction of another mixed fraction."""
        f1 = self.to_fraction()
        f2 = other.to_fraction()
        f1 -= f2
        return f1.to_mixed_fraction()

    def __imul__(self, other):
        """In-place multiplication with another mixed fraction."""
        f1 = self.to_fraction()
        f2 = other.to_fraction()
        f1 *= f2
        return f1.to_mixed_fraction()

    def __itruediv__(self, other):
        """In-place division by another mixed fraction."""
        f1 = self.to_fraction()
        f2 = other.to_fraction()
        f1 /= f2
        return f1.to_mixed_fraction()

    def __ifloordiv__(self, other):
        """In-place floor division by another mixed fraction."""
        f1 = self.to_fraction()
        f2 = other.to_fraction()
        f1 //= f2
        return f1.to_mixed_fraction()

    def __ipow__(self, k_x):
       """In-place exponentiation of this mixed fraction."""
       f1 = self.to_fraction()  
       f1 **= k_x  
       return f1.to_mixed_fraction()

    def root(self, r_x=2):
       """Calculate the r-th root of this mixed fraction."""
       if r_x <= 0:
           raise ValueError("Root must be a positive integer.")
       # Logic to calculate the root would go here.
       # Placeholder for actual implementation.
       pass

    def __gt__(self, other):
         """Check if this mixed fraction is greater than another."""
         return self.to_float() > other.to_float()

    def __lt__(self, other):
         """Check if this mixed fraction is less than another."""
         return self.to_float() < other.to_float()

    def __eq__(self, other):
         """Check if this mixed fraction is equal to another."""
         return self.to_float() == other.to_float()

    def __ge__(self, other):
         """Check if this mixed fraction is greater than or equal to another."""
         return self.to_float() >= other.to_float()

    def __le__(self, other):
         """Check if this mixed fraction is less than or equal to another."""
         return self.to_float() <= other.to_float()

    def __ne__(self, other):
         """Check if this mixed fraction is not equal to another."""
         return self.to_float() != other.to_float()

    def simplify(self):
         """Simplify the fractional part of this mixed number."""
         gcd_value = math.gcd(abs(self.numerator), abs(self.denominator))
         simplified_numerator = self.numerator // gcd_value
         simplified_denominator = self.denominator // gcd_value
        
         if simplified_numerator == 0:
             return MixedFraction(self.whole_part, 0, 0)
         
         return MixedFraction(self.whole_part,simplified_numerator, simplified_denominator)

    def to_float(self):
         """Convert the entire mixed number into a floating-point number."""
         return int(self.whole_part) + self.numerator / float(self.denominator)

    def to_fraction(self):
         """Convert this mixed number into an improper Fraction representation."""
         nenum = self.numerator + (self.whole_part * self.denominator)
         return Fraction(nenum,self.denominator)

    @classmethod
    def float_to_mixed_fraction(cls, fl_x):
         """Convert a floating-point number into a MixedFraction instance."""
         whole_part = int(fl_x)
         fractional_part = fl_x - whole_part
        
         denominator = 10000  # Use large denominator for precision
         numerator = int(fractional_part * denominator)
        
         gcd_value = math.gcd(numerator, denominator)
        
         # Return new instance with simplified values.
         return cls(numerator // gcd_value + whole_part * denominator // gcd_value , denominator // gcd_value)

###########################################################################

class Fraction:
    def __init__(self, numerator, denominator):
        '''Initialize the fraction with a numerator and denominator'''
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
        '''Return a string representation of the fraction in the form "numerator/denominator"'''
        return f'{self.numerator}/{self.denominator}'

    def __add__(self, other):
        '''Adds two fractions together'''
        # Calculate a new numerator and denominator for the result.
        nenum = (self.numerator * other.denominator) + (other.numerator * self.denominator)
        nedenom = self.denominator * other.denominator
        return Fraction(nenum, nedenom)


    def __sub__(self, other):
        '''Subtract one fraction from another'''
        # Calculate a new numerator and denominator for the result.
        nenum = (self.numerator * other.denominator) - (other.numerator * self.denominator)
        nedenom = self.denominator * other.denominator
        return Fraction(nenum, nedenom)

    def __mul__(self, other):
        '''Multiply two fractions by each other. The new numerator is the product of the numerators and the new denominator is the product of the denominators'''
        nenum = self.numerator * other.numerator
        nedenom = self.denominator * other.denominator
        return Fraction(nenum, nedenom)

    def __truediv__(self, other):
        '''Divide this fraction by another fraction'''
        # Raises an error if attempting to divide by zero.
        if other.numerator == 0:
            raise ValueError("Cannot divide by zero.")
        
        # The new numerator is this fraction's numerator multiplied by the other fraction's denominator,
        # and the new denominator is this fraction's denominator multiplied by the other fraction's numerator.
        nenum = self.numerator * other.denominator
        nedenom = self.denominator * other.numerator
        return Fraction(nenum, nedenom)
    
    def __floordiv__(self, other):
        '''Perform floor division between two fractions'''
        if other.numerator == 0:
            raise ValueError("Cannot divide by zero.")
        
        # Calculate the result of floor division
        result = (self.numerator * other.denominator) // (self.denominator * other.numerator)
        
        # Return the result as a Fraction
        return Fraction(result, 1)

    def __pow__(self, k_x):
        '''Raise this fraction to the power of k_x'''
        nenum = self.numerator ** k_x
        nedenom = self.denominator ** k_x
        return Fraction(nenum, nedenom)

    def __iadd__(self, other):
        '''In-place addition of two fractions'''
        self.numerator = (self.numerator * other.denominator) + (other.numerator * self.denominator)
        self.denominator *= other.denominator
        return self

    def __isub__(self, other):
        '''In-place subtraction of one fraction from another'''
        self.numerator = (self.numerator * other.denominator) - (other.numerator * self.denominator)
        self.denominator *= other.denominator
        return self

    def __imul__(self, other):
        '''In-place multiplication of two fractions'''
        self.numerator *= other.numerator
        self.denominator *= other.denominator
        return self 

    def __itruediv__(self, other):
        '''In-place division of this fraction by another fraction'''
        if other.numerator == 0:
            raise ValueError("Cannot divide by zero.")
        
        self.numerator *= other.denominator
        self.denominator *= other.numerator
        return self

    def __ifloordiv__(self, other):
        '''Perform in-place floor division between two fractions'''
        if other.numerator == 0:
            raise ValueError("Cannot divide by zero.")
        
        result = (self.numerator / self.denominator) // (other.numerator / other.denominator)
        
        # Update this fraction to represent the result as an improper fraction.
        self.numerator = int(result)
        self.denominator = 1
        return self  # Return the updated instance

    def __ipow__(self, k_x):
        '''Raise this fraction to the power of k_x in place'''
        self.numerator **= k_x
        self.denominator **= k_x
        return self

    def root(self, r_x=2):
        '''Calculate the r-th root of this fraction'''
        # Raises an error if r_x is not a positive integer.
        if r_x <= 0:
            raise ValueError("Root must be a positive integer.")
        
        numerator_root = self.numerator ** (1/r_x)
        denominator_root = self.denominator ** (1/r_x)
        return Fraction(numerator_root, denominator_root)

    def __gt__(self, other):
        '''Check if this fraction is greater than another fraction'''
        return self.to_float() > other.to_float()

    def __lt__(self, other):
        '''Check if this fraction is less than another fraction'''
        return self.to_float() < other.to_float()

    def __eq__(self, other):
        '''Check if this fraction is equal to another fraction'''
        return self.to_float() == other.to_float()

    def __ge__(self, other):
        '''Check if this fraction is greater than or equal to another fraction'''
        return self.to_float() >= other.to_float()

    def __le__(self, other):
        '''Check if this fraction is less than or equal to another fraction'''
        return self.to_float() <= other.to_float()

    def __ne__(self, other):
        '''Check if this fraction is not equal to another fraction'''
        return self.to_float() != other.to_float()

    def simplify(self):
        '''Simplify the fraction to its lowest terms'''
        
        # Calculate the greatest common divisor (GCD) of numerator and denominator.
        gcd_value = math.gcd(abs(self.numerator), abs(self.denominator))
        
        # Divide both numerator and denominator by their GCD to simplify.
        simplified_numer = self.numerator // gcd_value
        simplified_denom = self.denominator // gcd_value
        
        return Fraction(simplified_numer, simplified_denom)

    def to_float(self):
        '''Convert the fraction to a floating-point number'''
        return self.numerator / self.denominator

    def to_mixed_fraction(self):
        '''Convert this fraction to a mixed number representation'''
        
        whole_part = 0
        remainder = abs(self.numerator)

        if remainder >= self.denominator:
            whole_part = remainder // self.denominator  # Get whole number part.
            remainder %= self.denominator  # Get remainder for fractional part.

        return MixedFraction(remainder, self.denominator, whole_part)

    @classmethod
    def float_to_fraction(cls, fl_x):
        '''Convert a floating-point number to a Fraction instance'''
        
        whole_part = int(fl_x)
        fractional_part = fl_x - whole_part
        
        # Arbitrarily large denominator for precision.
        denominator = 10000
        
        numerator = int(fractional_part * denominator)
        
        # Simplify the fraction part if necessary.
        gcd_value = math.gcd(numerator, denominator)
        
        return cls(numerator // gcd_value + whole_part*denominator//gcd_value , denominator//gcd_value )


