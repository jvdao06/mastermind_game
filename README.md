#Mastermind
#Overview:
The goal of this exercise is to implement a command-line version of the game ‘Mastermind’.
#The Game:
The goal of mastermind is to find the “secret” word from a list of possible choices. Players should
be given a list of words of the same length and asked to pick one of the words from the provided
list for each guess. After each of the player’s guesses, the program should report the number of
letters in the correct position as the secret word. For example, if the secret word was “MIND”
and the player guessed “MEND”, the program should report “3 out of 4 letters correct” (which
are M_ND). The players should NOT be told which letters are in the correct position, only the
number of correctly positioned letters. If the correct word is guessed before the player runs out
of guesses, they win! If not, they lose. A full example game is shown below:
