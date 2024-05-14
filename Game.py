import random
import tkinter as tk
from tkinter import messagebox

def generate_random_number():
    return random.randint(1, 100)

def check_guess():
    global attempts
    guess = int(guess_entry.get())
    attempts += 1

    if guess < target_number:
        result_label.config(text="Too low! Try again.", fg="red")
    elif guess > target_number:
        result_label.config(text="Too high! Try again.", fg="red")
    else:
        result_label.config(text=f"Congratulations! You've guessed the number {target_number} in {attempts} attempts!", fg="green")
        guess_entry.config(state=tk.DISABLED)
        submit_button.config(state=tk.DISABLED)
    
    # Clear the guess entry field after checking the guess
    guess_entry.delete(0, tk.END)

def play_game():
    global target_number, attempts

    target_number = generate_random_number()
    attempts = 0

    result_label.config(text="", fg="black")
    guess_entry.delete(0, tk.END)  # Clear the guess entry field at the start of a new game
    guess_entry.config(state=tk.NORMAL)
    submit_button.config(state=tk.NORMAL)

window = tk.Tk()
window.title("Number Guessing Game")

title_label = tk.Label(window, text="Welcome To The Number Guessing Game!", font=("Helvetica", 19, "bold"), pady=10)
title_label.pack()

instruction_label = tk.Label(window, text="Think Of A Number Between 1 And 100.", font=("Helvetica", 16))
instruction_label.pack()

guess_entry = tk.Entry(window, width=10, font=("Helvetica", 42), justify="center")
guess_entry.pack(pady=10)

submit_button = tk.Button(window, text="Submit Guess", command=check_guess, font=("Helvetica", 14, "bold"), bg="blue", fg="white")
submit_button.pack(pady=10)

result_label = tk.Label(window, text="", font=("Helvetica", 16), pady=10)
result_label.pack()

play_button = tk.Button(window, text="Play Again", command=play_game, font=("Helvetica", 14, "bold"), bg="green", fg="white")
play_button.pack(pady=10)

author_label = tk.Label(window, text="Daniel Rizvi © 2024", font=("Helvetica", 10))
author_label.pack(side=tk.RIGHT, padx=10, pady=5)

play_game()  # Start the game when the GUI is launched

window.mainloop()
