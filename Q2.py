#input
n1 = float(input("Enter first number: "))
n2 = float(input("Enter second number: "))
#Calculations with results
print("\nResults:")
print(f"{n1} + {n2} = {n1 + n2}")
print(f"{n1} - {n2} = {n1 - n2}")
print(f"{n1} * {n2} = {n1 * n2}")
if n2 != 0:
    print(f"{n1} / {n2} = {n1 / n2:.2f}")
else:
    print(f"{n1} / {n2} = Error (Cannot divide by zero)")
print(f"{n1} % {n2} = {n1 % n2}")
print(f"{n1} ^ {n2} = {n1 ** n2}")