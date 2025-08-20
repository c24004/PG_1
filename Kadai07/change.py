money = int(input("お釣りはいくらですか:"))
one = money % 10
ten = (money % 100) // 10
hun = money // 100
print(f"100円玉{hun}枚, 10円玉{ten}枚, 1円玉{one}枚")
