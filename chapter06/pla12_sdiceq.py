import random,sys
panel = [""]*9
answer = ["×"]*9
point = 0
raound = 1
def gameStart():
    for i in range(9):
        panel[i] = i + 1
    while answer != panel:
        sai1 = random.randint(1,6)
        sai2 = random.randint(1,6)
        sai = sai1 + sai2
        print(f"{sai1}と{sai2}が出ました")
        isGameOver = True
        isAns = False
        while sai > 0:
            print(f"合計は{sai}です")
            print(panel)
            isGameOver = True
            for i in panel:
                if i == "×" or i > sai:
                    pass
                else:
                    isGameOver = False
                    break
            if isGameOver and not isAns:
                print("ゲームオーバー")
                sys.exit()
            select = int(input("どの数字を選びますか？:"))
            if select == 0:
                sys.exit()
            elif select < 0:
                if isAns:
                    break
                else:
                    print("まだ答えていません")
                    continue
            if select > sai:
                print("数が足りません")
                continue
            elif panel[select - 1] == "×":
                print("既に選んでいます")
                continue
            panel[select - 1] = "×"
            isAns = True
            sai -= select
            if answer == panel:
                break
    print("クリア")
while True:
    print(f"ラウンド{raound}")
    gameStart()
    raound += 1
