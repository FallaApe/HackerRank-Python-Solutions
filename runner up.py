if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))

    largest = arr[0]

    for i in arr:
        if i > largest:
            largest = i

    sec = -9999

    for i in arr:
        if i > sec and i < largest:
            sec = i

    print(sec)       
     
