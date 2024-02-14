from Guess_Game.guess_game import play as guess_play
from Roulette_Game.currency_roulette_game import play as curl_play
from Memory_Game.memory_game import play as memo_play
from Tools.utils import clear_screen as cls


games = [
    {
        "name": "Memory Game",
        "description": "a sequence of numbers will appear for 1 second and you have to guess it back.",
        "feedback": "Ah, the classic memory game! The only place where forgetting is not an option...",
    },
    {
        "name": "Guess_Game",
        "description": "guess a number and see if you chose like the computer.",
        "feedback": "Feeling like a mind reader today? GUESS what? you are in the right place!",
    },
    {
        "name": "Currency Roulette Game",
        "description": "try and guess the value of a random amount of USD in ILS.",
        "feedback": "Feeling like a financial wizard today, Eh?",
    }

]


def chk_input(string, mini, maxi):
    input_in_range = True
    while input_in_range:
        some_input = input(f'\n{string} ({mini}-{maxi}): ')
        if some_input == 'exit':
            exit()
        if some_input.isdigit():
            some_input = int(some_input)
            if mini <= some_input <= maxi:
                if (mini == 1) and (maxi == 3):
                    print(games[some_input - 1]["feedback"])
                    return some_input
                else:
                    return some_input
            else:
                print(f'Please enter a valid number. numbers between {mini} to {maxi}', end='')

        else:
            print(f'Please insert a valid input. numbers {mini} to {maxi}', end='')


def welcome():
    cls()
    print("-" * 50)
    print(f'{9 * " "}Welcome to the World Of Games')
    print("-" * 50)
    name_is_valid = True
    while name_is_valid:
        name = input('\n\rPlease enter your name: ')
        if name:
            print(f"\nHi {name.capitalize()}, and welcome to the World of Games: The Epic Journey\n")
            break
        else:
            continue


def start_play():
    game_continue = True
    games_functions = [0, memo_play, guess_play, curl_play]

    while game_continue:
        welcome()

        for index, game in enumerate(games):
            print(f"{index + 1}. {game['name']} - {game['description']}")

        game_number = chk_input('\nPlease choose a game to play', 1, 3)
        difficulty = chk_input('Please choose Difficulty', 1, 5)

        games_functions[game_number](difficulty)
        game_played = True

        while game_played:
            play_again = input('\nPlay again? (y/n):')
            if play_again.lower() == "y":
                cls()
                break
            elif play_again.lower() == "n":
                print('\nThat was fun hope to see you again...\n')
                return
            else:
                continue
