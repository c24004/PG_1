import random
num = random.randint(1,10)
life = 10
while life != 0:
    select = int(input("1~10の数字を割り当ててください："))
    if select > num:
        print("数字が大きいです")
    elif select < num:
        print("数字が小さいです")
    else:
        print("当たりです！")
        break
    life -= 1
    if life == 0:
        print("残念です！")
