import random
import tkinter as tk

def get_user_choice():
    user_choice = user_choice_var.get()
    if user_choice in ['rock', 'paper', 'scissors']:
        play_round(user_choice)
    else:
        result_label.config(text="Invalid input. Please enter 'rock', 'paper', or 'scissors'.")

def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return 'draw'
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return 'user'
    else:
        return 'computer'

def play_round(user_choice):
    computer_choice = get_computer_choice()
    computer_choice_label.config(text=f"Computer's choice: {computer_choice}")

    winner = determine_winner(user_choice, computer_choice)
    if winner == 'user':
        result_label.config(text="You win!")
        user_wins_var.set(user_wins_var.get() + 1)
    elif winner == 'computer':
        result_label.config(text="Computer wins!")
        computer_wins_var.set(computer_wins_var.get() + 1)
    else:
        result_label.config(text="It's a draw!")
        draws_var.set(draws_var.get() + 1)

    # Update the score label
    score_label.config(text=f"Score - You: {user_wins_var.get()}, Computer: {computer_wins_var.get()}, Draws: {draws_var.get()}")

def quit_game():
    root.destroy()

# Create the GUI window
root = tk.Tk()
root.title("Rock Paper Scissors")

# Create variables for score tracking
user_wins_var = tk.IntVar()
computer_wins_var = tk.IntVar()
draws_var = tk.IntVar()

# Create labels to display the score
score_label = tk.Label(root, text="Score - You: 0, Computer: 0, Draws: 0")
score_label.pack()

# Create labels for user and computer choices
user_choice_var = tk.StringVar()
user_choice_label = tk.Label(root, text="Enter your choice (rock, paper, scissors):")
user_choice_label.pack()
user_entry = tk.Entry(root, textvariable=user_choice_var)
user_entry.pack()

computer_choice_label = tk.Label(root, text="Computer's choice: ")
computer_choice_label.pack()

# Create label for result
result_label = tk.Label(root, text="")
result_label.pack()

# Create buttons for playing and quitting the game
play_button = tk.Button(root, text="Play", command=get_user_choice)
play_button.pack()

quit_button = tk.Button(root, text="Quit", command=quit_game)
quit_button.pack()

# Set initial values for score variables
user_wins_var.set(0)
computer_wins_var.set(0)
draws_var.set(0)

# Start the GUI event loop
root.mainloop()
