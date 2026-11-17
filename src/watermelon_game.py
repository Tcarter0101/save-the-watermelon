import random


def choose_word():
    """Pick a random word."""
    words = ["watermelon", "apple", "banana", "orange", "grape"]
    return random.choice(words)


def show_word(word, guessed):
    """Show the letters the player has guessed."""
    display = ""
    for letter in word:
        if letter in guessed:
            display += letter + " "
        else:
            display += "_ "
    return display


def get_guess(guessed):
    """Get a valid letter from the player."""
    while True:
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter one letter.")
        elif guess in guessed:
            print("You already guessed that letter.")
        else:
            return guess


def play_game():
    """Play one round of the game."""
    word = choose_word()
    guessed = set()
    slices = 6

    print("Welcome to Save the Watermelon!")

    while slices > 0:
        print("\nWord:", show_word(word, guessed))
        print("Slices left:", slices)

        guess = get_guess(guessed)
        guessed.add(guess)

        if guess in word:
            print("Good guess!")
        else:
            slices -= 1
            print("Wrong guess! You lost a slice.")

        if all(letter in guessed for letter in word):
            print("You win! The word was", word)
            return

    print("You lost! The word was", word)


def main():
    """Start the game and allow replay."""
    while True:
        play_game()

        again = input("Play again? (yes/no): ").lower()

        if again != "yes":
            print("Thanks for playing!")
            break


main()