import random
top_score = 100
while True:
    secret_num = random.randint(1, 100)
    lives = 7
    tries = 0
    win = False
    print("\nnew game")
    print("thinking")
    if top_score < 100:
        print("record:", top_score)
    while tries < lives:
        user_input = input("\nEnter your guess: ")
        if not user_input.isdigit():
            print("Please enter a valid number!")
            continue
        guess = int(user_input)
        tries = tries + 1
        if guess == secret_num:
            print("CONGRATULATIONS! You guessed the number in", tries, "tries!")
            win = True
            if tries < top_score:
                print("WOW! New record!")
                top_score = tries
            break
        if guess < secret_num:
            print("LOW!")
        else:
            print("HIGH!")
        print("Attempts remaining:", lives - tries)
    if win == False:
        print("\nGAME OVER!.")
        print("The number was:", secret_num)
    ch = input("\nDo you want to play again? (y/n): ")
    if ch != "y" and ch != "Y":
        print("Thanks for playing! Final Best Score:", top_score)
        break