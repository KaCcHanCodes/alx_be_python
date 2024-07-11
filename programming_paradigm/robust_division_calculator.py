def safe_divide(numerator, denominator):
    num = float(numerator)
    den = float(denominator)
    try:
        if num == 0 or den == 0:
            raise ZeroDivisionError("Error: Cannot divide by zero.")
        else:
            result = num / den
            print(f"The result of the division is {result}")
    except ValueError:
        print("Error: Please enter numeric values only.")