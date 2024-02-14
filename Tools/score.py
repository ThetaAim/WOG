from Tools.utils import SCORES_FILE_NAME
import os


def add_score(difficulty):
    winning_points = (difficulty * 3) + 5
    # print(winning_points)
    if os.path.exists(SCORES_FILE_NAME):
        with open(SCORES_FILE_NAME, 'r+') as file:
            exist_score = file.read()
            # print(exist_score)
            new_score = int(exist_score) + int(winning_points)
            # print(new_score)
            file.seek(0)
            file.truncate()
            file.write(str(new_score))
            file.flush()
    else:
        with open(SCORES_FILE_NAME, 'w') as file:
            file.write(str(winning_points))


