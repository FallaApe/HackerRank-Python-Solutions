if __name__ == '__main__':
    n = int(raw_input()) 
    integer_list = map(int, raw_input().split()) 
    print(hash(tuple(integer_list)))

#had to use python 2 caus hash variable was giving diff value in this environment
