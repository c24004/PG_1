import random,sys

#合計のマス、ゴールのマス
goalMass = 30

#それぞれの所持金
gold = [5,5]

#それぞれの現在地
nowMass = [1,1]

#今のターン
nowTurn = 0

#プレイヤーの名前
name = [input("プレイヤー１："),input("プレイヤー２：")]

#プレイヤーの配置
playerMass = [i - i for i in range(goalMass)]

#全てのマスの効果
effects = ["N","G","L","P","B","S","C"]
print(f"""
      普通のマス:{effects[0]}
      金貨ゲット:{effects[1]}
      金貨ロス　:{effects[2]}
    　Xマス進む :{effects[3]}
      Xマス戻る :{effects[4]}
      ふりだし  :{effects[5]}
      一回休み　:{effects[6]}
      """)
allMass = []
for i in range(goalMass):
    x = random.randint(0,len(effects) - 1)
    if i == 0 or i + 1 == goalMass:
        allMass.append(effects[0])
    else:
        allMass.append(effects[x])
print(*allMass,sep = ",")

#休みのフラグ
isCoolDown = [False,False]

#初期配置
playerMass[nowMass[nowTurn] - 1] = 3
print(playerMass)

#金貨に関するマスの処理
def goldMass(gold,mass):
    change = random.randint(1,3)
    if mass == effects[1]:
        gold += change
        print(f"所持金が{change}増えました")
    else:
        gold -= change
        print(f"所持金が{change}減りました")
    print(f"{name[nowTurn]}の所持金は{gold}ゴールド")
    return gold

#マス変化に関するマスの処理
def position(nowMass,mass):
    if mass == effects[3]:
        change = random.randint(1,3)
        if nowMass + change > goalMass:
            nowMass = goalMass - ((change + nowMass) - goalMass)
        else:
            nowMass += change
        print(f"{change}進む")
    elif mass == effects[4]:
        change = random.randint(1,3)
        if nowMass - change < 1:
            nowMass = 1
        else:
            nowMass -= change
        print(f"{change}戻る")
    else:
        nowMass = 1
        print("スタートに戻る")
    return nowMass

#ゲーム終了の処理
def finish():
    print(f"{name[1 - nowTurn]}がゴールしました")
    print(f"{name[0]}：{gold[0]}ゴールド｜{name[1]}：{gold[1]}ゴールド")

#ほんへ
while nowMass[1 - nowTurn] != goalMass:
    print(f"「{name[nowTurn]}」の番です")

    #休みだったら相手の番にする
    if isCoolDown[nowTurn]:
        input("休みです")
        print("------------------")
        isCoolDown[nowTurn] = False
        nowTurn = 1 - nowTurn
        continue
    
    #前のターンの位置を消去
    playerMass[nowMass[nowTurn] - 1] -= nowTurn + 1
    
    #サイコロを振る、ゲーム終了する
    if input("サイコロを振る") == "0":
        sys.exit()
    move = random.randint(1,6)
    print(f"{move}がでた")
    if move + nowMass[nowTurn] > goalMass:
        nowMass[nowTurn] = goalMass - ((move + nowMass[nowTurn]) - goalMass)
    else:
        nowMass[nowTurn] += move
    playerMass[nowMass[nowTurn] - 1] += nowTurn + 1
    print(playerMass)
    
    #特殊な効果のマス（金貨、マス変化、一回休み）
    if allMass[nowMass[nowTurn] - 1] == effects[1] or allMass[nowMass[nowTurn] - 1] == effects[2]:
        gold[nowTurn] = goldMass(gold[nowTurn],allMass[nowMass[nowTurn] - 1])
    elif allMass[nowMass[nowTurn] - 1] == effects[3] or allMass[nowMass[nowTurn] - 1] == effects[4] or allMass[nowMass[nowTurn] - 1] == effects[5]:
        playerMass[nowMass[nowTurn] - 1] -= nowTurn + 1
        nowMass[nowTurn] = position(nowMass[nowTurn],allMass[nowMass[nowTurn] - 1])
        playerMass[nowMass[nowTurn] - 1] += nowTurn + 1
        print(playerMass)
    elif allMass[nowMass[nowTurn] - 1] == effects[6]:
        isCoolDown[nowTurn] = True
        print("一回休み")
    
    #相手のターンへ
    nowTurn = 1 - nowTurn
    print("------------------")

finish()
