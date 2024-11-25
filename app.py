import json
import random

with open('intrebari.json', 'r', encoding = 'utf-8') as file:
    data = json.load(file)

score = 0
question_counter = 1




print("Bine ati venit la Quiz Game!")
while question_counter <= 5:
    print(f"Intrebarea nr. {question_counter}: ")
    current_question = random.choice(data)
    user_answer = input(f"{current_question['question']}\n")
    if user_answer.lower() == current_question['answer'].lower():
        score += 1
        print("Raspuns Correct!")
    else:
        print("Raspuns Gresit!")
    question_counter += 1
print(f"Ai adunat {score} puncte!")