from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By


def test_scores_service():
    driver = Chrome()
    driver.get('http://localhost:8080')

    element = driver.find_element(By.ID, 'score')
    score_value = int(element.text)
    print("Score:", score_value)
    driver.quit()
    if 0 < score_value <= 1000:
        return True
    else:
        return False


def main_function():
    if test_scores_service():
        return 0
    else:
        print('exceeded')
        return -1

