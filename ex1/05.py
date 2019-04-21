#乱数の発生

# 乱数発生が確定的
import random as rand
rand1 = rand.randrange(0,100)
print("確定的な乱数：%d" %rand1)

# 安全な乱数の発生
import secrets as rand_secu
rand2 = rand_secu.randbelow(100)
print("安全な乱数：%d" %rand2)
