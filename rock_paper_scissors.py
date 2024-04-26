import random

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

#Write your code below this line 👇

images = [rock, paper, scissors]
user_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print(images[user_input])

computer = random.randint(0,2)
print("Computer chose:")
print(images[computer])

if user_input >= 3 or user_input < 0:
  print("You typed an invalid number, you lose!")
elif user_input == 0 and computer == 2:
    print("You win!")
elif computer == 0 and user_input == 2:
    print("You lose!")
elif computer > user_input:
    print("You lose!")
elif user_input > computer:
    print("You win!")
elif user_input == computer:
    print("It's a draw")
