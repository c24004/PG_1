import random
allNum = [[i for i in range(0)] for i in range(6)]
for i in range(100):
    num = random.randint(1,6)
    allNum[num - 1].append("*")
for i in range(len(allNum)):
    print(i + 1,end = "")
    print(*allNum[i],sep = "")
