import sys

day = 7

commandCount = 4

#dirtCount = 1

status = {"hungry":10,"mood":10}

def action(command):
    if command == 1:
        status["hungry"] += 2
    elif command == 2:
        status["hungry"] -= 1
    elif command == 3:
        status["hungry"] -= 1
        status["mood"] += 1
    else:
        status["hungry"] -= 2
        status["mood"] += 2
    
    if status["hungry"] > 10:
        status["hungry"] = 10
    elif status["mood"] > 10:
        status["mood"] = 10

    return status["hungry"],status["mood"]

def gameOver(name):
    if status["hungry"] <= 0:
        print(f"{name}はあなたを食べてしまった")
        sys.exit()
    elif status["mood"] <= 0:
        print(f"{name}はあなたを燃やした")
        sys.exit()

def gameStart(commandCount):
    dirtCount = 1
    name = input("ドラゴンに名前を付けよう：")
    for d in range(day):
        sleep = False
        walk = False
        cleaning = False
        dirtFlag = False
        foodCount = 3
        print(f"{d + 1}日目")
    
        for i in range(commandCount):
            print("""
            1 食事：満腹度＋２
            2 掃除：満腹度－１、機嫌度の減少を１に戻します
            3 散歩：満腹度－１、機嫌度＋１
            4 睡眠：満腹度－２、機嫌度＋２
            0 逃亡：このゲームを終了する
            """)
        
            while True:
                command = input("コマンドを選択してください")
            
                if command == "0":
                    print("あなたはどさくさに紛れて逃げ出した")
                    sys.exit()
            
                elif command == "1":
                    if foodCount > 0:
                        print(f"{name}に食事を与えた")
                        foodCount -= 1
                        walk = False
                        cleaning = False
                    else:
                        print(f"{name}はお腹いっぱいだ")
                        continue
                elif command == "2":
                    if not cleaning:
                        print(f"{name}の部屋を掃除する")
                        walk = False
                        cleaning = True
                        dirtFlag = True
                        dirtCount = 1
                    else:
                        print(f"しかし、{name}の部屋はピカピカだ")
                        continue
                elif command == "3":
                    if not walk:
                        print(f"{name}と散歩をした")
                        walk = True
                        cleaning = False
                    else:
                        print(f"{name}は疲れている")
                        continue
                elif command == "4":
                    print(f"{name}を寝かしつけた")
                    walk = False
                    cleaning = False
                    sleep = True
            
                else:
                    continue

                status["hungry"],status["mood"] = action(int(command))
                break
        
            print(f'満腹度:{status["hungry"]}　機嫌度:{status["mood"]}')
            gameOver(name)

        if not dirtFlag:
            print(f"{name}の部屋が汚れている")
            if dirtCount == 1:
                status["mood"] -= 1
            else:
                status["mood"] -= dirtCount * 3
            dirtCount += 1
            print(f'満腹度:{status["hungry"]}　機嫌度:{status["mood"]}')

        if foodCount == 3:
            print(f"{name}はお腹を空かせている")
            status["hungry"] -= 3
            print(f'満腹度:{status["hungry"]}　機嫌度:{status["mood"]}')

        if not sleep:
            print(f"{name}は寝不足だ")
            status["mood"] -= 3
            print(f'満腹度:{status["hungry"]}　機嫌度:{status["mood"]}')
        gameOver(name)
        input("________________")
    print(f"""
        {name}は巣立ちした
        近くにタマゴが落ちてる
        どうする？
        """)
        
    if input("1:ハードモード　ENTER:諦める") == "1":
        print("ヒナが生まれた")
        print(f"コマンドが{commandCount - 1}回になりました")
        status["hungry"] = 10
        status["mood"] = 10
        gameStart(commandCount - 1)
    else:
        print("あなたはスクランブルエッグを食べた")

if input("[0]で説明を飛ばす：") == "0":
    pass
else:
    print("""
      突然ですが、ドラゴンを7日間預かることになりました
ドラゴンを飢えさせたり怒らせたりしないよう、ちゃんと世話をしないといけません
    """)

    input("7日間、世話するコマンドを入力し、ドラゴンのステータスを変化させます")

    input("1日につき4回コマンドを入力できます")

    input("""
ドラゴンのステータスは満腹度と機嫌度の2つあり、どちらも初期値は10です
また、どちらも10が上限値です
    """)

    input("ステータスがどちらでもゼロ以下になったら即ゲームオーバーです")

    input("ドラゴンは毎日うんちをします。掃除をしておかないと機嫌度の減少が3倍になり、その効果は累積していきます")

    input("コマンドは食事/掃除/散歩/睡眠の4つです")

    input("""
[1日の各コマンドの実行には制限があります]
・食事は1日最大3回までです
・掃除は連続して実行できません(途中に別のコマンドを挟むのは可)
・散歩は連続して実行できません(途中に別のコマンドを挟むのは可)
    """)
    
    input("""
[1日に1度も食事や睡眠を与えないと、さらにステータスが減少します]
・まる1日食事を与えない：満腹度－３
・まる1日睡眠を与えない：機嫌度－３
    """)

gameStart(commandCount)
