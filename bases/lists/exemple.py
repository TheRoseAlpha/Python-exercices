
# Les map permettent d'appliquer une fonction tout les elements d'un iterable pe une liste ou un tuple
# split() permet  de mettre les entrees dans une liste se basant sur les espaces

serie = list(map(int, input("Insert a serie of numbers").split()))

for i in serie:
    print(i)
print(serie)

# -----------------------------------------------------------------------

def division_per_2(value):
    return int(value/2)

my_list = [10, 20, 30, 40]

divided_per_2= list(map(division_per_2, my_list))
print(divided_per_2)

# ----------------------------------------------------------------------------