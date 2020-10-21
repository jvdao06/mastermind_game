import random


# User Input functions

def difficulty_selection(filename='.\word_bank\words.txt'):
    count_possible_choices = 0
    while True:
        try:
            print("---------------------------------------------------------------------------------------------")
            word_length_choice = int(input("Choose the length of the word you would like to guess: "))

            with open(filename) as f:
                for line in f:
                    if len(line) == word_length_choice + 1:
                        count_possible_choices += 1
            # This allows the user to know the maximum possible of choices based on the size of word file, around 30,
            # 000 total words in the file.
            print('Max Possible number of valid words for the bank is: ', count_possible_choices, " for length: ",
                  word_length_choice)

            # TODO: Create better exception handling to cover wider use cases.
            if count_possible_choices <= 1:
                raise ValueError

            if len(max(open('word_bank/words.txt', 'r'), key=len)) < word_length_choice:
                raise ValueError
            break
        except(ValueError, KeyError):
            print('Invalid Input, try using a number or a valid length for words')

    while True:
        try:
            # TODO: Should check for reasonable amount of choices for the bank, anything above 10 choices seems
            #  unreasonable
            word_bank_choice = int(input("Choose the number of words you would like to in your bank: "))
            if len(open(filename).readlines()) <= word_bank_choice:
                raise ValueError
            if count_possible_choices < word_bank_choice:
                print("---------------------------------------------------------------------------------------------")
                print('Max Possible number of valid words for the bank is: ', count_possible_choices, " for length: ",
                      word_length_choice)
                raise ValueError
            break
        except(ValueError, KeyError):
            print('Invalid Input, try using a number or a valid number of inputs for your word bank.')

    word_list = []

    with open(filename) as f:
        for line in f:
            if len(line) == word_length_choice + 1:
                word_list.append(line.strip().lower())

    return word_bank_choice, word_list


def number_of_guess_selection():
    while True:
        try:
            # TODO: Added more prompts for user verification, it easy to just give yourself 1000+ chances to guess,
            #  maybe implement a recommendation
            number_of_guesses = int(input("Choose the number of guesses you would like to have: "))
            break
        except(ValueError, KeyError):
            print('Invalid Input, try using a number.')

    return number_of_guesses


# Game Driver Function
# TODO: Optimize Game Driver function to increase runtime, convert functions to modular
#  functions for endpoints on REST instead
def game_driver():
    player_input = ''
    number_of_words, word_bank = difficulty_selection()

    word_bank = random.sample(word_bank, number_of_words)

    if not word_bank:
        raise IndexError(print("Could not Generate Word Bank, error with selection."))
    secret_word = random.choice(word_bank).lower()
    number_of_guesses = number_of_guess_selection()
    guesses_made = 0
    while player_input.lower() != secret_word:
        try:
            if number_of_guesses - guesses_made == 0:
                break
            print("---------------------------------------------------------------------------------------------")

            print('Number of Guesses Remaining: ', number_of_guesses - guesses_made)
            print(word_bank, sep='\n')
            player_input = str(input("Guess the word: "))

            if player_input.lower() not in word_bank:
                raise ValueError

            matching_chars = 0
            # Check if the player's input has a matching character in the secret word
            for char in range(len(secret_word)):
                if player_input[char].lower() in secret_word:
                    matching_chars += 1
            print("Number of matching chars = ", matching_chars)

        except(ValueError, KeyError):
            # If you make an invalid guess it counts as a guess
            print('Invalid Input, try a word from the list')
        guesses_made += 1

    if player_input.lower() == secret_word:
        print("You guessed ", player_input, " and the that was the correct word. You had ",
              number_of_guesses - guesses_made, " guesses remaining.")
    else:
        print("You lost, the word was: ", secret_word)


if __name__ == "__main__":
    game_driver()
