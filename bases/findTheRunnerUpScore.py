if __name__ == '__main__':
    # my_list = [2, 3, 6, 6, 5]
    my_list = [57, 57, -57, 57]
    # my_list = list(set(my_list))

    max_1 = 0
    for i in range(1, len(my_list)):
        if my_list[i] > my_list[max_1]:
            max_1 = i
    if len(my_list) <= 2:
        print(my_list[max_1])
    elif len(my_list) > 2:
        my_list.pop(max_1)
        # for i in my_list:
        #     print(i)
        max2_ = 0
        for j in range(1, len(my_list)):
            if my_list[j] > my_list[max2_]:
                max2_ = j
        print(my_list[max2_])   

    # my_list = [57, 57, -57, 57]