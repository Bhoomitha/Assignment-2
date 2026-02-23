print("PATTERN PRINTER")
print("1) Pattern 1")
print("2) Pattern 2")
print("3) Pattern 3")
print("4) Pattern 4")
pick = int(input("Select a design (1-4): "))
size = int(input("Set the vertical height: "))
if pick == 1:
    for row in range(1, size + 1):
        for col in range(1, row + 1):
            print(col, end=" ")
        print()
elif pick == 2:
    for row in range(1, size + 1):
        for col in range(row):
            print(row, end=" ")
        print()
elif pick == 3:
    for row in range(size, 0, -1):
        for col in range(row, 0, -1):
            print(col, end=" ")
        print()
elif pick == 4:
    for row in range(1, size + 1):
        for up in range(1, row + 1):
            print(up, end="")
        for down in range(row - 1, 0, -1):
            print(down, end="")
        print()
else:
    print("Selection outside of range.")