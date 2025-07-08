con = ("山羊座","水瓶座","魚座","牡羊座","牡牛座","双子座","蟹座","獅子座","乙女座","天秤座","蠍座","射手座")
change = (20,19,21,20,21,22,23,23,23,24,23,22)
month = int(input("生まれた月："))
day = int(input("生まれた日："))
try:
    if day < change[month - 1]:
        print(con[month - 1])
    elif month != 12:
        print(con[month])
    else:
        print(con[0])
except IndexError:
    print("そんな月はない")
