import os

SCORES_FILE_NAME = "Tools/Scores.txt"
BAD_RETURN_CODE = 404


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


