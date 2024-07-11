def safe_divide(numerator, denominator):
    float(numerator), float(denominator)
    try:
        if numerator == 0 or denominator == 0:
            raise ZeroDivisionError("Error: Cannot divide by zero.")
        else:
            result = print(f"The result of the division is {numerator / denominator}")
            return result
    except ValueError:
        print("Error: Please enter numeric values only.")