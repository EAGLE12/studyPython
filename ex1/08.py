# 例外処理
lst = ["a", "b", "c", "d"]

try:
    n = lst.index("z")
    print(n, "番目にあります")
except ValueError:
    print("要素が見つかりません")
