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

# nb: Appena una condizione è vera, il resto non viene più controllato.
# Quindi l’ordine in cui scrivi le condizioni cambia il risultato.

for i in range(1, 51):
    if i%3 == 0 and i%5 == 0: #casp prioritario
        print(f"{i}: FizzBuzz")
    elif i%5 == 0:
        print(f"{i}: Buzz")
    elif i%3 == 0:
        print(f"{i}: Fizz")
