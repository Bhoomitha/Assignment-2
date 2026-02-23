# Temperature Convertion
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")
print("3. Celsius to Kelvin")
print("4. Kelvin to Celsius")
print("5. Fahrenheit to Kelvin")
print("6. Kelvin to Fahrenheit")

choice = input("Select an option (1-6): ")

temp = float(input("Enter temperature value: "))

# Conversion Logic
if choice == '1':
    result = (temp * 9/5) + 32
    print(f"{temp}C = {result:.2f}F")
elif choice == '2':
    result = (temp - 32) * 5/9
    print(f"{temp}F = {result:.2f}C")
elif choice == '3':
    result = temp + 273.15
    print(f"{temp}C = {result:.2f}K")
elif choice == '4':
    result = temp - 273.15
    print(f"{temp}K = {result:.2f}C")
elif choice == '5':
    result = (temp - 32) * 5/9 + 273.15
    print(f"{temp}F = {result:.2f}K")
elif choice == '6':
    result = (temp - 273.15) * 9/5 + 32
    print(f"{temp}K = {result:.2f}F")