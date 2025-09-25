# list_n = list((1, 2, 3))
# print(list_n)

# list_a = ["uno", "due", "tre"]
# print(list_a)
# for i in list_n, list_a:
#     print(i, i)

#-----------------------------------------------------------------


#even and odd with try/except
# while True:
#     try:
#         nbr = int(input("Insert a number please: "))
#         if(nbr%2 == 0):
#             print(f"{nbr} is an even number")
#             break
#         elif(nbr%2 == 1):
#             print(f"{nbr} is an odd number")
#             break
#         else:
#             raise Exception
#     except ValueError:
#         print("This is not an integer")


#-----------------------------------------------------------------

#vowel counter
# vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'i', 'O', 'U']

# vowelsCounter = 0
# consonantsCounter = 0
# word = input("Insert a word please: ")

# for x in word:
#     if(x in vowels):
#         vowelsCounter += 1
#     else:
#         consonantsCounter +=1

# print(f"There are {vowelsCounter} vowels and {consonantsCounter} consonants in {word}")


#-----------------------------------------------------------------

#factorials numbers
# def fact(n):
#     if(n == 0 or n == 1):
#         return 1
#     else:
#         return fact(n-1)*n
    
# n = int(input("insert an integer: "))

# print(fact(n))


#-----------------------------------------------------------------

#reverse list 
list_n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(list_n[0])
length = len(list_n)


# while True:
#     print(list_n[length-1])
#     length -= 1
#     if(length <= 0):
#         break

# while length >= 0:
#     print(list_n[length-1])
#     length -= 1
#     if(length <= 0):
#         break


#-----------------------------------------------------------------

#fizzbuzz

for i in range(1, 51):
    if i%3 == 0 and i%5 == 0:
        print(f"{i}: FizzBuzz")
    elif i%5 == 0:
        print(f"{i}: Buzz")
    elif i%3 == 0:
        print(f"{i}: Fizz")
