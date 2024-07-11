from .utils import SCORES_FILE_NAME, BAD_RETURN_CODE
import os


def add_score(difficulty):
    winning_points = (difficulty * 3) + 5
    if os.path.exists(SCORES_FILE_NAME):
        with open(SCORES_FILE_NAME, 'r+') as file:
            exist_score = file.read()
            new_score = int(exist_score) + int(winning_points)
            file.seek(0)
            file.truncate()
            file.write(str(new_score))
            file.flush()
            return winning_points
    else:
        with open(SCORES_FILE_NAME, 'w') as file:
            file.write(str(winning_points))
            return winning_points

