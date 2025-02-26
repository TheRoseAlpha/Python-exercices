
# for i in range(5):
#     print("a"*(i+1))

"""
the first iteration it prints i(0)+1= 1 times a
the second line = second iteration,  it prints i (1)+1 = 2 times
and so on
"""

# n = 5 #the number of lines

# for i in range(5):
#     space = " " * (n-i-1) # 5-i-1 for the first iteration -> 5-0-1 = 4 spaces
#     stars = "*" * (2*i+1) #2*i+1 for the first iteration -> 2*0+1 = 1
#     print(space+stars)


"""
we know that for the first line we need 1 star for the seconde 1+2=3 and the next 3+2 = 5 star
So everytime we have to add 2 stars:
- fist line 2*0+1 = 1
- second line 2*1+1 = 3
- third line 2*2+1 = 5
- fifth line 2*3+1 = 7
"""

"""
TRIANGLE DE PASCAL:
- chaque ligne commence et fini par 1
- les chiffre du millieu sont le resultat de l'addition de deux chiffre addiacents
- prendre en compte une ligne i et un element de la ligne j
- 

"""

"""# list1 = [1]
n = 5

for i in range(5):
    space = " " * (n-i-1) #5-0-1 =4 premiere iteration
    number = "1" * (2*i+1)
    # number2 = "2"
    # print(space)
    # for j in range(i+1):
        # number2 = 
    print(space + number)

    # for j in range(i):
"""

n = 5
ligne_precedente = [1]
for i in range(5):
    space = " " * (n-i-1) #5-0-1 =4 premiere iteration
    number = "1" 
    print(space + f"{ligne_precedente[0]}")
