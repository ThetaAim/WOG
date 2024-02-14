from app import start_play
import subprocess
import webbrowser
import sys
import time

start_play()

print('Opening browser to show your score.')
webbrowser.open('http://localhost:5040')

#
# def start_flask_server():
#     subprocess.Popen([sys.executable, 'main_score.py'], cwd='/Users/user/Desktop/Devops-Classes/Vog2/Tools/')
#
#
# def open_browser():
#     time.sleep(1)
#     webbrowser.open('http://localhost:5040')
#
#
# if __name__ == '__main__':
#     start_flask_server()
#     open_browser()
