# The Memory Game
from Tools.score import add_score
from Tools.utils import clear_screen as cls
from random import randint
import time


def generate_sequence(difficulty):
    generated_list = [str(randint(1, 101)) for _ in range(difficulty)]
    return generated_list


def get_list_from_user(difficulty):
    generated_list = generate_sequence(difficulty)
    user_list = []
    numbers_correct = 0
    time_by_difficulty = abs(float(1 - difficulty / 10))

    print(f"After pressing enter key you will briefly see a list of numbers")
    print(f"lets see if you can memorise them...")
    input_ = input(f"\nPress enter to start! ")

    [(print(f"{generated_list[num]}", end=" ", flush=True), time.sleep(time_by_difficulty)) for num in
     range(len(generated_list))]
    print('\rCan you remember the numbers? enter the numbers in the same order: ')
    print('\n')
    for num in range(len(generated_list)):
        user_each_input = input(f'number {num + 1}: ')
        user_list.append(user_each_input)

        # find how much correct
        if user_list[num] == generated_list[num]:
            numbers_correct += 1
        else:
            numbers_correct = numbers_correct

    return generated_list, user_list, numbers_correct


def is_list_equal(user_list, generated_list):
    if user_list == generated_list:
        return True
    else:
        return False


def play(difficulty):
    cls()

    print("-" * 50)
    print(f'{9 * " "}Welcome to the the Memory game')
    print("-" * 50)

    generated_list, user_list, numbers_correct = get_list_from_user(difficulty)

    is_equal = is_list_equal(user_list, generated_list)

    if is_equal:
        print(f'\nCorrect!')
        print(f'You remembered {numbers_correct} number(s) correct!')
        add_score(difficulty)
    else:
        print(f'\nAlmost there! You remembered only {numbers_correct} number(s) correct!')


