import random,sys
num = random.randint(1,10)
life = 5
print("ゲームを終わるには[0]と入力")
while life != 0:
    select = int(input("1~10の数字を割り当ててください："))
    if select == 0:
        print("ゲームをやめる")
        sys.exit()
    elif select > num:
        print("数字が大きいです")
        life -= 1
    elif select < num:
        print("数字が小さいです")
        life -= 1
    else:
        print("当たりです！")
        life += 10
        num = random.randint(1,10)
    print(f"現在のライフ[{life}]")
print("残念です！")
