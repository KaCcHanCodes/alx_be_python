def safe_divide(numerator, denominator):
    try:
        num = float(numerator)
        den = float(denominator)
        if num != 0:
            return f"The result of the division is {num / den}"
        elif num == 0 or den == 0:
            raise ZeroDivisionError("Error: Cannot divide by zero.")
    except ValueError:
        return "Error: Please enter numeric values only."
    # except ZeroDivisionError as e:
    #     return print(e)
    # except Exception as e:
    #    return print(e)