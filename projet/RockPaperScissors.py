import random

#gestion des entrées
choiceList = ["rock", "paper", "scissors"]
computerWins = 0
playerWins = 0


while playerWins <3 and computerWins <3:
    while True:
        try:
            print("Take a choice between rock, paper and scissors")
            playerChoice = input() #INPUT retoune de base une chaine de caractere
            computerChoice = random.choice(choiceList)
            if playerChoice not in choiceList:
                raise Exception #exception personalisé il faut raise, il fut lever l'exception
            else:
                break #fermer la boucle infini
        except Exception:
            print("Wrong choice! Try again please")

    print(f"Computer choice: {computerChoice}")
    # print(f"Player choice: {playerChoice}")

    if playerChoice == "rock" and computerChoice == "scissors":
        print("You won")
        playerWins += 1
        # print(f"Your win counter: {playerWins}")
    elif playerChoice == "scissors" and computerChoice == "papier":
        print("Round won")
        playerWins += 1
        # print(f"Your win counter: {playerWins}")
    elif playerChoice == "paper" and computerChoice == "rock":
        print("Round won")
        playerWins += 1
        # print(f"Your win counter: {playerWins}")
    elif playerChoice == computerChoice:
        print("Round draw")
        playerWins += 0
        computerWins += 0
    else:
        print("Round lost")
        computerWins += 1
        # print(f"Computer win counter: {computerWins}")

    print(f"Your win counter: {playerWins}")
    print(f"Computer win counter: {computerWins}")
if playerChoice == 3:
    print("Nice game, you won!")
elif computerWins == 3:
    print("Game over, the computer won the game!")









# Je vais vous expliquer la logique du jeu Pierre-Papier-Ciseaux et comment structurer votre réflexion.

# Principe du jeu :
# - Deux joueurs choisissent simultanément un des trois éléments : pierre, papier ou ciseaux
# - La pierre bat les ciseaux (la pierre casse les ciseaux) ok
# - Les ciseaux battent le papier (les ciseaux coupent le papier) 
# - Le papier bat la pierre (le papier enveloppe la pierre)
# - Si les deux joueurs choisissent le même élément, c'est une égalité

# Pour structurer votre programme, voici la logique à adopter :

# 1. Gestion des entrées :
# - Permettre au joueur de faire son choix (via une saisie clavier) ok
# - Générer un choix aléatoire pour l'ordinateur ok

# 2. Validation des entrées :
# - Vérifier que le choix du joueur est valide (pierre, papier ou ciseaux) ok
# - Gérer les erreurs potentielles de saisie ok

# 3. Logique de comparaison :
# - Comparer les deux choix selon les règles du jeu
# - Identifier le gagnant en utilisant les conditions de victoire

# 4. Gestion du score (optionnel) :
# - Maintenir un compteur pour le score du joueur et de l'ordinateur
# - Afficher le score après chaque manche

# 5. Boucle de jeu :
# - Permettre de rejouer plusieurs parties
# - Donner l'option de quitter le jeu

# 6. Interface utilisateur :
# - Afficher clairement les choix ok
# - Annoncer le résultat de chaque manche ok
# - Donner des instructions claires au joueur

# Voulez-vous que je détaille certains de ces aspects en particulier ?
