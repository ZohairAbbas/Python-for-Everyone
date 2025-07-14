computer_input = input("Enter computer's choice:")
user_input = input("Enter your choice:")

if computer_input == user_input:
    print("Tie")
elif ((computer_input == "Rock" and user_input == "Paper") or
    (computer_input == "Paper" and user_input == "Scissors") or
    computer_input == "Scissors" and user_input == "Rock"):
    print("You Win")
else:
    print("You Lose")
