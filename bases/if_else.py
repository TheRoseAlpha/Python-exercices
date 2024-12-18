import random

if __name__ == '__main__':
    n = random.randint(1, 100)
    print (n)
    if n%2 == 1:
        print("Weird")
    elif n%2 == 0:
        if n in range(2, 6):
            print("Not Weird")
        elif n in range(6, 21):
            print("Weird")
        elif n > 20 and n <= 100:
            print("Not Weird")