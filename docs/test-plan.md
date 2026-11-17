# Save the Watermelon - Test Plan

## Testing Results

| Test | Input | Expected Result | Actual Result | Status |
|---|---|---|---|---|
| Repeated guess | a twice | Show already guessed message, no slice lost | Already guessed message appeared | Pass |
| Invalid input | 12 | Reject input without losing a slice | Input was rejected | Pass |
| Correct guess | Letter in word | Reveal the letter | Not tested yet | Pending |
| Incorrect guess | Letter not in word | Lose one slice | Not tested yet | Pending |
| Uppercase input | A | Treat it the same as a | Not tested yet | Pending |
| Special character | @ | Reject input | Not tested yet | Pending |
| Multiple letters | abc | Reject input | Not tested yet | Pending |
| Win game | Guess all letters | Display winning message | Not tested yet | Pending |
| Lose game | Use all slices | Display losing message | Not tested yet | Pending |
| Play again | yes | Start a new game | Not tested yet | Pending |

## Summary

The game started successfully in PyCharm. I tested repeated guesses and invalid number input. Both worked correctly without taking away extra slices. I still need to finish testing the other game features.