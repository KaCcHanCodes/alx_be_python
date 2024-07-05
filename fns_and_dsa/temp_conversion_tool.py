FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

temp = int(input("Enter the temperature to convert: "))
unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()

def convert_to_celsius(fahrenheit):
    celsius = FAHRENHEIT_TO_CELSIUS_FACTOR * (fahrenheit - 32)
    return celsius

def convert_to_fahrenheit(celsius):
    fahrenheit = 32 + (CELSIUS_TO_FAHRENHEIT_FACTOR * celsius)
    return fahrenheit

if unit == "F":
    conversion = convert_to_celsius(temp)
    print(f"{float(temp)}°F is {conversion}°C")
elif unit == "C":
    conversion = convert_to_fahrenheit(temp)
    print(f"{float(temp)}°C is {conversion}°F")
else: print("Invalid unit")