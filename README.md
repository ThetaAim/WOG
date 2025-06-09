# 🎮 World of Games (WOG) - DevOps Edition

Welcome to the **World of Games (WOG)** — an interactive Python-based platform offering a series of mini-games, supported by a Flask web server for score tracking. This repository is a showcase of **DevOps best practices**, combining Docker, orchestration, automation, and modular design.

Developed as part of the *DevOps Experts* course led by **Doron Nuni**, and completed with **distinction**, this project exemplifies practical knowledge in software packaging, containerization, and service verification.

---

## 📦 Features

* 🧠 **Mini-games**: Includes Memory Game, Guess Game, and Currency Roulette.
* 🌐 **Flask server**: Displays user score via a simple web UI.
* 🐳 **Dockerized environment**: Full application stack runs in isolated containers.
* 🧪 **Automated testing**: Selenium test checks web functionality.
* ⚙️ **Persistent scoring**: User progress saved in `Scores.txt`.

---

## 🐳 Dockerized Services

### Dockerfile

Located in `docker/Dockerfile`, the app uses a minimal Python base image and installs only what’s necessary:

```dockerfile
FROM python:3.8-slim-buster
WORKDIR /
COPY ../Tools/Scores.txt .
COPY ../Tools/e2e.py .
COPY ../Tools/main_score.py .
COPY ../Tools/utils.py .
COPY ../Tools/templates /templates
RUN pip install Flask selenium
EXPOSE 5040
CMD ["python", "main_score.py"]
```

### Docker Compose

Found in `docker/docker-compose.yaml`, this file orchestrates the container and exposes port 8090 on your host:

```yaml
version: '3'
services:
  app:
    build:
      context: .
      dockerfile: Dockerfile
    image: orenohayon/wog:v7
    ports:
      - "8090:5040"
    networks:
      - mynet
networks:
  mynet:
```

---

## 🧪 End-to-End Test

The `Tools/e2e.py` file uses **Selenium** to validate that the Flask app displays a valid score:

```python
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

def test_scores_service():
    driver = Chrome()
    driver.get('http://localhost:8080')
    element = driver.find_element(By.ID, 'score')
    score_value = int(element.text)
    print("Score:", score_value)
    driver.quit()
    return 0 < score_value <= 1000
```

Run it via:

```bash
python Tools/e2e.py
```

---

## 🚀 Run Locally

1. Clone the repository:

```bash
git clone https://github.com/yourusername/wog.git
cd wog
```

2. Build & start the service:

```bash
docker-compose -f docker/docker-compose.yaml up --build
```

3. Visit the app:
   [http://localhost:8090](http://localhost:8090)

---

## 🗂️ Project Structure

```
.
├── docker/
│   ├── Dockerfile
│   └── docker-compose.yaml
├── main.py               # Entry point to start the game
├── app.py                # Game selection and flow logic
├── Tools/
│   ├── Scores.txt        # Persistent score file
│   ├── e2e.py            # Selenium test for the Flask server
│   ├── main_score.py     # Flask web service
│   ├── utils.py          # Shared constants and helpers
│   ├── score.py          # Score management logic
│   └── templates/
│       └── not_found.html  # Error template
├── Games/
│   ├── guess_game.py
│   ├── memory_game.py
│   └── currency_roulette_game.py
```

---

## 💡 DevOps Highlights

| Area                  | Description                                      |
| --------------------- | ------------------------------------------------ |
| 🐳 Dockerization      | Minimal base image, production-ready setup       |
| 📦 Orchestration      | Docker Compose defines and runs app containers   |
| 🧪 Testing            | Functional test using Selenium for score display |
| 📊 Logging/Scoring    | Score written to persistent file                 |
| 🧱 Modular Design     | Games, UI, and logic separated into folders      |
| 🔁 Stateless Services | Flask serves from volume-mounted storage         |

---

## 🏁 Conclusion

This project merges Python programming with modern DevOps tooling. It is a practical showcase of containerization, automation, and microservice structuring — all built around a fun and engaging mini-game suite.

---

## ✨ Credits

Built during the DevOps Experts course by Doron Nuni, and completed with excellence, as a final portfolio project.

## 👤 Author

## Oren Ohayon
Aspiring DevOps practitioner with hands-on experience in system automation, containerization, and service orchestration. Always eager to learn and improve through practical projects and teamwork.
