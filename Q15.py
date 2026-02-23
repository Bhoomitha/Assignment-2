number = int(input("Check if this number is prime: "))
if number < 2:
    print(number, "is not a prime number.")
else:
    is_prime = True
    for factor in range(2, (number // 2) + 1):
        if number % factor == 0:
            is_prime = False
            break

    if is_prime:
        print(number, "is a PRIME number.")
    else:
        print(number, "is not a prime number.")
lower = int(input("\nEnter beginning of range: "))
upper = int(input("Enter end of range: "))

print(f"Primes between {lower} and {upper}:")

for current in range(lower, upper + 1):
    if current > 1:
        valid_prime = True
        
        for divisor in range(2, (current // 2) + 1):
            if current % divisor == 0:
                valid_prime = False
                break
        
        if valid_prime:
            print(current, end=" ")
print() 