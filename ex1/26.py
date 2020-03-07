names = ["田中太郎", "岡山太郎", "石田三木", "桜井翔"]
name = "太郎"
result = False
for item in names:
    if name in item:
      result = True
      break
print(result)  