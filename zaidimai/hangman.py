import random


def hangman():
    with open('words.txt', 'r') as file:
        word_list = file.read().split()
    if not word_list:
        print('Error: no words in file.')
        return
    secret_word = random.choice(word_list).lower()
    correct_letters = set()
    incorrect_letters = set()
    MAX_TRIES = 7

    while len(incorrect_letters) < MAX_TRIES:
        display_word = ''.join(letter if letter in correct_letters else '_' for letter in secret_word)
        print(display_word)
        if display_word == secret_word:
            print('You win!')
            break

        guess = input('Guess a letter: ').lower()
        if len(guess) != 1:
            print('Please enter a single letter.')
            continue
        if guess in correct_letters or guess in incorrect_letters:
            print('You already guessed that letter.')
            continue
        if guess in secret_word:
            correct_letters.add(guess)
        else:
            incorrect_letters.add(guess)
            print(f'That letter is not in the word. You have {MAX_TRIES - len(incorrect_letters)} guesses left.')

    else:
        print(f'Sorry, you lose. The word was "{secret_word}".')


if __name__ == '__main__':
    hangman()
