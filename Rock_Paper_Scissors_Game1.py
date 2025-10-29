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

import random
options = [rock, paper, scissors]

print("Welcome! ")
user_choice = int(input("What do you choose? Type 0 for Rock, "
                        "1 for Paper and 2 for Scissors "))
if user_choice < 0 or user_choice > 2:
    print("Your response is invalid")
else:
    print(f"You chose:\n {options[user_choice]}")
    computer_choice = random.randint(0, 2)
    print(f"Computer chose:\n {options[computer_choice]}")

    if computer_choice == user_choice:
       print("It's a tie!")
    elif computer_choice == 0 and user_choice == 2:
       print("You lose!")
    elif user_choice == 0 and computer_choice == 2:
       print("You win!")
    elif computer_choice < user_choice:
       print("You win!")
    else:
       print("You lose")


input("Press enter to EXIT")
