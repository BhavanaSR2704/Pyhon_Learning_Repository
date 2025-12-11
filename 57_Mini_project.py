import json
import os

# ----------------- FILE HANDLING -----------------
LEADERBOARD_FILE = "leaderboard.json"

def load_leaderboard():
    if os.path.exists(LEADERBOARD_FILE):
        with open(LEADERBOARD_FILE, "r") as f:
            return json.load(f)
    else:
        return {}

def save_leaderboard(leaderboard):
    with open(LEADERBOARD_FILE, "w") as f:
        json.dump(leaderboard, f, indent=4)

# ----------------- QUIZ DATA -----------------
quiz_questions = [
    {
        "question": "What is the capital of India?",
        "options": ["1. Delhi", "2. Mumbai", "3. Bangalore", "4. Chennai"],
        "answer": 1
    },
    {
        "question": "Which programming language is this quiz written in?",
        "options": ["1. Java", "2. C", "3. Python", "4. Ruby"],
        "answer": 3
    },
    {
        "question": "Which of these is a loop in Python?",
        "options": ["1. for", "2. switch", "3. define", "4. print"],
        "answer": 1
    },
    {
        "question": "What does 'if' statement do?",
        "options": ["1. Loop", "2. Condition", "3. Function", "4. Variable"],
        "answer": 2
    },
]

# ----------------- FUNCTIONS -----------------
def take_quiz(username):
    score = 0
    print(f"\nHello {username}, welcome to the quiz! Answer by typing the option number.\n")
    for i, q in enumerate(quiz_questions):
        print(f"Q{i+1}: {q['question']}")
        for opt in q['options']:
            print(opt)
        while True:
            try:
                answer = int(input("Your answer: "))
                if answer < 1 or answer > 4:
                    raise ValueError
                break
            except ValueError:
                print("Invalid input. Please enter a number from 1 to 4.")
        if answer == q['answer']:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! Correct answer: {q['answer']}\n")
    print(f"Quiz Finished! Your score: {score}/{len(quiz_questions)}\n")
    return score

def update_leaderboard(username, score, leaderboard):
    if username in leaderboard:
        if score > leaderboard[username]:
            leaderboard[username] = score
    else:
        leaderboard[username] = score
    save_leaderboard(leaderboard)

def show_leaderboard(leaderboard):
    print("\n--- LEADERBOARD ---")
    sorted_board = sorted(leaderboard.items(), key=lambda x: x[1], reverse=True)
    for rank, (user, score) in enumerate(sorted_board, start=1):
        print(f"{rank}. {user}: {score}")
    print("-------------------\n")

# ----------------- MAIN PROGRAM -----------------
def main():
    leaderboard = load_leaderboard()
    print("Welcome to the Student Quiz & Score Tracker!\n")
    username = input("Enter your name: ").strip()
    while True:
        print("\nMenu:\n1. Take Quiz\n2. Show Leaderboard\n3. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            score = take_quiz(username)
            update_leaderboard(username, score, leaderboard)
        elif choice == "2":
            show_leaderboard(leaderboard)
        elif choice == "3":
            print("Goodbye! Have a great day!")
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()



#=======================================================================O/P:-
Welcome to the Student Quiz & Score Tracker!

Enter your name: Bhavana

Menu:
1. Take Quiz
2. Show Leaderboard
3. Exit
Enter your choice: 1

Hello Bhavana, welcome to the quiz! Answer by typing the option number.

Q1: What is the capital of India?
1. Delhi
2. Mumbai
3. Bangalore
4. Chennai
Your answer: 1
Correct!

Q2: Which programming language is this quiz written in?
1. Java
2. C
3. Python
4. Ruby
Your answer: 1
Wrong! Correct answer: 3

Q3: Which of these is a loop in Python?
1. for
2. switch
3. define
4. print
Your answer: 1
Correct!

Q4: What does 'if' statement do?
1. Loop
2. Condition
3. Function
4. Variable
Your answer: 2
Correct!

Quiz Finished! Your score: 3/4


Menu:
1. Take Quiz
2. Show Leaderboard
3. Exit
Enter your choice: 2

--- LEADERBOARD ---
1. Bhavana: 3
-------------------


Menu:
1. Take Quiz
2. Show Leaderboard
3. Exit
Enter your choice: 3
Goodbye! Have a great day!
