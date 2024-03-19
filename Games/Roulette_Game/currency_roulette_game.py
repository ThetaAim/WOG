
# The Currency Roulette Game Game
from Tools.score import add_score
from Tools.utils import clear_screen as cls
from currency_converter import CurrencyConverter
from random import randint
import time


def get_rate():
    c = CurrencyConverter()
    try:
        rate = c.convert(1, 'USD', 'ILS')
    except Exception as e:
        print(f'something went wrong... {e}')
    return rate


def get_guess_from_user(difficulty, random_dollars):
    # print(random_dollars * get_rate())

    while True:
        user_guess = input(f"Make a guess! how much is {random_dollars}$ in ILS? ")
        try:
            user_guess = abs(float(user_guess))
            return user_guess

        except ValueError:
            continue


def get_money_interval(difficulty, dollars_nis):
    rate_by_max = float(dollars_nis + (10 - difficulty))
    rate_by_min = float(dollars_nis - (10 - difficulty))
    return rate_by_min, rate_by_max


def compare_results(mini, maxi, user_guess):
    if mini <= user_guess <= maxi:
        return True
    else:
        return False


def play(difficulty):
    cls()
    random_dollars = randint(1, 101)
    dollars_in_nis = float(get_rate() * random_dollars)

    print("-" * 50)
    print(f'{4 * " "}Welcome to the the Currency Roulette game')
    print("-" * 50)

    get_guess = get_guess_from_user(difficulty, random_dollars)
    mini, maxi = get_money_interval(difficulty, dollars_in_nis)
    get_compare_value = compare_results(mini, maxi, get_guess)

    if get_compare_value:
        print(f'\nCorrect! {random_dollars}$ is approximately {round(dollars_in_nis, 2)} ILS ')
        time.sleep(1)
        print(f'\nYou won {add_score(difficulty)} points!')
    else:
        print(f'\nNice try, but you are wrong! {random_dollars}$ is {round(dollars_in_nis, 2)} ILS')
        time.sleep(1)
        return False
