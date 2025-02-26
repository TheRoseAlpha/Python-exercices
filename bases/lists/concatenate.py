list_1 = [1, 2, 3, 4]
list_2 = [10, 20, 30, 40]
list_3 = list_1+list_2

print(list_1)
print(list_2)
print(list_3)

# extend modifie directement la list comme append et donc reoutne none
new_list = [11, 22, 33, 44]
new_list2 = [1, 2, 3, 4]
new_list.extend(new_list2)
print(new_list)


# append et nested list
new_list3 = [11, 22, 33, 44]
new_list4 = [1, 2, 3, 4]
result_list = new_list3.append(new_list4)  #append modifie directement la list donc pas besoin de la mettre dans une autre, il retourne none
print(new_list)
print(result_list) #affiche none7


#copy of a list
# other_list = new_list3.copy()
# print(other_list)

#edit list in function
# def list_edit(list):
#     for i in range(len(list)):
#         list[i] = f"banane{i}"


# list_edit(new_list3)
# print(new_list3)

#list comprehension
# list_12 = [2*i+1 for i in list_1] #pour i = 1, 2, 3, 4 -> les valeurs de la list_1
# list_13 = [2*i+1 for i in range(len(list_1))] #pour i = 0, 1, 2, 3 -> la longeur de list_1 a partir de 0


# print(list_12)
# print(list_13)