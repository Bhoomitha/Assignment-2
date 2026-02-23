def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if b == 0:
        return "Error!"
    return a / b
def modulus(a, b):
    return a % b
def power(a, b):
    return a ** b
def calculator():
    while True:
        print("CALCULATOR")
        print("1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Modulus\n6. Power")
        choice = input("\nChoose an operation (1-6): ")
        if choice in ['1', '2', '3', '4', '5', '6']:
            try:
                n1 = float(input("Enter first number: "))
                n2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input! Please enter numbers only.")
                continue
            if choice == '1':
                print(f"Result: {add(n1, n2)}")
            elif choice == '2':
                print(f"Result: {subtract(n1, n2)}")
            elif choice == '3':
                print(f"Result: {multiply(n1, n2)}")
            elif choice == '4':
                print(f"Result: {divide(n1, n2)}")
            elif choice == '5':
                print(f"Result: {modulus(n1, n2)}")
            elif choice == '6':
                print(f"Result: {power(n1, n2)}")
        else:
            print("Invalid choice.")
calculator()