#TimeTable Game
import tkinter as tk
import random

def generate_question():
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    return num1, num2, num1 * num2

def check_answer():
    user_answer = int(entry.get())
    if user_answer == current_answer:
        feedback_label.config(text="Correct!", fg="green")
        update_score(1)
    else:
        feedback_label.config(text="Incorrect!", fg="red")
    entry.delete(0, tk.END)
    ask_question()

def ask_question():
    global current_answer
    num1, num2, current_answer = generate_question()
    question_label.config(text=f"What is {num1} x {num2}?")

def update_score(points):
    global score
    score += points
    score_label.config(text=f"Score: {score}")

# Create the GUI
root = tk.Tk()
root.title("Times Table Game")

# Initialize game variables
score = 0
current_answer = None

# Create the score label
score_label = tk.Label(root, text="Score: 0")
score_label.pack()

# Create the question label
question_label = tk.Label(root, text="")
question_label.pack()

# Create the user input field
entry = tk.Entry(root, width=10)
entry.pack()

# Create the feedback label
feedback_label = tk.Label(root, text="")
feedback_label.pack()

# Create the submit button
submit_button = tk.Button(root, text="Submit", command=check_answer)
submit_button.pack()

# Start the game
ask_question()

root.mainloop()