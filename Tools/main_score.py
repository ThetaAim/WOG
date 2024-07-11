from utils import SCORES_FILE_NAME, BAD_RETURN_CODE
from flask import Flask, render_template
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
template_folder = os.path.join(current_dir, 'templates')
app = Flask(__name__, template_folder=template_folder)
# app = Flask(__name__, template_folder='/Users/user/Desktop/Devops-Classes/WOG/templates/')

@app.route('/')
def score_server():
    if os.path.exists(f'{SCORES_FILE_NAME}'):
        with open(f"{SCORES_FILE_NAME}", 'r+') as file:
            exist_score = file.read()
            return render_template('index.html', title="Scores Game", SCORE=exist_score)

    elif not os.path.exists(f'{SCORES_FILE_NAME}'):
        with open(f'{SCORES_FILE_NAME}', 'w') as file:
            file.write(str('0'))
            exist_score = 0
            return render_template('index.html', title="Scores Game", SCORE=exist_score)
    else:
        return render_template('not_found.html', title="Something went wrong...", ERROR=f"Scores file not found "
                                                                                        f"{BAD_RETURN_CODE}")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5040, debug=True)
