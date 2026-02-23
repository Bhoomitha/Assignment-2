text= input("Enter: ")
original = str(text)
text1 = original.lower()
rev = text1[::-1]
print(f"Original: {original}")
print(f"Reversed: {rev}")

if text1 == rev:
    print("PALINDROME")
else:
    print("NOT A PALINDROME")