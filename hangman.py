name = input("What is your name?")

print("Hello " + name, "Time to play Hangman")

word = "delicious"

guesses = ""

turns = 5

while turns > 0:
    failed = 0
    for char in word:
        if char in guesses:
            print(char)
        else:
            print("_")
            failed = failed + 1
    if failed == 0:
        print("You won!")
        break
    guess = input("guess a character:")

    guesses += guess
    if guess not in word:
        turns -= 1
        print("Wrong!")
        print("You have", + turns, "turns left")
        if turns == 0:
            print("You lose!")