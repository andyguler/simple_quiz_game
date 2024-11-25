# Quiz Game

Welcome to the **Quiz Game**, a simple command-line game where you can test your knowledge by answering random questions from a JSON file.

---

## Table of Contents

1. [About](#about)
2. [Features](#features)
3. [Setup Instructions](#setup-instructions)
4. [How to Play](#how-to-play)
5. [Contributing](#contributing)
6. [License](#license)

---

## About

The **Quiz Game** selects random questions from a JSON file (`intrebari.json`) and quizzes the player. For each correct answer, the player earns a point. The game ends after 5 questions, and the final score is displayed.

---

## Features

- Randomized questions for a fresh experience every time.
- Keeps track of the player's score.
- Simple and user-friendly interface.

---

## Setup Instructions

1. **Clone the repository**:
    ```bash
    git clone https://github.com/<your-username>/quiz-game.git
    cd quiz-game
    ```

2. **Prepare the JSON file**:
    Create a file named `intrebari.json` in the same directory as the script. The file should contain a list of questions in the following format:
    ```json
    [
        {
            "question": "What is the capital of France?",
            "answer": "Paris"
        },
        {
            "question": "What is 2 + 2?",
            "answer": "4"
        }
    ]
    ```

3. **Run the game**:
    Ensure you have Python installed, then execute:
    ```bash
    python quiz_game.py
    ```

---

## How to Play

1. After starting the game, you'll be greeted with a welcome message.
2. You will be asked 5 random questions, one at a time.
3. Type your answer and press **Enter**.
4. The game will inform you whether your answer is correct or incorrect.
5. At the end of the game, your final score will be displayed.

---
