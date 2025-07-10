import random,sys
num = random.randint(1,10)
life = 10
point = 5
missCount = 0
print("ゲームを終わるには[0]と入力")
while life != 0:
    select = int(input("1~10の数字を割り当ててください："))
    if select == 0:
        print("ゲームをやめる")
        sys.exit()
    elif select > num:
        print("数字が大きいです")
    elif select < num:
        print("数字が小さいです")
    else:
        print("当たりです！")
        point += 10
        num = random.randint(1,10)
        life -= 1
        missCount = 0
        print(f"ライフ[{life - missCount}/{life}]:ポイント[{point}]")
        continue
    point -= 1
    missCount += 1
    print(f"ライフ[{life - missCount}/{life}]:ポイント[{point}]")
    if missCount == life:
        print("終了")
        sys.exit()
print(f"最終ポイントは[{point}]です")
