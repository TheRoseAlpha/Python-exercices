#1 reverse
tuple1 = (10, 20, 30, 40, 50)

print(tuple1[::-1])


#2 Access value 20 from the tuple
tuple1 = ("Orange", [10, 20, 30], (5, 15, 25))

print(tuple1[1][1])

#3 single item tuple
tuple2 = (50)
print(tuple2)

#4 Unpack the tuple into 4 variables
tuple1 = (10, 20, 30, 40)
# a = tuple1[0]
# b = tuple1[1]
# c = tuple1[2]
# d = tuple1[3]
# do that instead
a, b, c, d = tuple1

print(a) # should print 10
print(b) # should print 20
print(c) # should print 30
print(d) # should print 40

# 5 Swap two tuples in Python
tuple1 = (11, 22)
tuple2 = (99, 88)

# temp = tuple1
# tuple1 = tuple2
# tuple2 = temp
# instead do...
tuple1, tuple2 = tuple2, tuple1


print(tuple1)
print(tuple2)

# 6: Copy specific elements from one tuple to a new tuple

tuple1 = (11, 22, 33, 44, 55, 66)

tuple2 = tuple1[3:5]
print(f"Tuple2 : {tuple2}")


# 7: Modify the tuple
tuple1 = (11, [22, 33], 44, 55)

tuple1[1][0] = 222
print(f"Tuple1 : {tuple1}")

# Exercise 8: Sort a tuple of tuples by 2nd item
tuple1 = (('a', 23),('b', 37),('c', 11), ('d',29))

tuple1 = tuple(sorted(list(tuple1), key=lambda x: x[1])) # key function (lambda x: x[1]), ce qui signifie que le tri se fait en fonction du deuxième élément de chaque élément du tuple.
print(tuple1)

# 9: Counts the number of occurrences of item 50 from a tuple
tuple1 = (50, 10, 60, 70, 50)

print(tuple1.count(50))


# 10: Check if all items in the tuple are the same

def check(t):
    return all(i == t[0] for i in t)

tuple1 = (45, 45, 45, 45)
print(check(tuple1))