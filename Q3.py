#input
text = input("Enter a sentence: ").strip()
if not text:
    print("Please enter a valid sentence")
else:
    words = text.split()
    total_characters = len(text)
    no_spaces = total_characters - text.count(" ")
#Results
    print(f"1.Original sentence: {text}")
    print(f"2.Total characters (with spaces): {total_characters}")
    print(f"3.Total characters (without spaces): {no_spaces}")
    print(f"4.Word count: {len(words)}")
    print(f"5.In UPPERCASE: {text.upper()}")
    print(f"6.In lowercase: {text.lower()}")
    print(f"7.In Title Case: {text.title()}")
    print(f"8.The first word is: {words[0]}")
    print(f"9.The last word is: {words[-1]}")
    print(f"10.Backward: {text[::-1]}")