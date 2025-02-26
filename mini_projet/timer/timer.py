import time as tm
# amelioration quitter le programme avec un touche

print("Welcome to the Focus Timer!")


while True:
    try:
        session_dur = int(input("Enter a focus session duration (in minutes): "))
        break_dur = int(input("Enter break duration  (in minutes): "))
        session_count = int(input("How many focus sessions would you like to complete? "))
        break
    except Exception:
        print("Wrong type, try again!")

session_dur_sec = session_dur*60
break_dur_sec = break_dur*60

for i in range(session_count):
    print(f"session {i+1} of {session_count}")
    print(f"Focus for {session_dur_sec} minute(s). Stay on track! 🚀")
    tm.sleep(session_dur_sec)
    print("End of session")
    print(f"Take a break for {break_dur_sec} minute(s)")
    tm.sleep(break_dur_sec)
    print("End of break")


total_focus = session_count*session_dur
total_break = session_count*break_dur


print(f"Your focus session ends. You did {total_focus+total_break} minutes")

# amelioration Tu pourrais aussi considérer d'ajouter :

# Le principal problème de ton code actuel est que time.sleep() bloque complètement
# l'exécution, ce qui empêche de détecter les touches pendant ce temps.
# Une meilleure approche serait de diviser le temps d'attente en plus petits intervalles 
# et vérifier régulièrement si l'utilisateur veut quitter.
# Aussi, il serait utile d'informer l'utilisateur au début du programme qu'il peut quitter
# à tout moment avec une touche spécifique (par exemple 'q').


# Un compte à rebours visible pendant les sessions/pauses
# Une option pour mettre en pause temporairement
# Un résumé des sessions complétées si l'utilisateur quitte avant la fin

