numList = []
for x in range(1,10):
    for y in range(1,10):
        numList.append(x * y)
    print(*numList,sep = "\t")
    numList.clear()
