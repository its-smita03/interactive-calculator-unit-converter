
print("=== Interactive Calculator & Unit Converter ===")

print("\n1. Calculator")
print("2. Unit Converter")

choice = input("Choose option (1 or 2): ")
if choice == "1":
    num1 = float(input("Enter first number: "))
    operator = input("Enter operator (+, -, *, /): ")
    num2 = float(input("Enter second number: "))

    if operator == "+":
        print("Result:", num1 + num2)
    elif operator == "-":
        print("Result:", num1 - num2)
    elif operator == "*":
        print("Result:", num1 * num2)
    elif operator == "/":
        if num2 != 0:
            print("Result:", num1 / num2)
        else:
            print("Cannot divide by zero!")
    else:
        print("Invalid operator!")
elif choice == "2":
    print("\n1. Kilometer to Meter")
    print("2. Kilometer to Miles")
    print("3. Celsius to Fahrenheit")
    unit = input("Choose conversion (1, 2 or 3): ")
    value = float(input("Enter value: "))
    if unit == "1":
        print("Meters:", value * 1000)
    elif unit == "2":
        print("Miles:", value * 0.621371)
    elif unit == "3":
        print("Fahrenheit:", (value * 9/5) + 32)
    else:
        print("Invalid conversion!")
else:
    print("Invalid option!")
