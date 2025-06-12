import tkinter as tk
import random

# ASCII Art
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]
choices = ["Rock", "Paper", "Scissors"]

# Game logic
def play(user_choice):
    computer_choice = random.randint(0, 2)

    result = ""
    if user_choice == computer_choice:
        result = "It's a draw!"
    elif (user_choice == 0 and computer_choice == 2) or \
         (user_choice == 1 and computer_choice == 0) or \
         (user_choice == 2 and computer_choice == 1):
        result = "You win!"
    else:
        result = "You lose!"

    user_label.config(text=f"You chose {choices[user_choice]}:\n{game_images[user_choice]}")
    comp_label.config(text=f"Computer chose {choices[computer_choice]}:\n{game_images[computer_choice]}")
    result_label.config(text=result)

# GUI setup
root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("500x600")
root.configure(bg="lightgray")

# Labels
tk.Label(root, text="Choose Rock, Paper, or Scissors", font=("Arial", 16), bg="lightgray").pack(pady=10)

btn_frame = tk.Frame(root, bg="lightgray")
btn_frame.pack(pady=10)

# Buttons
tk.Button(btn_frame, text="Rock", font=("Arial", 14), command=lambda: play(0)).grid(row=0, column=0, padx=10)
tk.Button(btn_frame, text="Paper", font=("Arial", 14), command=lambda: play(1)).grid(row=0, column=1, padx=10)
tk.Button(btn_frame, text="Scissors", font=("Arial", 14), command=lambda: play(2)).grid(row=0, column=2, padx=10)

user_label = tk.Label(root, text="", font=("Courier", 10), bg="lightgray", justify="left")
user_label.pack(pady=10)

comp_label = tk.Label(root, text="", font=("Courier", 10), bg="lightgray", justify="left")
comp_label.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 16, "bold"), bg="lightgray", fg="blue")
result_label.pack(pady=20)

root.mainloop()
