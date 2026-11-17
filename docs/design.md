# Save the Watermelon - Design

## Problem Description
This program is a word guessing game. The computer picks a random word and the player tries to guess it one letter at a time. The goal is to figure out the word before running out of watermelon slices.

## Game Rules
The game starts by choosing a random word and hiding the letters. The player enters one letter at a time. If the letter is correct, it shows up in the word. If it is wrong, the player loses one slice. The player wins by guessing the whole word and loses when all slices are gone.

## Program Data
I will use a list to store possible words. A variable will hold the secret word. A set will keep track of letters already guessed. The program will use the secret word and guessed letters to show which letters have been revealed. Another variable will track how many slices are left.

## Program Organization
- choose_word: Picks a random word.
- show_word: Displays guessed letters and hidden letters.
- get_guess: Gets a letter from the player and checks if it is valid.
- play_game: Runs the game and checks for a win or loss.
- main: Starts the game and asks if the player wants to play again.

## Program Flow
Start → Pick random word → Hide letters → Get guess → Check guess → Update word or slices → Check win or loss → Play again or end