if __name__ == '__main__':
    N = int(input())
    list = []
    
    
    
    for i in range(N): #tant qu'on est dans la taille du tableau
        command , *values = input().split()
        
        if command == 'insert':
            list.insert(int(values[0]), int(values[1]))
        elif command == 'print':
            print(list)
        elif command == 'remove':
            list.remove(int(values[0]))
        elif command == 'append':
            list.append(int(values[0]))
        elif command == 'sort':
            list.sort()
        elif command == 'pop':
            list.pop()
        elif command  == 'reverse':
            list.reverse()