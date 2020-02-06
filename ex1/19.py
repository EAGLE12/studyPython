name = "Tom"
age = 23
point = 170.5
s = "{} is {} old and he got {}."
text = s.format(name, age, point)
print(text)

text2 = f"{name} is {age} old and he got {point}."
print(text2)

tokyo = 123456789
kyoto = 987654321

print(f"Tokyo: {tokyo:,}, Kyoto: {kyoto:,}")

length = 120
weight = 60.22
g = "長さ：{:.1f}，厚み：{:.0f}"
print(g.format(length, weight))

num1 = 123.44
num2 = 234.4422
num3 = 12.333

print(f"{num1:>10.1f}")
print(f"{num2:>10.1f}")
print(f"{num3:>10.1f}")
