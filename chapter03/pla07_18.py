import random,sys

#ジャンケンの出す手
hand = ("グー","チョキ","パー")

#それぞれの指の数
fingerNum = (0,2,5)

#注意書き
print("グー[1] : チョキ[2] : パー[3] : 終了[0]")

#出した手の指の数
playerFin = 18
cpFin = 18

cp_list = []

#ポイントの割り当て
playerPoint = 0
cpPoint = 0

#ポイントの数
point = 1

#プレイヤーの出す手を処理
def playerInt(playerFin):
    pI = input("ジャンケンポン:")
    if pI == "0":
        sys.exit()
    while pI not in ["1","2","3"]:
        pI = input("そんな手はない:")
    while playerFin - fingerNum[int(pI) - 1] < 0:
        pI = input("もうその手は使えない")
    return int(pI) - 1

#コンピューターが出す手を処理
def cpInt(cpFin):
    cp_list = random.randint(0,2)
    if cpFin - fingerNum[cp_list] < 0:
        cp_list = 0
    return cp_list

#ジャンケンの処理
for i in range(1,11):
    if i == 6 or i == 10:
        point += 1
    elif i == 7:
        point -= 1
    cp = cpInt(cpFin)
    cpFin -= fingerNum[cp]
    player = playerInt(playerFin)
    playerFin -= fingerNum[player]
    if hand[cp] == hand[player]:
        print(f"プレイヤー：{hand[player]}| コンピューター：{hand[cp]}")
    elif hand[cp - 1] == hand[player]:
        print(f"プレイヤー：{hand[player]}| コンピューター：{hand[cp]}")
        playerPoint += point
    elif hand[cp] == hand[player - 1]:
        print(f"プレイヤー：{hand[player]}| コンピューター：{hand[cp]}")
        cpPoint += point

#勝敗の処理
if cpPoint - cpFin < playerPoint - playerFin:
    print("プレイヤーの勝利")
elif cpPoint - cpFin > playerPoint - playerFin:
    print("コンピューターの勝利")
else:
    print("引き分け")
print(f"プレイヤー:点数[{playerPoint}]:残りの指[{playerFin}]")
print(f"コンピューター:点数[{cpPoint}]:残りの指[{cpFin}]")
