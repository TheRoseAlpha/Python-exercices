if __name__ == '__main__':
    # print("Hello World!")

    #list
    print("List")
    print("------------------")

    my_list = ["ananas", "banana", "orange", "blueberry"]
    my_list_2 = list((1, 2, 3))
    # print(my_list)


    # pour chaque element dans la liste, execute le bloc
    for x in my_list_2:
        print(f"This number {x}")

    print("------------------")

    for i in my_list:
        print(f"I love {i}")
    print("------------------")


    # pour le nombre d'element dans la liste, execute le bloc
    for j in range(len(my_list)):
        print(f"I hate {j}")
    print("------------------")

    print(my_list[::-1]) #reverse
    print(my_list[-1]) #blueberry
    print(my_list[-3])  #banana
    print("------------------")

    #-----------************--------------------
    #tuple

    print("Tuple")
    print("------------------")

    tup = ("ananas", "banana", "orange", "blueberry")
    print("------------------")

    for i in tup:
        print(f"I ate a/an {i}")
        # print(i)
    print("------------------")

    for j in range(len(tup)):
        print(f"I hate {j}")
    print("------------------")

    print(tup.index("banana"))
    print("------------------")

    print(tup)
    tup = list(tup)

    tup.append("raspberry")
    tup.append("lemon")
    tup.pop(2)
    
    tup=tuple(tup)

    print(tup)
    print("------------------")

    #-----------************--------------------
    #dictionary
    print("Dictionary")
    print("------------------")

    dic = {1 : "Lucia", 2:"Maria", 3 : "Rosa"}
    
    for i in dic:
        print(f"key {i} ")
    print("------------------") 
    

    for j in dic:
        print(f"value {dic[j]}")
    print("------------------")


    for x in dic:
        print(f" {x} : {dic[x]}")
        
    print("------------------")
    print(dic.items())

    print("------------------")
    print(dic.values())

    print("------------------")
    print(dic.keys())

    print("------------------")
    dic[5] = "Giulia"
    dic.update({6 : "Marco"})
    print(dic)












