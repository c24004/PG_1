import sys
"""
selectAll = []

for x in range(5):
    for y in range(5):
        selectAll.append([y + 1,x + 1])
"""
def selectNum():
    x = input("ヨコ:")
    while x not in ["0","1","2","3","4","5"]:
        x = input("再度入力してください:")
    if x == "0":
        sys.exit()
    y = input("タテ:")
    while y not in ["0","1","2","3","4","5"]:
        y = input("再度入力してください:")
    if y == "0":
        sys.exit()
    return int(x),int(y)

icon = ["○","×"]

line = [[icon[0] for i in range(7)] for i in range(7)]

clearLine = [[icon[1] for i in range(len(line) - 2)] for i in range(len(line) - 2)]


for i in range(len(line)):
    if i != 0 and i != 6:
        l = line[i]
        print(*l[1:6],sep = " ")



while True:
    x,y = selectNum()

    for lineX in range(-1,2):
        for lineY in range(-1,2):
            if lineX == 0 or lineY == 0:
                line[y + lineY][x + lineX] = icon[1 - icon.index(line[y + lineY][x + lineX])]

    for i in range(len(line)):
        if i != 0 and i != 6:
            l = line[i]
            print(*l[1:6],sep = " ")
    
    l = [line[i][1:6] for i in range(1,6)]

    if clearLine == l:
        print("クリア")
        break
