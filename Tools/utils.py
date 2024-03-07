import os
# current_dir = os.path.dirname(os.path.abspath(__file__))
# SCORES_FILE_NAME = os.path.join(current_dir, "Scores.txt")

SCORES_FILE_NAME = "./Scores.txt"

BAD_RETURN_CODE = 404


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


