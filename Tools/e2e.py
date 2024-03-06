from Tools.utils import SCORES_FILE_NAME, BAD_RETURN_CODE
import os
from selenium.webdriver import Chrome


def test_scores_service():
    driver = Chrome()
    driver.get('http://localhost:5040')

    element = driver.find_element('id', 'score')
    score_value = int(element.text)
    print("Score:", score_value)
    if 0 < score_value <= 1000:
        return True
    else:
        return False
    driver.quit()


def main_function():
    if test_scores_service():
        return 0
    else:
        print('exceeded')
        return -1

