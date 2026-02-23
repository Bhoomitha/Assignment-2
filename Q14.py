num = int(input("Enter a number: "))
if num < 0:
    print("not defined enter positive number.")
elif num == 0:
    print("0! = 1")
else:
    factorial = 1
    for i in range(1, num + 1):
        factorial *= i
    print(f"The factorial of {num} is {factorial}")