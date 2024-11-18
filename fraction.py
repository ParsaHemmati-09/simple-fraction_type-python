import math

class Mixedfraction:
    def __init__(self, whole_part, numerator, denominator):
        """Initialize a mixed fraction with whole part, numerator, and denominator."""
        # Raise an error if entered values for whole part, numerator, or denominator are not integers
        if not isinstance(whole_part, int) or not isinstance(numerator, int) or not isinstance(denominator, int):
            raise ValueError("Invalid type; Please enter integers for whole part, numerator, and denominator.")
        
        # Raise an error if the denominator is zero.
        if denominator == 0:
            raise ValueError('Cannot have 0 as the denominator')
        
        # Normalize the sign so that the denominator is always positive.
        if denominator < 0:
            numerator = -numerator
            denominator = -denominator
        
        # Handle negative whole parts correctly
        if whole_part < 0:
            numerator = -abs(numerator)

        self.whole_part = whole_part
        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):
        """Return a string representation of the mixed fraction."""
        return f'{self.whole_part} {self.numerator}/{self.denominator}' if self.whole_part else f'{self.numerator}/{self.denominator}'

    def __add__(self, other):
        """Add another fraction or mixed fraction to this one."""
        other = fraction.to_fraction(other)  # Convert other to a fraction
        f1 = self.to_fraction()               # Convert this mixed fraction to a fraction
        f_final = f1 + other                  # Perform addition
        return f_final.to_mixed_fraction()    # Convert result back to mixed fraction

    def __sub__(self, other):
        """Subtract another fraction or mixed fraction from this one."""
        other = fraction.to_fraction(other)
        f1 = self.to_fraction()
        f_final = f1 - other
        return f_final.to_mixed_fraction()

    def __mul__(self, other):
        """Multiply this mixed fraction by another fraction or mixed fraction."""
        other = fraction.to_fraction(other)
        f1 = self.to_fraction()
        f_final = f1 * other
        return f_final.to_mixed_fraction()

    def __truediv__(self, other):
        """Divide this mixed fraction by another fraction or mixed fraction."""
        other = fraction.to_fraction(other)
        f1 = self.to_fraction()
        f_final = f1 / other
        return f_final.to_mixed_fraction()

    def __floordiv__(self, other):
        """Floor divide this mixed fraction by another fraction or mixed fraction."""
        other = fraction.to_fraction(other)
        f1 = self.to_fraction()
        f_final = f1 // other
        return f_final.to_mixed_fraction()

    def __pow__(self, k_x):
        """Raise this mixed fraction to the power of k_x."""
        f1 = self.to_fraction()
        f_final = f1 ** k_x
        return f_final.to_mixed_fraction()

    def __iadd__(self, other):
        """In-place addition of another fraction or mixed fraction."""
        other = fraction.to_fraction(other)
        f1 = self.to_fraction()
        f1 += other  # Update in-place
        return f1.to_mixed_fraction()

    def __isub__(self, other):
        """In-place subtraction of another fraction or mixed fraction."""
        other = fraction.to_fraction(other)
        f1 = self.to_fraction()
        f1 -= other  # Update in-place
        return f1.to_mixed_fraction()

    def __imul__(self, other):
        """In-place multiplication with another fraction or mixed fraction."""
        other = fraction.to_fraction(other)
        f1 = self.to_fraction()
        f1 *= other  # Update in-place
        return f1.to_mixed_fraction()

    def __itruediv__(self, other):
        """In-place division by another fraction or mixed fraction."""
        other = fraction.to_fraction(other)
        f1 = self.to_fraction()
        f1 /= other  # Update in-place
        return f1.to_mixed_fraction()

    def __ifloordiv__(self, other):
        """In-place floor division by another fraction or mixed fraction."""
        other = fraction.to_fraction(other)
        f1 = self.to_fraction()
        f1 //= other  # Update in-place
        return f1.to_mixed_fraction()

    def __ipow__(self, k_x):
        """In-place exponentiation of this mixed fraction."""
        f1 = self.to_fraction()
        f1 **= k_x  # Update in-place
        return f1.to_mixed_fraction()

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
        """Simplify the current mixed fraction to its lowest terms."""
        gcd_value = math.gcd(abs(self.numerator), abs(self.denominator))
        simplified_numerator = self.numerator // gcd_value
        simplified_denominator = self.denominator // gcd_value

        # Return a new Mixedfraction instance with simplified values.
        if simplified_numerator == 0:
            return Mixedfraction(self.whole_part, 0, 1)

        return Mixedfraction(self.whole_part, simplified_numerator, simplified_denominator)

    def to_float(self):
        """Convert the mixed fraction to a float representation."""
        return int(self.whole_part) + self.numerator / float(self.denominator)

    def to_fraction(self):
        """Convert the mixed fraction to an equivalent Fraction object."""
        nenum = self.numerator + (self.whole_part * self.denominator)
        return fraction(nenum, self.denominator)

    @classmethod
    def to_mixed_fraction(cls, num_x):
        """Convert an integer, float, Fraction, or Mixedfraction to a Mixedfraction."""
        if isinstance(num_x,float):  # Handle float input
            whole_part = int(num_x)
            fractional_part = num_x - whole_part

            denominator = 10000  # Use a large denominator for precision
            numerator = int(fractional_part * denominator)

            gcd_value = math.gcd(numerator, denominator)

            simplified_numerator = numerator // gcd_value
            simplified_denominator = denominator // gcd_value

            return cls(whole_part, simplified_numerator, simplified_denominator)

        elif isinstance(num_x,int):  # Handle integer input
            return cls(num_x,0,1)

        elif isinstance(num_x,fraction):  # Handle Fraction input
            whole_part = 0
            remainder = abs(num_x.numerator)

            if remainder >= num_x.denominator:
                whole_part = remainder // num_x.denominator  # Get whole number part.
                remainder %= num_x.denominator  # Get remainder for fractional part.

            return cls(whole_part, remainder, num_x.denominator)

        elif isinstance(num_x,Mixedfraction):  # Handle Mixedfraction input
            return num_x

        else:
            raise ValueError("Invalid input; must be integer/float/fraction/Mixedfraction")
            

#########################################################################################################
#########################################################################################################
#########################################################################################################

class fraction:

    def __init__(self, numerator, denominator):
        """Initialize the fraction with a numerator and denominator"""
        # Raise an error if entered values for numerator or denominator is not an integer
        if not isinstance(numerator, int) or not isinstance(denominator, int):
            raise ValueError("Invalid type; Please enter integers for both numerator and denominator.")
        
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
        """Return a string representation of the fraction in the form "numerator/denominator"""
        return f'{self.numerator}/{self.denominator}'

    def __add__(self, other):
        """In-place addition of two fractions or an integer."""
        other = fraction.to_fraction(other)
        # Update numerator and denominator in place
        self.numerator = (self.numerator * other.denominator) + (other.numerator * self.denominator)
        self.denominator *= other.denominator
        return self

    def __sub__(self, other):
        """In-place subtraction of another fraction or an integer."""
        other = fraction.to_fraction(other)
        # Update numerator and denominator in place
        self.numerator = (self.numerator * other.denominator) - (other.numerator * self.denominator)
        self.denominator *= other.denominator
        return self

    def __mul__(self, other):
        """In-place multiplication with another fraction or an integer."""
        other = fraction.to_fraction(other)
        # Update numerator and denominator in place
        self.numerator *= other.numerator
        self.denominator *= other.denominator
        return self

    def __truediv__(self, other):
        """In-place division by another fraction or an integer."""
        other = fraction.to_fraction(other)
        if other.numerator == 0:
            raise ValueError("Cannot divide by zero.")
        # Update numerator and denominator in place
        self.numerator *= other.denominator
        self.denominator *= other.numerator
        return self

    def __floordiv__(self, other):
        """Floor divide this fraction by another fraction or integer."""
        other = fraction.to_fraction(other)
        if other.numerator == 0:
            raise ValueError("Cannot divide by zero.")
        result = (self.numerator * other.denominator) // (self.denominator * other.numerator)
        return fraction(result, 1)  # Return as a new fraction.

    def __pow__(self, k_x):
        """Raise this fraction to the power of k_x."""
        nenum = self.numerator ** k_x
        nedenom = self.denominator ** k_x
        return fraction(nenum, nedenom)

    def __iadd__(self, other):
        """In-place additioin of another fraction or an integer."""
        other = fraction.to_fraction(other)
        self.numerator = (self.numerator * other.denominator) + (other.numerator * self.denominator)
        self.denominator *= other.denominator
        return self

    def __isub__(self, other):
        """In-place subtraction of another fraction or an integer."""
        other = fraction.to_fraction(other)
        self.numerator = (self.numerator * other.denominator) - (other.numerator * self.denominator)
        self.denominator *= other.denominator
        return self

    def __imul__(self, other):
        """In-place multiplication with another fraction or an integer."""
        other = fraction.to_fraction(other)
        self.numerator *= other.numerator
        self.denominator *= other.denominator
        return self

    def __itruediv__(self, other):
        """In-place division by another fraction or an integer."""
        other = fraction.to_fraction(other)
        if other.numerator == 0:
            raise ValueError("Cannot divide by zero.")
        self.numerator *= other.denominator
        self.denominator *= other.numerator
        return self

    def __ifloordiv__(self, other):
        """In-place floor division by another fraction or integer."""
        other = fraction.to_fraction(other)
        if other.numerator == 0:
            raise ValueError("Cannot divide by zero.")
        result = (self.numerator * other.denominator) // (self.denominator * other.numerator)
        self.numerator = result
        self.denominator = 1  # Reset to represent as whole number.
        return self  # Return the updated instance

    def __ipow__(self, k_x):
        """In-place exponentiation of this fraction."""
        self.numerator **= k_x
        self.denominator **= k_x
        return self

    def __gt__(self, other):
        """Check if this fraction is greater than another fraction"""
        return self.to_float() > other.to_float()

    def __lt__(self, other):
        """Check if this fraction is less than another fraction"""
        return self.to_float() < other.to_float()

    def __eq__(self, other):
        """Check if this fraction is equal to another fraction"""
        return self.to_float() == other.to_float()

    def __ge__(self, other):
        """Check if this fraction is greater than or equal to another fraction"""
        return self.to_float() >= other.to_float()

    def __le__(self, other):
        """Check if this fraction is less than or equal to another fraction"""
        return self.to_float() <= other.to_float()

    def __ne__(self, other):
        """Check if this fraction is not equal to another fraction"""
        return self.to_float() != other.to_float()

    def simplify(self):
        """Simplify the fraction to its lowest terms"""
        
        # Calculate the greatest common divisor (GCD) of numerator and denominator.
        gcd_value = math.gcd(abs(self.numerator), abs(self.denominator))
        
        # Divide both numerator and denominator by their GCD to simplify.
        simplified_numer = self.numerator // gcd_value
        simplified_denom = self.denominator // gcd_value
        
        return fraction(simplified_numer, simplified_denom)

    def to_float(self):
        """Convert the fraction to a floating-point number"""
        return self.numerator / self.denominator

    def to_mixed_fraction(self):
        """Convert this fraction to a mixed number representation"""
        
        whole_part = 0
        remainder = abs(self.numerator)

        if remainder >= self.denominator:
            whole_part = remainder // self.denominator  # Get whole number part.
            remainder %= self.denominator  # Get remainder for fractional part.

        return Mixedfraction(whole_part, remainder, self.denominator)

    @classmethod
    def to_fraction(cls, num_x):
        """Convert an integer number or floating point number to a fraction instance."""
        if isinstance(num_x, int):
            return cls(num_x, 1)
        elif isinstance(num_x, float):
            # Split the float into whole part and fractional part
            whole_part = int(num_x)
            fractional_part = num_x - whole_part
            
            # Use a large denominator for precision
            denominator = 1000000
            numerator = int(fractional_part * denominator)

            # Combine whole part with fractional part into a single numerator
            total_numerator = (whole_part * denominator) + numerator

            # Simplify the fraction before returning
            gcd_value = math.gcd(total_numerator, denominator)
            
            return cls(total_numerator // gcd_value, denominator // gcd_value)
        elif isinstance(num_x,fraction):
            return num_x
        elif isinstance(num_x,Mixedfraction):
            nenum = num_x.numerator + (num_x.whole_part * num_x.denominator)
            return cls(nenum,num_x.denominator)
        else:
            raise ValueError("Invalid input; must be integer/float/fraction/Mixedfraction")


