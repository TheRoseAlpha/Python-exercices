if __name__ == '__main__':
    n = int(input())
    while True:
        integer_list = map(int, input().split())
        try:
            if (len(integer_list)  > n) or (len(integer_list) < n):
                raise ValueError
            else:
                break
        except ValueError:
            print("Non!")
    
    t = tuple(integer_list)
    print(hash(t))