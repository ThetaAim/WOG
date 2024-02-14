from Tools.utils import SCORES_FILE_NAME
from flask import Flask, render_template
import os

app = Flask(__name__, template_folder='/Users/user/Desktop/Devops-Classes/Vog2/templates/')
app.config['DEBUG'] = False


@app.route('/')
def score_server():
    if os.path.exists(f'../{SCORES_FILE_NAME}'):
        with open(f"../{SCORES_FILE_NAME}", 'r+') as file:
            exist_score = file.read()
            return render_template('index.html', title="Scores Game", SCORE=exist_score)
    else:
        return render_template('not_found.html', title="Something went wrong...", ERROR="Scores file not found")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5040, debug=False)
