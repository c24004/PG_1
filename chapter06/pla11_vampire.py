import random,sys
class Vampire:
    ground = ["D","M","K","〇","〇","〇"]
    under = ["C","V","M","S","〇","〇"]
    area = [ground,under]
    areaNum = 0
    isMap = []
    isKey = False
    cross = 0
    time = 14
    coin = 0
    stake = 0
    sanity = 8

    def __init__(self):
        random.shuffle(self.ground)
        random.shuffle(self.under)
        self.area = [self.ground,self.under]
        areaNum = 0
        self.isMap = [False,False]
        self.isKey = False
        self.cross = 0
        self.time = 14
        self.coin = 0
        self.stake = 0
        self.sanity = 8

    def Battle(self):
        print("ヴァンパイアが現れた！")
        input("勝負だ！")
        player = random.randint(1,6) + self.cross + self.stake
        cpu = random.randint(1,6)
        if self.coin >= 10:
            player -= 2
        print(f"p[{player}]:v[{cpu}]")
        if player > cpu:
            print("勝った")
            print(f"あなたは財宝{self.coin}ポイントを持ち帰った")
        elif player < cpu:
            print("負けた")
        else:
            print("引き分け")
        sys.exit()

    def GetKey(self,select):
        print("鍵を発見した")
        self.isKey = True
        self.area[self.areaNum][select] = "X"

    def GetMap(self,select):
        print("地図を入手した")
        self.isMap[self.areaNum] = True
        self.area[self.areaNum][select] = "X"

    def Entrance(self):
        print("地下への入り口だ")
        if(self.isKey):
            self.areaNum = 1 - self.areaNum
            print("地下へ移動した")
        else:
            print("鍵が必要だ")

    def GetCross(self,select):
        print("十字架を見つけた")
        self.cross = 3
        self.area[self.areaNum][select] = "X"

    def GetCoin(self,select):
        getCoin = random.randint(1,3)
        self.coin += getCoin
        self.area[self.areaNum][select] = "X"
        print(f"財宝を{getCoin}ポイント見つけました")
        print(f"手持ちは今{self.coin}ポイント")

    def GetStake(self,select):
        print("杭を見つけた")
        self.stake = 2
        self.area[self.areaNum][select] = "X"

    def SanityCheck(self,select):
        randomSanity = random.randint(1,10)
        if randomSanity > self.sanity or self.area[self.areaNum][select] == "V":
            print("恐ろしいものを見てしまった！")
            self.sanity -= 1
        print(f"現在の正気度{self.sanity}")
        if self.sanity == 0:
            print("正気を失った君はもう、探索はできなくなった")
            sys.exit()

    def Game(self):
        while True:
            if self.time == 24:
                self.Battle()
            elif self.time == 23 and self.stake != 0:
                print("杭の効力が失った！")
                self.stake = 0
            if self.isMap[self.areaNum]:
                print(self.area[self.areaNum])
            select = int(input("どのエリアを探索しますか？:")) - 1
            if select < 0:
                sys.exit()
            elif self.area[self.areaNum][select] == "K":
                self.GetKey(select)
            elif self.area[self.areaNum][select] == "M":
                self.GetMap(select)
            elif self.area[self.areaNum][select] == "D":
                self.Entrance()
            elif self.area[self.areaNum][select] == "C":
                self.GetCross(select)
            elif self.area[self.areaNum][select] == "V":
                self.Battle()
            elif self.area[self.areaNum][select] == "〇":
                self.GetCoin(select)
            elif self.area[self.areaNum][select] == "S":
                self.GetStake(select)
            else:
                print("何もなかった")
            self.SanityCheck(select)
            self.time += 1
            print(f"現在時刻{self.time}時")

vampire = Vampire()
vampire.Game()

