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

images = [rock, paper, scissors]

print("Welcome to Rock Paper and Scissors!!")
player = int(input("What do you choose? '0' for Rocks, '1' for Paper and '2' for Scissors  "))

print(f"{images[player]}")
computer = random.randint(0,2)
print(f"Computer choice : \n {images[computer]}")

if player == computer :
    print("Draw")
elif player == 2 and computer == 0:
    print("You Lose!")
elif player == 0 and computer == 2:
    print("You Win!")
elif player > computer : 
    print("You Win!")
elif player < computer :
    print("You Lose!")
else:
    print("Invalid choice!")

