numlist = [3, 4, 3.3, 33, "ee", 34, 20, 22]
sum = 0
for num in numlist:
    if not isinstance(num, (int, float)):
        print(num, "数値以外の値が含まれていました．")
        break
    sum += num
else:
    print("sum: ", sum)