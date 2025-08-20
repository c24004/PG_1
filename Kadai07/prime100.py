numList = [] * 10
for i in range(1,101):
    for n in range(2,i):
        if i == n:
            continue
        else:
            if i % n == 0:
                break
    else:
        if i == 1:
            continue
        numList.append(i)
        if len(numList) == 10:
            print(*numList,sep = ",")
            numList.clear()
    if i == 100:
        print(*numList,sep = ",")
