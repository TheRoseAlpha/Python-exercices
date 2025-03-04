if __name__ == '__main__':
    # my_list = [2, 3, 6, 6, 5]
    my_list = [57, 57, -57, 57]
    max_1 = 0
    for i in range(1, len(my_list)-1):
        if my_list[i] > my_list[max_1]:
            max_1 = i
        elif my_list[i] == my_list[max_1]:
            my_list.pop(max_1)
        print(my_list[i])
        
    my_list.pop(max_1)
        
    max2_ = 0
    for j in range(1, len(my_list)):
        if my_list[j] > my_list[max2_]:
            max2_ = j
    print(my_list[max2_])   

    my_list = [57, 57, -57, 57]