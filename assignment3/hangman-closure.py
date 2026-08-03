#task4:
def make_hangman(secret_word):
    guesses = []

    def hangman_closure(letter):
        guesses.append(letter)
        display_word = ""
        for character in secret_word:
            if character in guesses:
                display_word += character
            else:
                display_word += "_"

        print(display_word)
        if "_" not in display_word:
            return True
        else:
            return False

    return hangman_closure

secret_word = input("Enter the secret word: ")

hangman = make_hangman(secret_word)

word_guessed = False

while not word_guessed:
    letter = input("Guess a letter: ")

    word_guessed = hangman(letter)

print("You guessed the word!")