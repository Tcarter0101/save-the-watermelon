# Save the Watermelon - Pseudocode

START PROGRAM

Create a list of possible words

REPEAT
    Pick a random word from the list
    Set remaining slices to 6
    Create an empty collection for guessed letters

    WHILE slices remain
        Display the word with unguessed letters hidden
        Display remaining slices
        Ask the player to guess one letter

        Change the guess to lowercase

        IF the guess is not exactly one letter
            Display an invalid input message
            Continue to the next guess

        IF the letter was already guessed
            Display an already guessed message
            Continue to the next guess

        Add the letter to guessed letters

        IF the letter is in the secret word
            Reveal every matching letter
            Display a correct guess message
        ELSE
            Subtract one slice
            Display an incorrect guess message
        END IF

        IF every letter has been guessed
            Display the completed word
            Display a winning message
            Stop the current game
        END IF
    END WHILE

    IF no slices remain and the word is incomplete
        Display a losing message
        Show the secret word
    END IF

    Ask the player if they want to play again

UNTIL the player chooses not to play again

Display a goodbye message

END PROGRAM