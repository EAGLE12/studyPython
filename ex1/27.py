city = input("調べる地名：")
members = {"東京":21, "大阪":23, "名古屋":24, "横浜":25, "福岡":26}

try:
    value = members[city]
    print(f"{city} の値は {value}です．")
except KeyError:
    print(f"{city} はありません．")
except Exception as error:
    print(error)