# if you enter a number it print what number you printed
# if you enter another caracter it raise the exception valueerror and print the error message
'''try:
    x = int(input("Enter an integer please: "))
    print(f"You enter {x}")
except ValueError:
    print("This is not a number")'''

# var = input("").lower()
# print(var)

this_list = ["francais", "english", "italiano", "spanish"]
while True:
    choice = input("Choose a language: ").lower() #converti l'entree de l'utilisateur en minuscule comme ca ca passe toujours 👍😃
    try:
        if choice not in this_list:
            raise Exception
        else:
            break
    except Exception:
        print("You should try again, and put an available language!")
        
print(f"Nice now you can speak {choice}")
        