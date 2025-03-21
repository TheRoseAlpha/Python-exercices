# https://www.youtube.com/watch?v=4TZ1K8EHT2M


# name = input("What's your name? ")

# print(f"Hi {name} now you can begin the quiz")


questions_dic = {
    "What is the capital of France? " : ["Paris", "Berlin", "Madrid", "Rome"],
    "Which planet is known as the Red Planet? " : ["Venus", "Mars", "Jupiter", "Saturn"],
    "How many continents are there on Earth? " : [7, 5, 6, 8],
    "Who wrote the play Romeo and Juliet? " :  ["Charles Dickens", "William Shakespeare", "Mark Twain", " J.K. Rowling"],
    "What is the chemical symbol for Gold? " :  ["Ag", "Fe", "Au", "Pb"], 
    "Which element has atomic number 1" : ["Oxygen", "Hydrogen", "Helium", "Carbon"]
}

user_point = 0

for question, answers in questions_dic.items():
    correct_answer = answers[0]
    sorted_answers = sorted(answers)

    print(question)

    for label, answers in enumerate(sorted_answers, start=1):
        print(f"  {label}) {answers}")

    selected_number = int(input("Response: "))
    selected = sorted_answers[selected_number-1]

    if selected == correct_answer:
        user_point = user_point + 1
        print(f"Right answer! You have earn {user_point} points")
    elif selected != correct_answer:
        print(f"Worg answer. The correct answer is {correct_answer}")

if user_point > 3:
    print(f"End of the quiz, your total point is {user_point}. Good job!")
else:
    print(f"End of the quiz, your total point is {user_point}. You can try again if you want to!")

    
    