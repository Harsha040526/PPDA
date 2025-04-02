def temperature_converter():
    print("Temperature Converter")
    temp = float(input("Enter Temperature: "))
    print("Convert to:")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    print("4. Fahrenheit to Kelvin")
    print("5. Kelvin to Fahrenheit")
    print("6. Kelvin to Celsius")
    choice = input("Enter choice (1/2/3/4/5/6): ")
    
    if choice == '1':
        fahrenheit = (temp * 9/5) + 32
        print(f"{temp}°C is {fahrenheit}°F")
    elif choice == '2':
        celsius = (temp - 32) * 5/9
        print(f"{temp}°F is {celsius}°C")
    elif choice == '3':
        kelvin = temp + 273.15
        print(f"{temp}°C is {kelvin}K")
    elif choice == '4':
        kelvin = (temp - 32) * 5/9 + 273.15
        print(f"{temp}°F is {kelvin}K")
    elif choice == '5':
        fahrenheit = (temp - 273.15) * 9/5 + 32
        print(f"{temp}K is {fahrenheit}°F")
    elif choice == '6':
        celsius = temp - 273.15
        print(f"{temp}K is {celsius}°C")
    else:
        print("Invalid Input")

temperature_converter()
