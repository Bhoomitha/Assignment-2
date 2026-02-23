#input
year = int(input("Enter a year: "))
# Leap Year Check
if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    print(year, "is a Leap Year.")
    print("It follows the leap year rule.")
else:
    print(year, "is NOT a Leap Year.")
    print("It does not follow the leap year rule.")