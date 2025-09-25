#Prime number: 
#il numero stesso e uno

mlist = []
start = 100
for j in range(start):
    n = start
    div = n
    counter = 0
    for i in range(n):
        # print(n%div)
        if(n%div==0):
            # print(div)
            counter += 1
        div -= 1
    # print(f"final print {counter}")
    if(counter == 2):
        # print(f"{n} is a prime number")
        # print(n)
        mlist.append(n)
    start -= 1
# print(mlist[::-1])
mlist = mlist[::-1]
for i in range(len(mlist)):
    print(mlist[i])





    





















