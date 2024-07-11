def safe_divide(numerator, denominator):
    try:
        num = float(numerator)
        den = float(denominator)
        if num == 0 or den == 0:
            raise ZeroDivisionError("Error: Cannot divide by zero.")
        else:
            return f"The result of the division is {num / den}"
    except ValueError:
        return "Error: Please enter numeric values only."
    except ZeroDivisionError as e:
        return e
    except Exception as e:
       return e