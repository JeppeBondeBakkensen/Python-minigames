import random


def generated_number():
    return random.randint(1, 100)


def get_user_input():
    while True:
        try:
            user_guess = int(input("Guess a number between 1 - 100: "))
            return user_guess
        except ValueError:
            print("Invalid input! Please enter a valid number.")


def main():
    number_to_guess = generated_number()
    allready_guessed = set()
    number_of_guesses = 0
    print("Welcom to my guessing game ")
    print("Try to guess the number i am thinking of. Type 0 to quit the game")

    while True:
        guess = get_user_input()
        if guess == 0:
            print(f"Thank you for playing. The number i was thinking of was {
                  number_to_guess}")
            break

        if guess in allready_guessed:
            print(f"You have allready guessed {guess}. Try again")
            continue

        allready_guessed.add(guess)
        number_of_guesses += 1

        if guess > number_to_guess:
            print("You guess is to high. Try again")
        elif guess < number_to_guess:
            print("Your guess is to low. Try again")
        else:
            print(f"You guessed my number {number_to_guess} in {
                  number_of_guesses} attemps")
            break


if __name__ == "__main__":
    main()
