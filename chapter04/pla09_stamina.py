import random,sys

#合計のマス、ゴールのマス
goalMass = 30

#それぞれの所持金
gold = [10,10]

#それぞれのスタミナ
stamina = [6,6]

#それぞれの現在地
nowMass = [1,1]
icon = ["〇","P","C","㍶"]

#今のターン
nowTurn = 0

#プレイヤーの名前
name = [input("名前は何ですか："),"CPU"]

#配置
playerMass = []
for i in range(goalMass):
    playerMass.append(icon[0])

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
    if i == 0 or i + 1 == goalMass:
        allMass.append(effects[0])
    else:
        x = random.randint(0,len(effects) - 1)
        allMass.append(effects[x])
print(*allMass,sep = " ")

#休みのフラグ
isCoolDown = [False,False]

#初期配置
playerMass[nowMass[nowTurn] - 1] = icon[3]
print(*playerMass,sep = " ")

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
    print(f"{name[0]}：[{gold[0]}]ゴールド｜スタミナ[{stamina[0]}]")
    print(f"CPU：[{gold[1]}]ゴールド｜スタミナ[{stamina[1]}]")

#ほんへ
while nowMass[1 - nowTurn] != goalMass:
    print(f"「{name[nowTurn]}」の番です")

    #休みだったら相手の番にする
    if isCoolDown[nowTurn]:
        print(f"{name[nowTurn]}は休んだ")
        if stamina[nowTurn] + 3 > 6:
            stamina[nowTurn] = 6
        else:
            stamina[nowTurn] += 3
        print(f"現在のスタミナ{stamina[nowTurn]}")
        input("------------------")
        isCoolDown[nowTurn] = False
        nowTurn = 1 - nowTurn
        continue
    
    #サイコロを振る、食事をする、ゲーム終了する
    print(f"残りスタミナ：{stamina[nowTurn]}")
    print(f"所持金：{gold[nowTurn]}ゴールド")
    if nowTurn == 0:
        saikoro = input("サイコロを振るか食事をする")
        if saikoro == "0":
            sys.exit()
        elif saikoro == "1":
            if gold[nowTurn] > 0:
                print("あなたは食事を取った")
                stamina[nowTurn] = 6
                gold[nowTurn] -= 1
                print(f"{name[nowTurn]}の所持金は{gold[nowTurn]}ゴールド")
                input("------------------")
                nowTurn = 1 - nowTurn
                continue
            else:
                input("金貨がないため、食料を買えない")
    else:
        if nowMass[0] < nowMass[1] or stamina[nowTurn] == 6:
            input("CPUはサイコロを振った")
        else:
            input("CPUは充電する")
            if gold[nowTurn] > 0:
                stamina[nowTurn] = 6
                gold[nowTurn] -= 1
                print(f"CPUの所持金は{gold[nowTurn]}ゴールド")
                input("------------------")
                nowTurn = 1 - nowTurn
                continue
            else:
                input("しかし、電池を持っていなかったようだ")

    #前のターンの位置を消去
    playerMass[nowMass[nowTurn] - 1] = icon[icon.index(playerMass[nowMass[nowTurn] - 1]) - (nowTurn + 1)]

    #進む
    move = random.randint(1,stamina[nowTurn])
    print(f"{move}がでた")
    if move + nowMass[nowTurn] > goalMass:
        nowMass[nowTurn] = goalMass - ((move + nowMass[nowTurn]) - goalMass)
    else:
        nowMass[nowTurn] += move
    stamina[nowTurn] -= move
    
    #スタミナは最低値：１
    if stamina[nowTurn] <= 0:
        stamina[nowTurn] = 1
    
    playerMass[nowMass[nowTurn] - 1] = icon[icon.index(playerMass[nowMass[nowTurn] - 1]) + (nowTurn + 1)]
    print(*playerMass,sep = " ")
    
    #特殊な効果のマス（金貨、マス変化、一回休み）
    if allMass[nowMass[nowTurn] - 1] == effects[1] or allMass[nowMass[nowTurn] - 1] == effects[2]:
        gold[nowTurn] = goldMass(gold[nowTurn],allMass[nowMass[nowTurn] - 1])
    elif allMass[nowMass[nowTurn] - 1] == effects[3] or allMass[nowMass[nowTurn] - 1] == effects[4] or allMass[nowMass[nowTurn] - 1] == effects[5]:
        playerMass[nowMass[nowTurn] - 1] = icon[icon.index(playerMass[nowMass[nowTurn] - 1]) - (nowTurn + 1)]
        nowMass[nowTurn] = position(nowMass[nowTurn],allMass[nowMass[nowTurn] - 1])
        playerMass[nowMass[nowTurn] - 1] = icon[icon.index(playerMass[nowMass[nowTurn] - 1]) + (nowTurn + 1)]
        print(*playerMass,sep = " ")
    elif allMass[nowMass[nowTurn] - 1] == effects[6]:
        isCoolDown[nowTurn] = True
        print("一回休み")
    
    #相手のターンへ
    nowTurn = 1 - nowTurn
    input("------------------")

finish()
