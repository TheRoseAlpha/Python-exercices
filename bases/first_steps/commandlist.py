# Consider a list (list = []). You can perform the following commands:

# insert i e: Insert integer e at position i.
# print: Print the list.
# remove e: Delete the first occurrence of integer e.
# append e: Insert integer e at the end of the list.
# sort: Sort the list.
# pop: Pop the last element from the list.
# reverse: Reverse the list.
# Initialize your list and read in the value of n followed by n lines 
# of commands where each command will be of the 7 types listed above. 
# Iterate through each command in order and perform the corresponding operation on your list.

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