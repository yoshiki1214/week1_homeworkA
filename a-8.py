users_info = [["Bob", 79], ["Tom", 59], ["Ken", 61]]

# ネスト構造からを並列構造に変換。それぞれnameとageに代入し出力
for user in users_info:
    name = user[0]
    age = user[1]
    print(f"Name: {name}, Age: {age}")
