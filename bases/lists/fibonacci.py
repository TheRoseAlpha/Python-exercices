def fibo(nbr):
    list_1 = [0, 1]
    if nbr==0:
        return [0]
    elif nbr==1:
        return list_1
    for i in range(2, nbr+1):
        list_1.append(list_1[-1] + list_1[-2])#ajoute les deux dernier elements
    return list_1


print(fibo(8))
