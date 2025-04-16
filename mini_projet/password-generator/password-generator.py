if __name__ == '__main__':

    special_car = ["@, #, $"]
    number = [x for x in range(0, 10)]
    upper_char = [chr(i) for i in range(65, 91)]
    lower_char = [chr(i) for i in range(97, 123)]

    # print(upper_char)
    # print(lower_char)

    # while True:
    #     try:
    #         pw = input("Hi user, insert your password: ")
    #         if len(pw) <= 8:
    #             raise Exception
    #         else:
    #             print("Nice you welcome on your profile")
    #             break
    #     except Exception:
    #         print("Your password must be longer then 8 caractere")

    # print("Nice you welcome on your profile")
    

    pw = input("Hi user, insert your password: ")
    print(pw.split())

    # if (f'{special_car[0]}' or f'{special_car[1]}' or f'{special_car[2]}') not in pw.split():
    #     print("at least a number")



    # print(len(pw))

    # if len(pw) <= 8:
    #     print("nope")
    # else:
    #     print("yeah")

