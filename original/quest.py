import random

#==========キャラクタークラス==========#
class Chara:
    def __init__(self,name,hp,attack,defense,condition):
        self.name = name
        self.maxHp = hp
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.condition = condition
        self.isAlive = True

    def hitDamage(self,damage):
        d = max(1,int((damage / 2) - (self.defense / 4) + random.randint(0,3)))
        self.hp = max(0, self.hp - d)
        input(f"{self.name}に{d}ダメージ！")

    def die(self):
        self.isAlive = False

#==========アイテム==========#
class Item:
    def __init__(self, name):
        self.name = name

    def use(self, player,chara):
        pass

class Bandage(Item):
    def __init__(self,name):
        super().__init__(name)
        self.heel = 10

    def use(self,player,chara):
        player.hp = min(player.maxHp, player.hp + self.heel)
        print("====================")
        input(f"{player.name}の体力が{self.heel}回復した")
        player.item.remove(self)

#==========人格ヘルメット==========#
class Helmet(Item):
    def __init__(self,name):
        super().__init__(name)

    def use(self,player,chara):
        print("====================")
        input("あなたはヘルメットを被った")
        input("あなたは人格を乗っ取られてしまった………")
        player.name = "トスケ"
        player.die()

#==========ヨウカゲの邪悪箱==========#
class EvilBox(Item):
    def __init__(self,name):
        super().__init__(name)
        self.isYoukage = True
        self.charaList = ["ノウゼン","ノリミケ"]

    def use(self,player,chara):
        print("====================")
        input("邪悪箱をコツンっとたたいた")
        if self.isYoukage and chara.name in self.charaList:
            print("中からヨウカゲが飛び出してきた！")
            input("ヨウカゲ「ここは任せろ……」")
            chara.die()
            self.isYoukage = False
            input("ヨウカゲが敵を一掃した！")
            return
        input("しかし何も起きない……")

#==========ヒカリの腕輪==========#
class Bracelet(Item):
    def __init__(self,name):
        super().__init__(name)
        self.isFriend = False

    def use(self,player,chara):
        print("====================")
        if any(isinstance(h, HelperHikari) for h in player.helper):
            input("私はここだよ！")
            return
        if self.isFriend:
            player.helper.append(HelperHikari("ヒカリ"))
            input("呼んだ？")
        else:
            print("腕輪を装備した")
            input("その瞬間閃光が走り、何かが飛び出てきた！")
            print("ヒカリ「私はヒカリよろしくね！」")
            player.helper.append(HelperHikari("ヒカリ"))
            self.isFriend = True
            input("ヒカリが仲間になった！")

#==========ナイの大発明==========#
class Gun(Item):
    def __init__(self,name):
        super().__init__(name)
        self.isBreak = False

    def use(self,player,chara):
        print("====================")
        if self.isBreak:
            input("しかし、壊れて使えない……")
        else:
            input("ビームを撃った！")
            chara.hit(30)
            self.name = "壊れたビームがン"
            self.isBreak = True

class HeelBox(Item):
    def __init__(self,name):
        super().__init__(name)
        self.isBreak = False

    def use(self,player,chara):
        print("====================")
        if self.isBreak:
            input("しかし、壊れて使えない……")
        else:
            input("ヒールボックスを使用した")
            player.hp = min(player.maxHp,player.hp + 20)
            print(f"{player.name}のHPが20回復した")
            self.name = "壊れたヒールボックス"
            self.isBreak = True

class Goggle(Item):
    def __init__(self,name):
        super().__init__(name)
        self.isBreak = False

    def use(self,player,chara):
        print("====================")
        if self.isBreak:
            input("しかし、壊れて使えない……")
        else:
            input("---分析中---")
            print("====================")
            print(f"名称:{chara.name}")
            input(f"行動:{chara.actList}")
            self.name = "壊れたサーチゴーグル"
            self.isBreak = True

#==========エリクサーの瓶==========#
class ElixirBottle(Item):
    def __init__(self,name):
        super().__init__(name)
        self.isEmp = False
        self.timeCount = 0

    def consume(self):
        print("====================")
        if self.isEmp:
            input("しかし、中身は空だった……")
        else:
            input("エリクサーの瓶を使用した")
            if player.condition == "感染者":
                player.maxHp = 100
                player.hp = 100
                player.attack -= 20
                player.defense -= 10
                input("感染が治り、体力が全回復した")
            else:
                player.hp = player.maxHp
                input("体力が全回復した")
            self.isEmp = True
            self.timeCount = 0

    def use(self,player,chara):
        if chara.name == "キョンビ":
            if self.isEmp:
                return False
            chara.isStun = True
            self.isEmp = True
            self.timeCount = 0
            return True
        self.consume()
        return False

    def onMove(self,player):
        if self.isEmp:
            self.timeCount += 1
            if self.timeCount == 7:
                input("瓶が液体で満たされている！？")
                self.isEmp = False
                self.timeCount = 0

#==========マインドクローン==========#
class CloneBottle(Item):
    def __init__(self,name):
        super().__init__(name)

    def use(self,player,chara):
        print("====================")
        print("マインドクローンを取り出した")
        input("マインドクローンは相手を模倣する……")

        if chara.name == "ノイド":
            input("互いは見るだけで終わった")

        elif chara.name == "トスケ":
            input("ただのヘルメットになった……")

        elif chara.name == "ヨウカゲ":
            print("互いは戦闘を繰り広げている！")
            chara.hit(chara.attack)
            print("マインドクローンは元に戻った")

        elif chara.name == "ナイ":
            input("しかし、ナイの発明品によって阻止される……")

        elif chara.name == "ノリミケ":
            ans = random.randint(0,2)
            input("マインドクローンが魔物を生み出した！")
            if ans == 0:
                input("しかし、魔物は棒立ちだ……")
            elif ans == 1:
                input(f"魔物は{player.name}を攻撃した！")
                player.hit(10)
            else:
                input("魔物は大暴れだ！")
                chara.hit(20)
                if random.randint(1,10) == 7:
                    print("====================")
                    print("あなたも巻き込まれてしまった……")
                    player.hit(15)
            print("魔物ごとマインドクローンに戻った")

        elif chara.name == "ノウゼン":
            print("互いは拮抗している！")
            if chara.isSukura:
                input("……訳ではなかった")
            else:
                input("あなたはその間に逃げた")
                chara.die()
                player.item.remove(self)

        elif chara.name == "プロトタイプ":
            if chara.chargeCount > 2:
                print("マインドクローン「アルティメットキャノン法、発射！」")
                chara.hit(100)
            else:
                print("マインドクローン「エネルギー不足デス」")
                input("マインドクローンは元に戻った")

        elif chara.name == "キャッター":
            input("マインドクローンも丸くなった")

        elif chara.name == "化けダヌキ":
            input("タヌキになった……")

        else:
            input("マインドクローンは模倣できなかった……")

#==========味方キャラ==========#
class Helper:
    def __init__(self,name):
        self.name = name

    def act(self,player,chara):
        pass
#==========ノイド==========#
class HelperNoido(Helper):
    def __init__(self,name):
        super().__init__(name)

    def act(self,player,chara):
        print("====================")
        if chara.name == "ヨウカゲ":
            input("ノイド「腕輪があれば楽勝なんだけどな～」")
        elif chara.name == "ナイ":
            input("ノイド「ナイはいろんな道具や機械を作るんだ！」")
        elif chara.name == "ノリミケ":
            input("ノイド「ノリミケは良いヤツなんだけどな～」")
        elif chara.name == "ノウゼン":
            input("ノイド「スクラは大切にしろよ？」")
        elif chara.name == "プロトタイプ":
            input("ノイド「ぼくが狙われたら隠れるね～」")
        elif chara.name == "キャッター":
            input("ノイド「……あいつを甘く見ないほうが良いぞ」")
        elif chara.name == "マインドクローン":
            input("ノイド「マジでそっくりだな！」")
        elif chara.name == "化けダヌキ":
            input("ノイド「こいつは怖がりだからな」")
        else:
            input("ノイド「知らないヤツだ」")

#==========ノリミケ==========#
class HelperNorimike(Helper):
    def __init__(self,name):
        super().__init__(name)

    def act(self,player,chara):
        ans = random.randint(0,2)
        print("====================")
        input("ノリミケは魔物を生み出した")
        if ans == 0:
            input("しかし、魔物は棒立ちだ……")
        elif ans == 1:
            input(f"魔物は{chara.name}を攻撃した！")
            chara.hit(15)
        else:
            input("魔物は大暴れだ！")
            chara.hit(20)
            if random.randint(1,10) == 7:
                print("====================")
                print("あなたも巻き込まれてしまった……")
                player.hit(15)
        print("魔物はどこかへ立ち去った")

#==========ヒカリ==========#
class HelperHikari(Helper):
    def __init__(self,name):
        super().__init__(name)
        self.attack = 20
        self.exist = True

    def vanish(self,player):
        if self.exist:
            print("ヒカリ「それじゃ、またね」")
            player.helper.remove(self)
            self.exist = False
            input("ヒカリは消失した……")

    def act(self,player,chara):
        print("====================")
        print("ヒカリ「くらえ！ライジングストーム！」")
        if chara.name == "ヨウカゲ":
            if chara.condition == "通常":
                chara.hit(self.attack * 10)
            else:
                chara.hit(self.attack * 20)
        else:
            chara.hit(self.attack)
        self.vanish(player)

    def onMove(self,player):
        self.vanish(player)

#==========スクラ==========#
class HelperSukura(Helper):
    def __init__(self,name):
        super().__init__(name)

    def act(self,player,chara):
        print("====================")
        print("スクラ「ワンワン」")
        input("応援してくれているようだ")

#==========プロトタイプ==========#
class HelperPrototype(Helper):
    def __init__(self,name):
        super().__init__(name)
        self.chargeCount = 0

    def act(self,player,chara):
        print("====================")
        if self.chargeCount == 0:
            input("プロトタイプ「マズハボタンヲ押シテクダサイ」")
        elif self.chargeCount == 1:
            input("プロトタイプ「次ニレバーヲ引イテクダサイ」")
        else:
            print("プロトタイプ「チャージ完了！」")
            input("プロトタイプ「アルティメットキャノン法、発射！」")
            chara.hit(100)

    def onMove(self,player):
        if self.chargeCount != 0:
            self.chargeCount = 0
            input("プロトタイプ「チャージシステム停止シマス」")

#==========ふえるくん==========#
class HelperIncremal(Helper):
    def __init__(self,name):
        super().__init__(name)
        self.numCount = 1
        self.outCount = 100

    def push(self,player):
        player.die()
        input("あなたはふえるくんに押しつぶされてしまった……")

    def stretch(self,player):
        input("あなたはしっぽを引っ張った")
        if self.numCount == 1:
            print("突然、大量のふえるくんが出現した！")
            self.push(player)
        else:
            self.numCount = 1
            input("ふえるくんのコピーが消失した！")


    def act(self,player,chara):
        print("====================")
        self.stretch(player)

    def onMove(self,player):
        self.numCount += self.numCount
        self.numCount > self.numCount
        print("ふえるくんが増加した")
        if self.numCount > self.outCount / 2:
            input("嫌な予感がする……")
        elif self.numCount > self.outCount / 4:
            input("狭くなった気がする")
        if self.numCount > self.outCount:
            self.push(player)
            return
        print(f"現在の総数：{self.numCount}体")
        sel = input("しっぽを引っ張りますか？(y / n):")
        if sel.lower() == "y":
            self.stretch(player)

#==========プレイヤー==========#
class Player(Chara):
    def __init__(self,name):
        super().__init__(name,100,10,10,"通常")
        self.helper = []
        self.item = [Bandage("包帯")]
        self.isGuard = False

    def status(self):
        print(f"=== {self.name} ===")
        print(f"HP:{self.hp}/{self.maxHp}")
        print(f"AT:{self.attack}")
        print(f"DE:{self.defense}")
        print(f"状態：{self.condition}")
        if not self.item:
            print("アイテム：なし")
        else:
            itemName = [i.name for i in self.item]
            print(f"アイテム：{itemName}")
        if not self.helper:
            print("同行：なし")
        else:
            helperName = [i.name for i in self.helper]
            print(f"同行：{helperName}")
        input("（確認）")

    def start_turn(self):
        self.isGuard = False

    def select(self,maxNum,back = None):
        num = [str(i + 1) for i in range(maxNum)]
        if back:
            num.append(back)
        ans = input("選んでください:")
        while ans not in num:
            ans = input("もう一度選んでください:")
        return int(ans)

    def attack_AC(self,target):
        print("剣で攻撃！")
        target.hit(self.attack)
        return True

    def defense_AC(self,target):
        print("盾で防御！")
        self.isGuard = True
        return True

    def observe_AC(self,target):
        print("誰を観察？")
        print("====================")
        print(f"1:{self.name}")
        print(f"2:{target.name}")
        print("0:戻る")
        ans = self.select(2,"0")
        if ans == 0:
            pass
        elif ans == 1:
            self.status()
        else:
            target.info()
        return False

    def item_AC(self,target):
        print("=====アイテム一覧=====")
        for i in range(len(self.item)):
            print(f"{i + 1}:{self.item[i].name}")
        print("0:戻る")
        sel = self.select(len(self.item),"0")
        if sel == 0:
            return False
        idx =  sel - 1
        self.item[idx].use(self,target)
        return True

    def helper_AC(self,target):
        print("=====キャラクター一覧=====")
        for i in range(len(self.helper)):
            print(f"{i + 1}:{self.helper[i].name}")
        print("0:戻る")
        sel = self.select(len(self.helper),"0")
        if sel == 0:
            return False
        self.helper[sel - 1].act(self,target)
        return True

    def action(self,target):
        command = ["攻撃","防御","観察"]
        ac = [self.attack_AC,self.defense_AC,self.observe_AC]
        if self.item:
            command.append("道具")
            ac.append(self.item_AC)
        if self.helper:
            command.append("味方")
            ac.append(self.helper_AC)
        while True:
            print("====================")
            for i in range(len(command)):
                print(f"{i + 1}:{command[i]}")
            print("====================")
            ans = self.select(len(command))
            isTurnEnd = ac[ans - 1](target)
            if isTurnEnd:
                break

    def hit(self,damage):
        if self.isGuard:
            damage = int(damage / 4)
            self.isGuard = False

        self.hitDamage(damage)

        if self.hp <= 0:
            self.die()
            input("あなたは倒されてしまった……")

    def moveRoom(self):
        if not self.isAlive:
            return
        print("====================")
        input("あなたは部屋を出た")
        if player.hp != player.maxHp:
            for i in self.item:
                if i.name == "包帯":
                    print(f"現在HP:{player.hp}/{player.maxHp}")
                    if input("包帯を使用しますか？(y / n):").lower() == "y":
                        i.use(self, None)
                    break
        for i in self.item[:]:
            if hasattr(i,"onMove"):
                i.onMove(self)

        for i in self.helper[:]:
            if hasattr(i,"onMove"):
                i.onMove(self)

#==========ノイド==========#
class Noido(Chara):
    def __init__(self):
        super().__init__("ノイド",10,1,1,"通常")
        self.selectCommu = ["仲良くする","無視する","戦う"]
        self.actList = ["再生","観察","攻撃"]
        print("====================")
        input("ノイド「ぼくはノイド、君の名前は？」")

    def info(self):
        print(f"=== {self.name} ===")
        print(f"HP:{self.hp}/{self.maxHp}")
        print(f"AT:{self.attack}")
        print(f"DE:{self.defense}")
        print(f"状態：{self.condition}")
        print("関係：警戒")
        print("行動傾向：こちらの様子をうかがっている")
        print("危険度：低")
        print("備考：この建物の住人")
        input("（確認）")

    def community(self,player):
        print("====================")
        print("どうする？")
        print("====================")
        for i in range(len(self.selectCommu)):
            print(f"{i + 1}:{self.selectCommu[i]}")
        print("====================")
        ans = player.select(len(self.selectCommu))
        if ans == 1:
            input(f"ノイド「へえ～、{player.name}っていうんだ～、よろしくね！」")
            print("====================")
            player.helper.append(HelperNoido("ノイド"))
            input("ノイドが仲間になった！")
        elif ans == 2:
            input("ノイド「？へんなやつ……」")
        else:
            input("ノイド「えぇ！？なんでー！？」")
            return True
        return False

    def action(self,player):
        act = random.choice(self.actList)
        if act == "再生":
            if self.hp < self.maxHp:
                print("ノイド「再生だー！」")
                self.hp = self.maxHp
            else:
                print("ノイド「……？」")
        elif act == "観察":
            print("ノイド「何なんだコイツ……」")
        else:
            print("ノイド「オラ！」")
            player.hit(self.attack)

    def hit(self,damage):
        self.hitDamage(damage)
        if self.hp <= 0:
            self.die()
            print("====================")
            print("ノイド「ぐわー」")
            input(f"{self.name}を倒した！")

#==========トスケ==========#
class Tosuke(Chara):
    def __init__(self):
        super().__init__("人格ヘルメット",10,1,1,"通常")
        self.selectCommu = ["拾う","蹴とばす","被ってみる"]
        self.act = ["自爆"]
        print("====================")
        input("人格ヘルメットを発見した！")

    def info(self):
        print(f"=== {self.name} ===")
        print(f"HP:{self.hp}/{self.maxHp}")
        print(f"AT:{self.attack}")
        print(f"DE:{self.defense}")
        print(f"状態：{self.condition}")
        print("関係：不明")
        print("行動傾向：楽しそうにはしゃいでいる")
        print("危険度：低")
        print("備考：ノイドの人格を乗っ取った")
        input("（確認）")

    def community(self,player):
        if any(n.name == "ノイド" for n in player.helper):
            print("====================")
            input("ノイド「あっ！これ探してたんだよね～」")
            print("ノイドはヘルメットを被った")
            input("？？？「……」")
            player.helper = [h for h in player.helper if h.name != "ノイド"]
            self.name = "トスケ"
            input("トスケ「いえ～い、ぼくだよ～」")
            return True
        else:
            print("====================")
            print("どうする？")
            print("====================")
            for i in range(len(self.selectCommu)):
                print(f"{i + 1}:{self.selectCommu[i]}")
            print("====================")
            ans = player.select(len(self.selectCommu))
            if ans == 1:
                player.item.append(Helmet("人格ヘルメット"))
                input("人格ヘルメットをゲットした！")
            elif ans == 2:
                print("ヘルメットを蹴とばした")
                input("部屋の隅へと転がって行った")
            else:
                Helmet("人格ヘルメット").use(player,None)
            return False

    def action(self,player):
        print("トスケ「これでもくらえ！プロペラボム！」")
        player.hit(100)
        print("====================")
        print("トスケも巻き込まれた")
        self.hit(100)

    def hit(self,damage):
        self.hitDamage(damage)
        if self.hp <= 0:
            self.die()
            print("====================")
            print("トスケ「ンギャピッ！」")
            input(f"{self.name}を倒した！")

#==========ヨウカゲ==========#
class Youkage(Chara):
    def __init__(self):
        super().__init__("邪悪箱",100,50,50,"通常")
        self.selectCommu = ["拾う","放っておく","ぶっ壊す"]
        self.actList = ["強化","防御","攻撃","必殺"]
        self.isGuard = False
        self.isPowerUp = False
        print("====================")
        input("邪悪箱を発見した！")

    def info(self):
        print(f"=== {self.name} ===")
        print(f"HP:{self.hp}/{self.maxHp}")
        print(f"AT:{self.attack}")
        print(f"DE:{self.defense}")
        print(f"状態：{self.condition}")
        print("関係：敵対")
        print("行動傾向：こちらに敵意を向けている……")
        print("危険度：高")
        print("備考：邪悪箱から出てきた存在")
        input("（確認）")

    def community(self,player):
        print("====================")
        print("どうする？")
        print("====================")
        for i in range(len(self.selectCommu)):
            print(f"{i + 1}:{self.selectCommu[i]}")
        print("====================")
        ans = player.select(len(self.selectCommu))
        if ans == 1:
            print("中から邪悪な存在が飛び出してきた！")
            input("あなたは逃げた際に、攻撃を受けてしまった……")
            player.hit(self.attack)
        elif ans == 2:
            input("特に何も起きなかった")
        else:
            input("中から謎の存在が飛び出してきた！")
            self.name = "ヨウカゲ"
            input("？？？「この箱を壊そうとしたのは……お前か？」")
            return True
        return False

    def action(self,player):
        self.isGuard = False
        self.condition = "通常"
        if self.isPowerUp:
            print("====================")
            input("ヨウカゲ「消え失せろ……」")
            player.hit(self.attack * 2)
            self.isPowerUp = False
            return
        act = random.choice(self.actList)
        if act == "攻撃":
            print("ヨウカゲの攻撃が繰り出す！")
            player.hit(self.attack)
        elif act == "防御":
            self.isGuard = True
            self.condition = "防御中"
            print("ヨウカゲはマフラーで身を包む")
        else:
            self.isPowerUp = True
            self.condition = "強化形態"
            print("====================")
            input("ヨウカゲの腕が変形した！？")

    def hit(self,damage):
        if self.isGuard:
            damage /= 2
        elif self.isPowerUp:
            damage *= 1.5
        self.hitDamage(damage)
        if self.hp <= 0:
            self.die()
            print("====================")
            print("ヨウカゲ「……クソッ」")
            input(f"{self.name}を倒した！")

#==========ヒカリ==========#
class Hikari(Chara):
    def __init__(self):
        super().__init__("ヒカリの腕輪",10,10,10,"通常")
        self.selectCommu = ["拾う","放っておく","ぶっ壊す"]
        print("====================")
        input("ヒカリの腕輪を発見した！")

    def community(self,player):
        print("====================")
        print("どうする？")
        print("====================")
        for i in range(len(self.selectCommu)):
            print(f"{i + 1}:{self.selectCommu[i]}")
        print("====================")
        ans = player.select(len(self.selectCommu))
        if ans == 1:
            player.item.append(Bracelet("ヒカリの腕輪"))
            input(f"ヒカリの腕輪をゲットした！")
        elif ans == 2:
            input("特に何も起きなかった")
        else:
            print("腕輪に電気が帯びた！")
            input("あなたは感電してしまった……")
            player.hit(self.attack)
        return False

#==========ナイ==========#
class Nai(Chara):
    def __init__(self):
        super().__init__("ナイ",30,10,5,"通常")
        self.selectCommu = ["発明品をもらう","無視する","実験体になる"]
        self.actList = ["回復","観察","飛行","攻撃","必殺"]
        self.items = [Gun("ビームガン"),HeelBox("ヒールボックス"),Goggle("サーチゴーグル")]
        self.isJet = False
        self.isBoat = False
        print("====================")
        input("ナイ「よく聞け！僕は超天才発明家ナイだ！」")

    def info(self):
        print(f"=== {self.name} ===")
        print(f"HP:{self.hp}/{self.maxHp}")
        print(f"AT:{self.attack}")
        print(f"DE:{self.defense}")
        print(f"状態：{self.condition}")
        print("関係：中立")
        print("行動傾向：機械をいじっている")
        print("危険度：中")
        print("備考：自称天才発明家")
        input("（確認）")

    def community(self,player):
        print("====================")
        print("どうする？")
        print("====================")
        for i in range(len(self.selectCommu)):
            print(f"{i + 1}:{self.selectCommu[i]}")
        print("====================")
        ans = player.select(len(self.selectCommu))
        if ans == 1:
            input(f"ナイ「有効活用してくれよ？」")
            item = random.choice(self.items)
            player.item.append(item)
            print("====================")
            input(f"{item.name}をゲットした！")
        elif ans == 2:
            input("ナイ「無視するなー！」")
            return True
        else:
            input("ナイ「ちょうど、実験体が欲しかったんだ」")
            print("====================")
            input("---実験中---")
            print("====================")
            if player.condition == "通常" and random.randint(0,1) == 1:
                player.maxHp += 50
                player.hp = player.maxHp
                player.attack += 10
                player.defense += 10
                player.condition = "サイボーグ"
                input("ナイ「よし！成功した！」")
                print("====================")
                input(f"{player.name}のステータスが上昇した！")
            else:
                input("ナイ「し……しっぱいした……」")
                player.hp = 0
                player.die()
        return False

    def action(self,player):
        if self.isBoat:
            print("====================")
            print("ナイはエアボートで突撃した！")
            player.hit(self.attack * 2)
            print("====================")
            print("ナイはその反動を受けた")
            self.hit(self.attack)
            self.isBoat = False
            self.condition = "通常"
            return
        elif self.isJet:
            input("ナイは上空から様子をうかがっている")
            return
        act = random.choice(self.actList)
        if act == "回復":
            if self.hp > self.maxHp / 2:
                print("ナイは様子を見ている")
            else:
                self.hp = min(self.maxHp,self.hp + 5)
                print("ナイはヒールボックスで回復した")
                print("ナイのHPが5回復した")
        elif act == "攻撃":
            print("ナイはビームガンを使った！")
            player.hit(self.attack)
        elif act == "飛行":
            self.isJet = True
            self.condition = "ジェット"
            print("ナイはジェットパックで飛んだ")
        else:
            self.isBoat = True
            self.condition = "エアボート"
            print("====================")
            input("ナイはエアボートに乗り込んだ")

    def hit(self,damage):
        if self.isJet:
            input("しかし、避けられた……")
            self.isJet = False
            self.condition = "通常"
            return
        self.hitDamage(damage)
        if self.hp <= 0:
            self.die()
            print("====================")
            print("ナイ「なかなかやるじゃないか……」")
            input(f"{self.name}を倒した！")

#==========ノリミケ==========#
class Norimike(Chara):
    def __init__(self):
        super().__init__("ノリミケ",5,1,1,"通常")
        self.selectCommu = ["仲良くする","無視する","戦う"]
        self.actList = ["棒立ち","攻撃","暴走"]
        self.deathCount = 0
        self.maxRevive = 2
        self.isSeoul = False
        print("====================")
        input("ノリミケ「オレ、ノリミケ！よろしくな！」")

    def info(self):
        print(f"=== {self.name} ===")
        if self.isSeoul:
            print(f"HP:??/??")
            print(f"AT:??")
            print(f"DE:??")
            print(f"状態：不明")
            print("関係：不明")
            print("行動傾向：宙に漂っている")
            print("危険度：中")
            print(f"備考：復活回数:{self.maxRevive - self.deathCount}")
        else:
            print(f"HP:{self.hp}/{self.maxHp}")
            print(f"AT:{self.attack}")
            print(f"DE:{self.defense}")
            print(f"状態：{self.condition}")
            print("関係：友好的")
            print("行動傾向：魔物を生み出そうとしている")
            print("危険度：中")
            print("備考：魔物を生み出す存在")
        input("（確認）")

    def community(self,player):
        print("====================")
        print("どうする？")
        print("====================")
        for i in range(len(self.selectCommu)):
            print(f"{i + 1}:{self.selectCommu[i]}")
        print("====================")
        ans = player.select(len(self.selectCommu))
        if ans == 1:
            input(f"ノリミケ「よろしくな！{player.name}！」")
            print("====================")
            player.helper.append(HelperNorimike("ノリミケ"))
            input("ノリミケが仲間になった！")
        elif ans == 2:
            print("ノリミケが魔物を生み出した！")
            input("あなたは逃げた際に、攻撃を受けてしまった……")
            player.hit(20)
        else:
            input("ノリミケ「ほへぃ？」")
            return True
        return False

    def action(self,player):
        if self.isSeoul:
            self.hp = self.maxHp
            self.name = "ノリミケ"
            self.isSeoul = False
            print("青い魂からノリミケが飛び出してきた！")
            input("ノリミケ「生き返った～」")
            return
        act = random.choice(self.actList)
        print("ノリミケは魔物を生み出した！")
        if act == "棒立ち":
            print("しかし、魔物は棒立ちだ")
        elif act == "攻撃":
            print("魔物はこちらに攻撃してきた！")
            player.hit(10)
        else:
            print("魔物は暴れまわった！")
            player.hit(20)
            print("====================")
            print("ノリミケも巻き込まれた")
            self.hit(20)
        print("あなたは魔物を倒した")

    def hit(self,damage):
        if self.isSeoul:
            input("しかし、攻撃が当たらない……")
            return
        self.hitDamage(damage)
        if self.hp <= 0:
            self.isSeoul = True
            print("====================")
            print("ノリミケ「えぇ～」")
            input(f"{self.name}を倒した！")
            self.name = "青い魂"
            input("しかし、青い魂が現れた！")
            if self.deathCount == self.maxRevive:
                input("青い魂はどこかへと消えていった……")
                self.die()
            else:
                self.deathCount += 1

#==========ノウゼン==========#
class Nouzen(Chara):
    def __init__(self):
        super().__init__("ノウゼン",10,1,1,"通常")
        self.selectCommu = ["崇める","無視する","戦う"]
        self.actList = ["改変"]
        self.isSukura = False
        print("====================")
        input("ノウゼン「おい！崇めろ！」")

    def info(self):
        print(f"=== {self.name} ===")
        print(f"HP:{self.hp}/{self.maxHp}")
        print(f"AT:{self.attack}")
        print(f"DE:{self.defense}")
        print(f"状態：{self.condition}")
        print("関係：断罪")
        print("行動傾向：仁王立ちでこちらを見ている")
        print("危険度：高")
        print("備考：自称全能の神")
        input("（確認）")

    def sukuraAction(self):
        input("……")
        input("ノウゼン「我の力が通用しない！？」")

    def community(self,player):
        self.isSukura = any(isinstance(s,HelperSukura) for s in player.helper)
        print("====================")
        print("どうする？")
        print("====================")
        for i in range(len(self.selectCommu)):
            print(f"{i + 1}:{self.selectCommu[i]}")
        print("====================")
        ans = player.select(len(self.selectCommu))
        if ans == 1:
            print("ノウゼン「我の恵みを受けよ……ハッ！」")
            if self.isSukura:
                self.sukuraAction()
                input("特に何も起きなっかった")
                return
            player.defense += 10
            input("あなたの防御力が上昇した！")
        elif ans == 2:
            print("ノウゼン「我を崇めぬものはいらぬ！ハッ！」")
            if self.isSukura:
                self.sukuraAction()
                print("特に何も起きなかった")
                return
            player.die()
            input("あなたは歯車になった……")
        else:
            input("ほう……我と対峙するか")
            return True
        return False

    def action(self,player):
        print("我の力を見よ！ハッ！")
        if self.isSukura:
            self.sukuraAction()
            return
        player.die()
        input("あなたは歯車になった……")

    def hit(self,damage):
        if self.isSukura:
            self.hitDamage(damage)
            if self.hp <= 0:
                self.die()
                print("====================")
                print("ノウゼン「ば……ばかな……われがまけるとは……」")
                input(f"{self.name}を倒した！")
        else:
            input("ノウゼン「効かぬわ！」")

#==========スクラ==========#
class Sukura(Chara):
    def __init__(self):
        super().__init__("スクラ",5,1,1,"通常")
        self.selectCommu = ["仲良くする","待機する","戦う"]
        print("====================")
        input("スクラ「ワンワン！」")

    def community(self,player):
        print("====================")
        print("どうする？")
        print("====================")
        for i in range(len(self.selectCommu)):
            print(f"{i + 1}:{self.selectCommu[i]}")
        print("====================")
        ans = player.select(len(self.selectCommu))
        if ans == 1:
            print("スクラ「ワンワン！」")
            player.helper.append(HelperSukura("スクラ"))
            input(f"スクラが仲間になった！")
        elif ans == 2:
            if player.hp == player.maxHp:
                input("特に何も起きなかった")
            else:
                print("スクラが包帯を持ってきてくれた")
                player.item.append(Bandage("包帯"))
                input("包帯をゲットした！")
        else:
            print("スクラ「ワンワン！」")
            input("しかし、逃げられてしまった……")
        return False

#==========キョンビ==========#
class Kyombie(Chara):
    def __init__(self):
        super().__init__("キョンビ",10,1,1,"通常")
        self.selectCommu = ["くしゃみさせる","待機する","無視する"]
        self.isStun = False
        print("====================")
        input("キョンビ「いえ～い、私は改造生物キョンビだぞ～」")

    def zombie(self,player):
        player.name = "ゾンビ"
        player.die()
        input(f"あなたは感染し、ゾンビになってしまった……")

    def community(self,player):
        print("====================")
        print("どうする？")
        print("====================")
        for i in range(len(self.selectCommu)):
            print(f"{i + 1}:{self.selectCommu[i]}")
        print("====================")
        ans = player.select(len(self.selectCommu))
        if ans == 1:
            print("キョンビ「べっくしょん！」")
            input("ゾンビウイルスが飛び出してきた")
            if player.condition == "サイボーグ":
                input("しかし、あなたはサイボーグのため襲われなかった")
            elif any(isinstance(e,ElixirBottle) for e in player.item):
                elixir = next(i for i in player.item if i.name == "エリクサーの瓶")
                if elixir.use(player,self):
                    input("あなたはエリクサーの瓶を使用した")
                    input("ゾンビは気絶し、難を逃れた")
                else:
                    self.zombie(player)
            else:
                self.zombie(player)
        elif ans == 2:
            if player.condition == "通常":
                print("キョンビ「べっくしょん！」")
                input("タグウイルスが飛び出してきた")
                player.condition = "感染者"
                player.maxHp = 80
                player.hp = min(player.hp,player.maxHp)
                player.attack += 20
                player.defense += 10
                input("あなたは感染し、ステータスが変更した！")
            else:
                input("特に何も起きなかった")
        else:
            input("キョンビ「ばいば～い」")
        return False

#==========エリクサーの瓶==========#
class Elixir(Chara):
    def __init__(self):
        super().__init__("エリクサーの瓶",1,1,1,"通常")
        self.selectCommu = ["拾う","放っておく","飲む"]
        print("====================")
        input("エリクサーの瓶を発見した！")

    def community(self,player):
        print("====================")
        print("どうする？")
        print("====================")
        for i in range(len(self.selectCommu)):
            print(f"{i + 1}:{self.selectCommu[i]}")
        print("====================")
        ans = player.select(len(self.selectCommu))
        if ans == 1:
            player.item.append(ElixirBottle("エリクサーの瓶"))
            input(f"エリクサーの瓶をゲットした！")
        elif ans == 2:
            input("特に何も起きなかった")
        else:
            print("あなたは瓶の中身を飲んだ")
            ElixirBottle("エリクサーの瓶").use(player,None)
        return False


#==========プロトタイプ==========#
class Prototype(Chara):
    def __init__(self):
        super().__init__("プロトタイプ",10,100,100,"暴走")
        self.selectCommu = ["仲良くする","ボタンを押す","戦う"]
        self.actList = ["溜める","必殺"]
        self.chargeCount = 0
        print("====================")
        input("プロトタイプ「私ハ、プロトタイプデス」")

    def info(self):
        print(f"=== {self.name} ===")
        print(f"HP:{self.hp}/{self.maxHp}")
        print(f"AT:{self.attack}")
        print(f"DE:{self.defense}")
        print(f"状態：{self.condition}")
        print("関係：敵対")
        print("行動傾向：何かのシステムを作動させている")
        print("危険度：低")
        print("備考：暴走ボタンを押してしまった……")
        input("（確認）")

    def community(self,player):
        print("====================")
        print("どうする？")
        print("====================")
        for i in range(len(self.selectCommu)):
            print(f"{i + 1}:{self.selectCommu[i]}")
        print("====================")
        ans = player.select(len(self.selectCommu))
        if ans == 1:
            input(f"プロトタイプ「コレカラ、ヨロシクデス！」")
            print("====================")
            player.helper.append(HelperPrototype("プロトタイプ"))
            input("プロトタイプが仲間になった！")
        elif ans == 2:
            input("プロトタイプ「暴走モード起動！」")
            return True
        else:
            print("プロトタイプ「ヒェー！オタスケー！」")
            input("しかし、逃げられてしまった……")
        return False

    def action(self,player):
        self.chargeCount += 1
        if self.chargeCount == 1:
            print("プロトタイプ「システム再機動」")
        elif self.chargeCount == 2:
            print("プロトタイプ「エネルギー充填中」")
        elif self.chargeCount == 3:
            print("プロトタイプ「チャージ完了」")
        elif self.chargeCount == 4:
            print("プロトタイプ「ターゲットロックオン」")
        else:
            input("プロトタイプ「アルティメットキャノン法、発射！」")
            player.hit(self.attack)
            self.chargeCount = 0

    def hit(self,damage):
        self.hitDamage(damage)
        if self.hp <= 0:
            self.die()
            print("====================")
            print("プロトタイプ「システムダウン……」")
            input(f"{self.name}を倒した！")

#==========キャッター==========#
class Catter(Chara):
    def __init__(self):
        super().__init__("キャッター",10,1,1,"通常")
        self.selectCommu = ["攻撃する","無視する","戦う"]
        self.actList = ["休止","反撃"]
        self.isAttack = False
        print("====================")
        input("キャッターが部屋の真ん中で丸まっている！")

    def info(self):
        print(f"=== {self.name} ===")
        print(f"HP:{self.hp}/{self.maxHp}")
        print(f"AT:{self.attack}")
        print(f"DE:{self.defense}")
        print(f"状態：{self.condition}")
        if self.isAttack:
            print("関係：敵対")
            print("行動傾向：こちらを見ている……")
            print("危険度：高")
            print("備考：矢印のような毛がこちらを指している……")
        else:
            print("関係：中立")
            print("行動傾向：丸まっている")
            print("危険度：低")
            print("備考：矢印のような毛がある")
        input("（確認）")

    def anger(self):
        input("あなたはキャッターの逆鱗に触れた……")
        self.maxHp *= 100
        self.hp = self.maxHp
        self.attack = 500
        self.defense = 500
        self.condition = "憤怒"
        self.isAttack = True

    def community(self,player):
        print("====================")
        print("どうする？")
        print("====================")
        for i in range(len(self.selectCommu)):
            print(f"{i + 1}:{self.selectCommu[i]}")
        print("====================")
        ans = player.select(len(self.selectCommu))
        if ans == 1:
            self.anger()
            player.hit(self.attack)
        elif ans == 2:
            input("キャッターは丸まったままだ")
        else:
            input("あなたは戦いを挑んだ！")
            return True
        return False

    def action(self,player):
        if self.isAttack:
            input("キャッターの反撃！")
            player.hit(self.attack)
        else:
            input("キャッターは丸まっている")

    def hit(self,damage):
        print("しかし、キャッターは無傷だ……")
        if not self.isAttack:
            self.anger()

#==========ふえるくん==========#
class Incremal(Chara):
    def __init__(self):
        super().__init__("ふえるくん",1,1,1,"通常")
        self.selectCommu = ["しっぽを引っ張る","連れていく","無視する"]
        print("====================")
        input("ふえるくん「チュー」")

    def community(self,player):
        print("====================")
        print("どうする？")
        print("====================")
        for i in range(len(self.selectCommu)):
            print(f"{i + 1}:{self.selectCommu[i]}")
        print("====================")
        ans = player.select(len(self.selectCommu))
        if ans == 1:
            input(f"突然、大量にふえるくんが生成された！")
            player.die()
            input("あなたは大量のふえるくんに押しつぶされてしまった……")
        elif ans == 2:
            input("ふえるくん「チュー？」")
            print("====================")
            player.helper.append(HelperIncremal("ふえるくん"))
            input("ふえるくんが仲間になった！")
        else:
            input("特に何も起きなかった")
        return False

#==========マインドクローン==========#
class MindClone(Chara):
    def __init__(self):
        super().__init__("マインドクローン",10,1,1,"模倣")
        self.selectCommu = ["ボトルに入れる","無視する","戦う"]
        self.actList = ["攻撃","防御","観察"]
        self.isGuard = False
        print("====================")
        input("マインドクローン「私はマインドクローン」")

    def info(self):
        print(f"=== {self.name} ===")
        print(f"HP:{self.hp}/{self.maxHp}")
        print(f"AT:{self.attack}")
        print(f"DE:{self.defense}")
        print(f"状態：{self.condition}")
        print("関係：模倣")
        print("行動傾向：こちらの様子をうかがっている")
        print("危険度：不明")
        print("備考：あなたを模倣しているようだ")
        input("（確認）")

    def community(self,player):
        print("====================")
        print("どうする？")
        print("====================")
        for i in range(len(self.selectCommu)):
            print(f"{i + 1}:{self.selectCommu[i]}")
        print("====================")
        ans = player.select(len(self.selectCommu))
        if ans == 1:
            input(f"マインドクローン「何かあったら呼べよ～」")
            print("====================")
            player.item.append(CloneBottle("クローンボトル"))
            input("クローンボトルをゲットした！")
        elif ans == 2:
            input("マインドクローン「……？」")
        else:
            self.maxHp = max(1,player.maxHp // 5)
            self.hp = max(1,player.hp // 5)
            self.attack = player.attack
            self.defense = player.defense
            input("マインドクローンはあなたを模倣した！？")
            return True
        return False

    def action(self,player):
        self.isGuard = False
        act = random.choice(self.actList)
        if act == "攻撃":
            print("マインドクローンの攻撃！")
            player.hit(self.attack)
        elif act == "防御":
            self.isGuard = True
            print("マインドクローンは盾を構えている！")
        else:
            print("マインドクローンはこちらを見ている")

    def hit(self,damage):
        if self.isGuard:
            damage /= 4
        self.hitDamage(damage)
        if self.hp <= 0:
            self.die()
            print("====================")
            print("マインドクローンは溶けた")
            input(f"{self.name}を倒した！")

#==========タヌキ==========#
class Tanuki(Chara):
    def __init__(self):
        super().__init__("タヌキ",5,1,1,"通常")
        self.selectCommu = ["驚かす","無視する","戦う"]
        self.actList = ["溜める","必殺","気絶"]
        self.attackTurn = 0
        print("====================")
        input("タヌキがこちらを警戒している")

    def info(self):
        print(f"=== {self.name} ===")
        print(f"HP:{self.hp}/{self.maxHp}")
        print(f"AT:{self.attack}")
        print(f"DE:{self.defense}")
        print(f"状態：{self.condition}")
        print("関係：敵対")
        print("行動傾向：こちらの様子をうかがっている")
        print("危険度：中")
        print("備考：驚かすと変化する")
        input("（確認）")

    def community(self,player):
        print("====================")
        print("どうする？")
        print("====================")
        for i in range(len(self.selectCommu)):
            print(f"{i + 1}:{self.selectCommu[i]}")
        print("====================")
        ans = player.select(len(self.selectCommu))
        if ans == 1:
            input("驚いて化けダヌキに変化した！")
            self.name = "化けダヌキ"
            self.maxHp = 20
            self.hp = self.maxHp
            self.attack = 10
            self.defense = 5
            return True
        elif ans == 2:
            input("特に何もなかった")
        else:
            input("タヌキは矢に変化して、こちらに飛んできた！")
            player.hit(10)
        return False

    def action(self,player):
        if self.attackTurn == 0:
            input("化けダヌキは力を溜めている……！")
        elif self.attackTurn == 1:
            input("化けダヌキの突進！")
            player.hit(self.attack * 2)
        else:
            print("化けダヌキは気絶している")
            self.attackTurn = 0
            return
        self.attackTurn += 1

    def hit(self,damage):
        self.hitDamage(damage)
        if self.hp <= 0:
            self.name = "タヌキ"
            self.die()
            print("====================")
            print("タヌキ「プクー」")
            input(f"{self.name}を倒した！")

#==========部屋管理==========#
class Room:
    def __init__(self, roomID, content):
        self.roomID = roomID
        self.content = content
        self.charaName = "???"
        self.isCheck = False
        self.flag = {}

#==========オープニング==========#
def opening(player_name):
    print("")
    input(f"{player_name}は数々の依頼をこなしていた")
    input("時には人を助け")
    input("時には害獣を倒した")
    print("")
    input("そして今日も、とある依頼が舞い込んできた")
    input("『突然現れた建物を調査してほしい』")
    print("")
    input(f"{player_name}はその建物の前に立ち")
    input("建物の看板を見上げる")
    print("")
print("オープニングを見ますか？")
ans = input("(y or n):")
print("依頼主「そういや、あんた名前は？」")
name = input("名前を入力してください:")
if not name:
    name = "トモユキ"
if ans.lower() == "y":
    opening(name)
    print("====================")
    print("|                  |")
    print("|--イグネス開発所--|")
    print("|                  |")
    print("====================")
    input("")
player = Player(name)

#==========メイン==========#
allRoom = [
    
    [Room("IN-963", Tosuke),Room("IN-301", Sukura),Room("IN-500", Elixir)],
    [Room("IN-000", Noido),Room("IN-073", Hikari),Room("IN-111",Tanuki)],
    [Room("IN-914", Nai),Room("IN-109",MindClone),Room("IN-102", Kyombie)],
    [Room("IN-104", Norimike),Room("IN-001",Prototype),Room("IN-076", Youkage)],
    [Room("IN-239", Nouzen),Room("IN-871",Incremal),Room("IN-096",Catter)]

    ]

def battle(player,chara):
    print("====================")
    input(f"{chara.name}が現れた！")
    battler = [player,chara]
    turn = 0
    while player.isAlive and chara.isAlive:
        print("====================")
        input(f"{battler[turn].name}のターン")
        if hasattr(battler[turn],"start_turn"):
            battler[turn].start_turn()
        battler[turn].action(battler[1 - turn])
        turn = 1 - turn
    #アイテムドロップ
    if not chara.isAlive:
        if isinstance(chara, Youkage):
            player.item.append(EvilBox("邪悪箱"))
            print("====================")
            input("邪悪箱をゲットした！")

def shotStatus(player):
    print(f"====={player.name}=====")
    print(f"HP{player.hp}/{player.maxHp}")
    if player.item:
        itemName = [i.name for i in player.item]
        print(f"道具:{itemName}")
    if player.helper:
        helperName = [i.name for i in player.helper]
        print(f"同行:{helperName}")

def showRoom(floor):
    print("====================")
    print("どこを調査しますか？")
    print("====================")
    for i, room in enumerate(floor):
        if room.isCheck:
            print(f"{i + 1}:{room.charaName}の部屋")
        else:
            print(f"{i + 1}:{room.roomID}号室")
    print("0:奥に進む")
    print("====================")

def roomSelect(player, floor):
    sel = player.select(len(floor), "0")
    return sel

def warpKey(player,allRoom):
    print("====================")
    input("転移の鍵を拾った！")
    print("====================")
    print("どこにいく？")
    for i, alea in enumerate(allRoom):
        roomName = [room.charaName for room in alea]
        print(f"{i + 1}:{', '.join(roomName)}の場所")
    print("0:出口")
    selectNum = player.select(len(allRoom),"0")
    return selectNum

def roomCheck(player, room):
    if room.isCheck:
        print("====================")
        input("調査済みです")
        return True

    room.isCheck = True
    chara = room.content()
    room.charaName = chara.name

    if chara.community(player):
        battle(player, chara)
    return False

alea = 0
roomNum = 0

while player.isAlive:
    showRoom(allRoom[alea])
    sel = roomSelect(player, allRoom[alea])

    if sel == 0:
        alea += 1
        if alea == len(allRoom):
            keyNum = warpKey(player,allRoom)
            if keyNum == 0:
                break
            else:
                alea = keyNum - 1
                print("====================")
                input("気が付くと、鍵が消えていた……")
        continue

    room = allRoom[alea][sel - 1]
    if roomCheck(player, room):
        continue

    player.moveRoom()

    print("====================")
    shotStatus(player)

    if player.isAlive:
        if input("（ENTERで進む／nで脱出）").lower() == "n":
            break


print("====================")
if player.isAlive:
    print("あなたはこの建物から脱出した！")
else:
    print("あなたがこの建物から出ることはなかった……")
print("====================")
