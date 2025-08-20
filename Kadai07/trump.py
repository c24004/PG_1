import random
allNum = [i + 1 for i in range(52)]
random.shuffle(allNum)
mark = ["スペード","クローバー","ダイヤ","ハート"]
num = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
print("あなたが引いたトランプは,")
for i in range(5):
    select = random.choice(allNum) - 1
    selectNum = num[select % 13]
    selectMark = mark[select // 13]
    print(f"{selectMark}の{selectNum}")
    allNum.remove(select + 1)
