import random,sys
t = ["グー","チョキ","パー"]
print("グー[1] | チョキ[2] | パー[3] | 終了[0]")
def playerInt():
    pI = input("ジャンケンポン:")
    if pI == "0":
        sys.exit()
    while pI not in ["1","2","3"]:
        pI = input("そんな手はない:")
    return int(pI) - 1
cpNum = 0
playerNum = 0
for i in range(1,11):
    cp = random.randint(0,2)
    player = playerInt()
    if t[cp] == t[player]:
        print(f"プレイヤー：{t[player]}| コンピューター：{t[cp]}")
    elif t[cp - 1] == t[player]:
        print(f"プレイヤー：{t[player]}| コンピューター：{t[cp]}")
        playerNum += 1
    elif t[cp] == t[player - 1]:
        print(f"プレイヤー：{t[player]}| コンピューター：{t[cp]}")
        cpNum += 1
if cpNum < playerNum:
    print("プレイヤーの勝利")
elif cpNum > playerNum:
    print("コンピューターの勝利")
else:
    print("引き分け")
