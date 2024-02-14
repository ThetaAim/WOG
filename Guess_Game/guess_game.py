# The Guess_Game
from Tools.score import add_score
from Tools.utils import clear_screen as cls
from random import randint


def generate_number(difficulty):
    return randint(0, difficulty)


def get_guess_from_user(difficulty):
    input_valid = True
    while input_valid:
        user_input = input(f'Guess a number between 0 to {difficulty}: ')
        if user_input.isdigit():
            user_input = int(user_input)
            while 0 <= user_input <= difficulty:
                return int(user_input)
            else:
                continue
        else:
            continue


def compare_results(guess, secret_num):
    if guess == secret_num:
        print('You win!')
        return True
    else:
        print('You lose!')
        return False


def play(difficulty):
    cls()
    print("-" * 50)
    print(f'{10 * " "}Welcome to the the guess game')
    print("-" * 50)

    secret_number = generate_number(difficulty)
    guessed_by_user = get_guess_from_user(difficulty)

    if compare_results(guessed_by_user, secret_number):
        add_score(difficulty)






