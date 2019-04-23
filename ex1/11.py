# リストの複製
import copy
lst1 = [3,4,6,7,2,6,8,4]
lst2 = copy.copy(lst1)
print("lst1: ",lst1)
print("lst2: ",lst2)
lst1.sort() # リストごと書き換えられる
print("sort: ",lst1)
lst2_sort = sorted(lst2)
lst2_sort_reverse = sorted(lst2, reverse=True)
print("sort: ",lst2_sort)
print("sort: ",lst2_sort_reverse)

