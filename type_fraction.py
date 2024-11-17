import math

class fraction:
    def __init__(self, numerator, denominator):
        # Initialize the fraction with a numerator and denominator.
        # Raise an error if the denominator is zero.
        if denominator == 0:
            raise ValueError('Cannot have 0 as the denominator')
        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):
        # Return a string representation of the fraction in the form "numerator/denominator".
        return f'{self.numerator}/{self.denominator}'

    def add(self, k_x):
        # Add another fraction (k_x) to this fraction.
        if k_x.denominator == self.denominator:
            # If the denominators are the same, simply add the numerators.
            nenum = self.numerator + k_x.numerator
            return fraction(nenum, self.denominator)
        else:
            # If the denominators are different, find a common denominator and add.
            nenum = (self.numerator * k_x.denominator) + (k_x.numerator * self.denominator)
            nedenom = self.denominator * k_x.denominator
            return fraction(nenum, nedenom)

    def subtract(self, k_x):
        # Subtract another fraction (k_x) from this fraction.
        if k_x.denominator == self.denominator:
            # If the denominators are the same, simply subtract the numerators.
            nenum = self.numerator - k_x.numerator
            return fraction(nenum, self.denominator)
        else:
            # If the denominators are different, find a common denominator and subtract.
            nenum = (self.numerator * k_x.denominator) - (k_x.numerator * self.denominator)
            nedenom = self.denominator * k_x.denominator
            return fraction(nenum, nedenom)

    def multiply(self, k_x):
        # Multiply this fraction by another fraction (k_x).
        nenum = self.numerator * k_x.numerator
        nedenom = self.denominator * k_x.denominator
        return fraction(nenum, nedenom)

    def divide(self, k_x):
        # Divide this fraction by another fraction (k_x).
        if k_x.numerator == 0:
            raise ValueError("Cannot divide by zero.")
        nenum = self.numerator * k_x.denominator
        nedenom = self.denominator * k_x.numerator
        return fraction(nenum, nedenom)
    
    def root(self, r_x=2):
        # Calculate the r-th root of the fraction.
        if r_x <= 0:
            raise ValueError("Root must be a positive integer.")
        numerator_root = self.numerator ** (1/r_x)
        denominator_root = self.denominator ** (1/r_x)
        return fraction(numerator_root, denominator_root)

    def power(self, k_x):
        # Raise this fraction to the power of k_x.
        nenum = self.numerator ** k_x
        nedenom = self.denominator ** k_x
        return fraction(nenum, nedenom)

    def is_greater_than(self,fraction_x):
        # Check if this fraction is greater than another fraction (fraction_x).
        return self.to_float() > fraction_x.to_float()

    def is_lesser_than(self,fraction_x):
        # Check if this fraction is less than another fraction (fraction_x).
        return self.to_float() < fraction_x.to_float()

    def is_equal_to(self,fraction_x):
        # Check if this fraction is equal to another fraction (fraction_x).
        return self.to_float() == fraction_x.to_float()

    def simplify(self, new_output=False):
        # Simplify the fraction to its lowest terms.
        
        # Ensure that the denominator is positive.
        if self.denominator < 0:
            self.numerator = -self.numerator
            self.denominator = -self.denominator

        # Calculate the greatest common divisor (GCD) of numerator and denominator.
        gcd_value = math.gcd(abs(self.numerator), abs(self.denominator))
        
        # Divide both numerator and denominator by their GCD to simplify.
        self.numerator //= gcd_value
        self.denominator //= gcd_value

        # If new_output is True, return a new simplified fraction instead of modifying in place.
        if new_output:
            return fraction(self.numerator, self.denominator)

    def to_float(self):
        # Convert the fraction to a floating-point number.
        return self.numerator / self.denominator

    def to_mixed_fraction(self):
        # Convert the improper fraction to a mixed number format if applicable.
        
        if abs(self.numerator) >= self.denominator:
            whole_part = self.numerator // self.denominator  # Get whole number part.
            remainder = abs(self.numerator) % self.denominator  # Get remainder for fractional part.
            
            if remainder == 0:
                return str(whole_part)  # Return just the whole part if no remainder.
                
            return f'{whole_part} {remainder}/{self.denominator}'  # Return mixed number format.

        return f'{self.numerator}/{self.denominator}'  # Return simple fractional format.


