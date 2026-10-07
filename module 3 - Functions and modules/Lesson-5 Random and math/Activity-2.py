#Import the random module to let the computer make a random choice.
import random
while True:
    user_action = input("Enter your choice (rock,paper or scissors):  ")
    possible_actions = ["rock","paper","scissors"]
    computer_action = random.choice(possible_actions)
    print(f"Your choice is {user_action} and computers choice is {computer_action}.")
    if user_action == computer_action:
        print("Oop, its a tie!")
    elif user_action == "rock" and computer_action == "scissors":
        print("Yayy, you win!")
    elif user_action == "scissors" and computer_action == "rock":
        print("Oop, computer wins!")
    elif user_action == "paper" and computer_action == "scissors":
        print("Oop, computer wins!")
    elif user_action == "scissors" and computer_action == "paper":
        print("Yayy, you win!")
    elif user_action == "rock" and computer_action == "paper":
        print("Oop, computer wins!")
    elif user_action == "paper" and computer_action == "rock":
        print("Yayy, you win!")
    print("Do you want to play again?")
    play_again = input("Press 'yes' to play again or 'no' to not play again: ")
    if play_again != 'yes':
        break
    else:
        print("Okay bye!")    
    
        
   
    
# 2) Start an infinite loop using `while True` so the game can repeat for multiple rounds.

# 3) Take the user's choice as input and store it in `user_action`.

# (Expected inputs: "rock", "paper", or "scissors".)

# 4) Create a list `possible_actions` containing the three valid moves.

# 5) Use `random.choice(possible_actions)` to randomly select the computer’s move

# and store it in `computer_action`.

# 6) Display both choices (user and computer) using an f-string.

# 7) Compare `user_action` and `computer_action` to decide the result:

# a) If both are the same, print that it’s a tie.

# b) Else if the user chose "rock":

# i) If computer chose "scissors", user wins.

# ii) Otherwise, user loses (computer chose "paper").

# c) Else if the user chose "paper":

# i) If computer chose "rock", user wins.

# ii) Otherwise, user loses (computer chose "scissors").

# d) Else if the user chose "scissors":

# i) If computer chose "paper", user wins.

# ii) Otherwise, user loses (computer chose "rock").

# 8) After showing the result, ask the user if they want to play again

# and store the input in `play_again`.

# 9) If `play_again` is not "y", stop the game using `break`.

# Otherwise, the loop continues and a new round starts.