for i in range(2, 100):
    j = 2
    count = 0
    while j < i:
        if i % j == 0:
            count = 1
            j = j + 1
        else:
            j = j + 1
    if count == 0:
        print(str(i)+ "is a prime number.")
    else:
        count = 0
        