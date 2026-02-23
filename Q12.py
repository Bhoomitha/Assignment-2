num = int(input("Enter number: "))
limit = int(input("Enter range (end): "))
print(f"\nMultiplication Table of {num}")
for i in range(1, limit + 1):
    result = num * i
    print(f"{num} x {i} = {result}")
