import tkinter as tk
import random

# Main window
root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("400x400")

choices = ["Rock", "Paper", "Scissors"]

user_score = 0
computer_score = 0

def play(user_choice):
    global user_score, computer_score

    computer_choice = random.choice(choices)

    user_choice_label.config(text="Your Choice: " + user_choice)
    computer_choice_label.config(text="Computer Choice: " + computer_choice)

    if user_choice == computer_choice:
        result = "It's a Tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        result = "You Win!"
        user_score += 1
    else:
        result = "Computer Wins!"
        computer_score += 1

    result_label.config(text=result)
    score_label.config(
        text=f"Your Score: {user_score}    Computer Score: {computer_score}"
    )

# Heading
title = tk.Label(root, text="Rock Paper Scissors Game",
                 font=("Arial", 16, "bold"))
title.pack(pady=10)

instruction = tk.Label(root, text="Choose Rock, Paper, or Scissors")
instruction.pack()

# Buttons
frame = tk.Frame(root)
frame.pack(pady=10)

rock_btn = tk.Button(frame, text="Rock", width=10,
                     command=lambda: play("Rock"))
rock_btn.grid(row=0, column=0, padx=5)

paper_btn = tk.Button(frame, text="Paper", width=10,
                      command=lambda: play("Paper"))
paper_btn.grid(row=0, column=1, padx=5)

scissors_btn = tk.Button(frame, text="Scissors", width=10,
                         command=lambda: play("Scissors"))
scissors_btn.grid(row=0, column=2, padx=5)

# Labels
user_choice_label = tk.Label(root, text="Your Choice: ")
user_choice_label.pack(pady=5)

computer_choice_label = tk.Label(root, text="Computer Choice: ")
computer_choice_label.pack(pady=5)

result_label = tk.Label(root, text="", font=("Arial", 14, "bold"))
result_label.pack(pady=10)

score_label = tk.Label(root, text="Your Score: 0    Computer Score: 0")
score_label.pack(pady=10)

# Exit button
exit_btn = tk.Button(root, text="Exit", width=10, command=root.destroy)
exit_btn.pack(pady=15)

root.mainloop()
