# データ構造のシャッフル

import random
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
random.shuffle(a)
print(a)

s = "abcdefghijk"
t = list(s)
random.shuffle(t)

print("".join(t))
