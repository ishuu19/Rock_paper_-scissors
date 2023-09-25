# Rock, Paper, Scissors Game

import random

my_choice = str(input("Please enter your choice. Rock, Paper or Scissors"))


choices = ["Rock", "Paper", "Scissors"]

rand_choice = random.randint(0, 2)
comp_choice = choices[rand_choice]

Rock = '''  
    _______
---'   ____)  
      (_____)  
      (_____)  
      (____)
---.__(___)  
'''

Paper = '''  
    _______
---'   ____)____  
          ______)  
          _______)  
         _______)
---.__________)  
'''

Scissors = '''  
    _______
---'   ____)____  
          ______)  
       __________)  
      (____)
---.__(___)  
'''

comp_art = [Rock, Paper, Scissors]

if my_choice == "Rock":
    print(f'Your choice is: {my_choice}\n{Rock}')
elif my_choice == "Paper":
    print(f'Your choice is: {my_choice}\n{Paper}')
elif my_choice == "Scissors":
    print(f'Your choice is: {my_choice}\n{Scissors}')

# draw = comp_art[comp_art==my_choice]

if my_choice =="Rock" and comp_choice =='Rock':
    print(f"Computer choice is: Rock.\n{Rock}\nIt's a draw. Play again!")
elif my_choice =="Paper" and comp_choice =='Paper':
    print(f"Computer choice is: Paper.\n{Paper}\nIt's a draw. Play again!")
elif my_choice =="Scissors" and comp_choice =='Scissors':
    print(f"Computer choice is: Scissors.\n{Scissors}\nIt's a draw. Play again!")
elif my_choice == 'Rock' and comp_choice =='Scissors':
    print(f"Computer choice is: Scissors.\n{Scissors}\nYou win!")
elif my_choice == 'Rock' and comp_choice =="Paper":
    print(f"Computer choice is: Paper.\n{Paper}\nComputer wins!")
elif my_choice == 'Paper' and comp_choice =="Scissors":
    print(f"Computer choice is: Scissors.\n{Scissors}\nComputer wins!")
elif my_choice == 'Paper' and comp_choice =="Rock":
    print(f"Computer choice is: Rock.\n{Rock}\nYou win!")
elif my_choice == 'Scissors' and comp_choice =="Rock":
    print(f"Computer choice is: Rock.\n{Rock}\nComputer wins!")
elif my_choice == 'Scissors' and comp_choice =="Paper":
    print(f"Computer choice is: Paper.\n{Paper}\nYou win!")