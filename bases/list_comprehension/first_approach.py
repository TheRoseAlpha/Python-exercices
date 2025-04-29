'''
list comprehension allow us to fill a list without the for loop 
newlist = [expression for item in iterable if condition == True]

'''
# we want to have a list, based on the fruit one, containing the fruits with an 'a' in the name


#the for loop way
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
new = [] #empty list

for x in fruits:
    if 'a' in x:
        new.append(x)

print(new)


# the list comprehention way
new2 = [x for x in fruits if 'a' in x]
print(new2)


# set the value if its diff to banane and orange if its equal to banana
new3 = [x if x != "banana" else "orange" for x in fruits]
print(new3)
