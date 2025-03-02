# listp = ["z11", "a0", ["b1", "b2", ["b12", ["b13"]]], "c3"]
listp = []
for i in range(3):
    listp.append([])
print(listp)
# for i in range(len(listp)):
listp[0][0] = 12
print(listp)



# if __name__ == '__main__':
#     for _ in range(int(input())):
#         name = input()
#         score = float(input())
#         nest_list = [name, score]
#         for i in nest_list:
#             print(i)