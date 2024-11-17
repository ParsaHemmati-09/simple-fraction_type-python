def test_fraction_class():
    from type_fraction import fraction
    print("\n***TEST STARTED***")
    print("\n=== Testing Creation of Fractions ===")
    f1 = fraction(4, 16)  # Should represent 1/4
    f2 = fraction(1, 2)   # Should represent 1/2
    f3 = fraction(3, 4)   # Should represent 3/4
    f4 = fraction(-3, 9)  # Should represent -1/3
    
    print(f"f1: {f1}")
    print(f"f2: {f2}")
    print(f"f3: {f3}")
    print(f"f4: {f4}")

    print("\n=== Testing Simplification ===")
    f1.simplify()  # Should simplify to 1/4 
    f2.simplify()  # Should simplify to 1/2
    f4.simplify()  # Should simplify to -1/3
    
    print(f"Simplified f1: {f1}")  # Expected: 1/4
    print(f"Simplified f2: {f2}")  # Expected: 1/2
    print(f"Simplified f4: {f4}")  # Expected: -1/3

    f5 = fraction(8, -12)   # Should represent -2/3 after simplification
    f5_simple = f5.simplify(new_output=True)
    print(f"Original f5: {f5}, Simplified f5: {f5_simple}")  # Expected: 8/-12,-2/3

    print("\n=== Testing Addition ===")
    print(f"f1 + f2 = {f1.add(f2)}")  # Expected: (4 + 8) / 16 = 12/16 = 3/4
    print(f"f2 + f3 = {f2.add(f3)}")  # Expected: (2 + 3) / 4 = 10/8 = 7/8

    print("\n=== Testing Subtraction ===")
    print(f"f3 - f2 = {f3.subtract(f2)}")  # Expected: (3 - 2) / 4 = 1/4
    print(f"f2 - f1 = {f2.subtract(f1)}")  # Expected: (8 - 4) / 16 = 4/16 = 1/4

    print("\n=== Testing Multiplication ===")
    print(f"f1 * f3 = {f1.multiply(f3)}")  # Expected: (4 * 3) / (16 * 4) = 12/64 = 3/16
    print(f"f2 * f3 = {f2.multiply(f3)}")  # Expected: (1 * 3) / (2 * 4) = 3/8

    print("\n=== Testing Division ===")
    try:
        print(f"f3 / f1 = {f3.divide(f1)}")      # Expected: (3 * 16) / (4 * 4) = 48/16 = 3
        print(f"f2 / f3 = {f2.divide(f3)}")      # Expected: (1 * 4) / (2 * 3) = 4/6 = (2/3)
        zero_fraction = fraction(0,5)
        print(f"Dividing by zero test result: {f1.divide(zero_fraction)}") 
    except ValueError as e:
        print(e)

    print("\n=== Testing Root ===")
    f6 = fraction(27, 64)   # Should represent (27/64)
    print(f"Root of f6 (cube root): {f6.root(3)}")   # Expected: (3/4)

    try:
        print(f"Root of f6 (negative root): {f6.root(-2)}")   # Should raise ValueError
    except ValueError as e:
        print(e)

    print("\n=== Testing Power ===")
    print(f"Power of f2^(-1): {f2.power(-1)}")   # Expected: (2/1)

    print("\n=== Testing Comparisons ===")
    print(f"Is f1({f1}) greater than f2({f2}) ? {f1.is_greater_than(f2)}")   # Expected: False
    print(f"Is f2({f2}) less than f3({f3}) ? {f2.is_lesser_than(f3)}")       # Expected: True
    print(f"Is f4({f4}) equal to fraction(-1,3)? {f4.is_equal_to(fraction(-1,3))}")   # Expected: True

    print("\n=== Testing Mixed Fraction Representation ===")
    improper_fraction = fraction(9, 4)   # Should represent mixed number "2 1/4"
    mixed_fraction_representation = improper_fraction.to_mixed_fraction()
    print(f"Mixed fraction representation of {improper_fraction}: {mixed_fraction_representation}") 

    print("\n***TEST FINISHED SUCCESFULLY***")   # No error encountered during runtime


test_fraction_class()
