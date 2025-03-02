import time

if __name__ == '__main__':
    birth_year = int(input("Insert your year of date please: "))
    current_year = int(time.strftime("%Y"))

    age = current_year - birth_year
    print(f"Now you are {age} years old 😊")

