from random import randint

while True:
    a = randint(1, 100)
    b = randint(1, 100) 
    c = randint(1, 100)
    if (a+b+c) == 20:
        break
print(a, b, c)