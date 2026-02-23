txt = input("Enter text: ")
words = txt.split()
print("Words:", len(words))
vowels ="aeiouAEIOU"
v = 0
c = 0
for char in txt:
    if char in vowels:
        v = v+1
    elif char.isalpha():
        c =c+ 1
print("Vowels:", v)
print("Consonants:", c)
print("Reverse:", txt[::-1])
clean = txt.replace(" ", "").lower()
if clean == clean[::-1]:
    print("Palindrome-Yes")
else:
    print("Palindrome-No")
new_txt = ""
for ch in txt:
    if ch not in vowels:
        new_txt += ch
print("Without vowels:", new_txt)
long = ""
for w in words:
    if len(w) > len(long):
        long = w
print("Longest word:", long)
freq = {}
for w in words:
    w = w.lower()
    if w in freq:
        freq[w] += 1
    else:
        freq[w] = 1
print("Word frequency:", freq)