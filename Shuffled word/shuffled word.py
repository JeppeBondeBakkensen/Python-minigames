import random

ord_liste = [
    "blomster", "fiskeri", "vandring", "klipper", "solskin",
    "håndværk", "fuglsang", "kuglepen", "studenter", "mødelokale",
    "lufthavn", "skrivebord", "arbejdsmiljø", "jernbane", "havemøbler",
    "fællesskab", "billedkunst", "fugleliv", "solnedgang", "cykelsport"
]
# Shufler bogstaverne i et udvalgt ord
chosen_word = random.choice(ord_liste)
list_of_char = random.sample(chosen_word, len(chosen_word))
tekst = "".join(list_of_char)
print(chosen_word)


def user_guess():
    user_input = input(f"Hvilket ord gemmer sig bag {tekst}? ")
    return user_input


def right_index(input):
    check_userinput = []
    chosen_word_as_list = []
    combined = []

    for char in input:
        check_userinput.append(char)

    for char in chosen_word:
        chosen_word_as_list.append(char)

    for index_1, element_1 in enumerate(check_userinput):
        for index_2, element_2 in enumerate(chosen_word_as_list):
            if (element_1 == element_2) and (index_1 == index_2):
                combined.append(str(index_1 + 1))

    rigtig_gæt = ", ".join(combined)
    print(f"Plads {rigtig_gæt} er korrekt")


def hint():
    while True:
        try:
            want_a_hint = int(input("Press 1 for a hint else press 0: "))
            if want_a_hint == 1:
                return print(f"De 3 første bogstaver i ordet er: {chosen_word[:3]}")
            elif want_a_hint == 0:
                user_guess()
            else:
                print("Enter 1 or 0")
        except ValueError:
            print("Invalid input! Please enter a valid number.")


def main():
    number_of_guess = 0
    while True:
        number_of_guess += 1
        user_input = user_guess()
        right_index(user_input)
        if user_input == chosen_word:
            print(f"Sådan du fandt ordet {chosen_word} i {number_of_guess}")
            break
        elif number_of_guess >= 3:
            hint()
        else:
            print("Try again")


if __name__ == "__main__":
    main()
