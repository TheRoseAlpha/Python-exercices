import random as rd

right_number = rd.randint(1, 100)
attempts = 0

while True:
    guest_number = int(input("Guest the number: "))
    if right_number == guest_number:
        if attempts < 3:
            print("Good! This is the right number, you did it at the first attempt😊")
        else:
            print(f"Nice after {attempts} attempts you did it 🤪")

        break
    elif right_number > guest_number:
        print("Wrong! The number is higher, try again")
        attempts += 1

    elif right_number < guest_number:
        print("Wrong! The number is lower, try again")
        attempts += 1
