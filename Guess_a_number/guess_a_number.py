import random


def welcome():
    print("Welcome to my guessing game!")
    print("Try to guess the number I am thinking of. Type 0 to quit the game.")


def dificulty():
    while True:
        try:
            level = int(input(
                "What level do you want to play? Press 1 for beginner, 2 for advanced, 3 for expert: "))
            if level == 1:
                print("Ok, take it slow.")
                return random.randint(1, 10), 10
            elif level == 2:
                print("I know you want more than that.")
                return random.randint(1, 100), 100
            elif level == 3:
                print("I like how confident you are!")
                return random.randint(1, 1000), 1000
            else:
                print("Please enter 1, 2, or 3.")
        except ValueError:
            print("Invalid input! Please enter a valid number.")


def get_user_input(max_value):
    while True:
        try:
            user_guess = int(
                input(f"Guess a number between 1 - {max_value}: "))
            return user_guess
        except ValueError:
            print("Invalid input! Please enter a valid number.")


def in_how_many_guesses():
    how_many_guess = int(
        input("In how many guesses do you think you can beat me? "))
    return how_many_guess


def main():
    welcome()
    number_to_guess, max_value = dificulty()
    print(f"DEBUG: number_to_guess = {
          number_to_guess}, max_value = {max_value}")

    allready_guessed = set()
    number_of_guesses = 0
    guesses_left = in_how_many_guesses()
    while True:

        # Printer, hvor mange gæt user har tilbage

        guess = get_user_input(max_value)
        # Quit game
        if guess == 0:
            print(f"Thank you for playing. The number i was thinking of was {
                  number_to_guess}")
            break

        # Hvis de skriver det samme tal flere gange
        if guess in allready_guessed:
            print(f"You have allready guessed {guess}. Try again")
            continue
        allready_guessed.add(guess)

        # Tilføjer hvor mange gæt de har brugt, og hvor mange gæt de har tilbage
        number_of_guesses += 1
        guesses_left -= 1

        # Hvis de ikke har flere gæt break
        if guesses_left == 0:
            print(f"HaHa, you did not guess my number. The number I was thinking of was {
                  number_to_guess}.")
            break

        # Hvis de går igennem alle if-statemens. User gætter, hvilket tal jeg tænker på.
        if guess > number_to_guess:
            print("You guess is to high. Try again")
        elif guess < number_to_guess:
            print("Your guess is to low. Try again")
        else:
            print(f"You guessed my number {number_to_guess} in {
                  number_of_guesses} attemps")
            break

        print(f"You have: {guesses_left} guesses left")


if __name__ == "__main__":
    main()
