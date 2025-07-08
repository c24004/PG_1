x = input("生まれた年")
x += input("生まれた月")
x += input("生まれた日")
a = 0
b = 0
for i in x:
    a += int(i)
y = str(a)
for i in y:
    b += int(i)
print(f"あなたの運命数は{b}です")
