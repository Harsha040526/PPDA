def calculator():
    print("Simple Calculator")
    num1 = float(input("Enter first number:"))
    num2 = float(input("Enter second number:"))
    print("Select operation:")
    print("1. Add")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Divide")
    print("5. Modulus")
    print("6. Exponentation")
    print("7. Floor Division")
    choice = input("Enter input(1-7):")
    if choice == '1':
        print(f"Result: {num1} + {num2} = {num1 + num2}")
    elif choice == '2':
        print(f"Result: {num1} - {num2} = {num1 - num2}")
    elif choice == '3':
        print(f"Result: {num1} * {num2} = {num1 * num2}")
    elif choice == '4':
        if num2 != 0:
            print(f"Result: {num1} / {num2} = {num1 / num2}")
        else:
            print("Error! Division by 0")
    elif choice == '5':
        print(f"Result: {num1} % {num2} = {num1 % num2}")
    elif choice == '6':
        print(f"Result: {num1} ** {num2} = {num1 ** num2}")
    elif choice == '7':
        print(f"Result: {num1} // {num2} = {num1 // num2}")
    else:
        print("Invalid Input")

calculator()
