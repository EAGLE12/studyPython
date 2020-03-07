from random import randint
miss = 0
correct = 0
print("QUESTION!|3 times wrong or push q finish")

while miss < 3:
    a = randint(1, 100)
    b = randint(1, 100)
    ans = a + b
    question = f"{a}+{b}--->>>"
    value = input(question)

    if value == "q":
        break
    if value == str(ans):
        correct += 1
        print("correct!")
    else:
        miss += 1
        print("wrong your answer!", "*"*miss)

print("-"*20)
print("correct: ", correct)
print("miss: ", miss)
