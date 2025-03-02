import random as rd

# 💡 Amelioration
# Utilisation d’un dictionnaire workouts pour simplifier la gestion des exercices.
# Suppression de workout_type qui était redondant.

workout_type = ["strength", "cardio", "flexibility"]
strength = ["Push-ups", "Squats", "Lunges", "Plank", "Dumbbell Press"]
cardio = ["Jumping Jacks", "Burpees", "Running in Place", "Jump Rope", "High Knees"]
flexibility = ["Yoga Stretching", "Hamstring Stretch", "Toe Touches", "Cat-Cow Stretch", "Shoulder Rolls"]

print("Welcome to the workout routine generator! 🏋️")

while True:
    workout_choice = input("Choose your workout routine type (Cardio/Strength/Flexibility): ").lower()
    try:
        if workout_choice not in workout_type:
            raise ValueError
        else:
            break
    except ValueError:
        print("Your choice is not a workout type. Let's try again...")

if workout_choice == "strength":
    rd_strength = rd.choice(strength)
    print(f"Try this exercices: {rd_strength} 💪")
elif workout_choice == "cardio" :
    rd_cardio = rd.choice(cardio)
    print(f"Try this exercices: {rd_cardio} 💪")
elif workout_choice == "flexibility":
    rd_flexibility = rd.choice(flexibility)
    print(f"Try this exercices: {rd_flexibility} 💪")
print("Stay active and keep moving! 🚀")



