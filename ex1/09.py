def isEven(n):
    return(n % 2 == 0)

def isOdd(n):
    return(n % 2 != 0)

lst = [1,2,3,4,5,6,7,8,9,10,11]
print("list: ", lst)

count = len(list(filter(isEven, lst)))
print("偶数の要素の数：", count)

count = len(list(filter(isOdd, lst)))
print("奇数の要素の数：", count)
