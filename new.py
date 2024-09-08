import random
from words import word_list
from display import display_hangman


def get_words():
    word = random.choice(word_list)
    return word.upper()

def play(word):
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = [] 
    tries = 7
    print("Let's play hangman")
    print(display_hangman(tries))
    print(word_completion)
    print("\n")
    while not guessed and tries > 0:
        guess = input("Guess a letter or word: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed that letter:", guess)
            elif guess not in word:
                print("Guess is not in the word")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("Good job")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if '_' not in word_completion:
                    guessed = True
                
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("You already guessed the word", guess)
            elif guess != word:
                print("Incorrect")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        
        else:
            print("Not a valid guess")
        
        print(display_hangman(tries))
        print(word_completion)
        print("\n")
        
    if guessed:
        print("You win!")
    else:
        print("Game over. The word was:", word)

def main():
    word = get_words()
    play(word)
    while input("Play again? (Y/N): ").upper() == "Y":
        word = get_words()
        play(word)
        
        
if __name__ == "__main__":
    main()
