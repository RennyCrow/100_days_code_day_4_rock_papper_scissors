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

choices = [rock, paper, scissors]

choice= int(input ("What do you choose? Type 0 for  Rock, 1 for Paper or 2 for Scissors."))

ia_choice = random.randint(0,2)
print(f"IA CHOICE: {ia_choice}")
print(choices[choice])
print("Computer  chose:")
print(choices[ia_choice])

if choice == 2 and ia_choice == 0:
    print("You lose.")
elif choice == 0 and ia_choice == 2:
    print("You win.")
elif choice > ia_choice:
    print("You win.")
elif choice < ia_choice:
    print("You lose.")
else:
    print("Draw.")