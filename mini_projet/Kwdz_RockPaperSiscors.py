import random

choices = ["rock","paper","scissors"]

print("Let's play rock,paper,scissors")
print("chose a number of round")

round_choice = 0

# if isinstance(round_choice,int) == True :
#   print(f"good luck on your {round_choice} round game")
# else :
#   print("make sure you choose a number")


round_played = 0

tie = True

while True :
 
  try: # tester l'erreur : input integer instead of string for the variable round_choice
    round_choice = int(input("Enter the round number: "))
    print(f"Good luck on your {round_choice} round game!")
    break
  # except ValueError :
  except Exception :
    print("Make sure you choose a valid number.")

while round_played < round_choice :
  
  player_choice = input("choose rock, paper, or scissors : ").lower()
  computer_choice = random.choice(choices)

  if player_choice != "rock" and player_choice != "paper" and player_choice != "scissors" :
    print("you should chose one of the proposition. Please try again.")
    round_choice += 1

  elif(player_choice == "rock" and computer_choice == "scissors") or (player_choice == "paper" and computer_choice == "rock") or (player_choice == "scissors" and computer_choice == "paper") :
    print("you win" + f" computer chose:{computer_choice}")

  elif player_choice == computer_choice :
    print("it is a tie, try again")
    tie = True
    round_choice += 1

  else :
    print ("you lose " + f" computer chose:{computer_choice}")
  
  round_played += 1
