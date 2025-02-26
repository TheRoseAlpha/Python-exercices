list_1 = []

# ceci ne marche pas, le list est vide donc la boucle ne s'execute pas
# meme si la list n'etait pas vide la boucle n'allait pas non plus d'executer
# parce que i se refere a la valeur a l'interieur de la list
# for i in list_1:
#     list[i] = i+1 

for i in range(10):
    list_1.append(i+1)
print(list_1)

list_1= list_1[5:9]
print(list_1)

print(len(list_1)) #4 apres l'extraction