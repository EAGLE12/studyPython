# 辞書型
dic = {"1":"Tom", "2":"Jhon", "3":"Sam", "4":"David"}

try:
    result = dic["8"]
    print(result)
except KeyError:
    print("リストにありません．")
