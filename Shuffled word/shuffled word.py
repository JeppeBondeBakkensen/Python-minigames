import random

word_list = [
    "blomster", "fiskeri", "vandring", "klipper", "solskin",
    "håndværk", "fuglsang", "kuglepen", "studenter", "mødelokale",
    "lufthavn", "skrivebord", "arbejdsmiljø", "jernbane", "havemøbler",
    "fællesskab", "billedkunst", "fugleliv", "solnedgang", "cykelsport"
]

# Shuffle the letters in the chosen word
def shuffle_word(chosen_word):
    shuffled_letters = random.sample(chosen_word, len(chosen_word))
    shuffled_text = "".join(shuffled_letters)
    return shuffled_text

# User guess, what the shuffled word is
def user_guess(shuffled_word):
    user_input = input(f"Which word is hidden behind {shuffled_word}? ")
    return user_input

# After each guess this tells the user, what index that are correct
def correct_indices(user_input, chosen_word):
    user_input_list = []
    chosen_word_list = []
    correct_positions = []

    for char in user_input:
        user_input_list.append(char)

    for char in chosen_word:
        chosen_word_list.append(char)

    for user_index, user_char in enumerate(user_input_list):
        for word_index, word_char in enumerate(chosen_word_list):
            if (user_char == word_char) and (user_index == word_index):
                correct_positions.append(str(user_index + 1))

    correct_guess = ", ".join(correct_positions)
    print(f"Position(s) {correct_guess} is/are correct")

# After 3 guesses the program ask the user if they want a hint
def hint(correct_word):
    while True:
        try:
            want_hint = int(input("Press 1 for a hint, else press 0: "))
            if want_hint == 1:
                return print(f"The first 3 letters of the word are: {correct_word[:3]}")
            elif want_hint == 0:
                user_guess()
            else:
                print("Enter 1 or 0")
        except ValueError:
            print("Invalid input! Please enter a valid number.")


def main():
    guess_count = 0
    random_word = random.choice(word_list)
    shuffled = shuffle_word(random_word)
    print(random_word)  # For debugging
    while True:
        guess_count += 1
        user_input = user_guess(shuffled)
        correct_indices(user_input, random_word)
        if user_input == random_word:
            print(f"Well done! You found the word {
                  random_word} in {guess_count} attempts.")
            break
        elif guess_count >= 3:
            hint(random_word)
        else:
            print("Try again")


if __name__ == "__main__":
    main()
